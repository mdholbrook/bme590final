# IMPORTS
import logging.handlers
import datetime
import binascii
from flask import Flask, jsonify, request
from pymodm import errors
from pymodm import connect
from Server.mongoSetup import User
from Server.serverHelper import check_user_data, decode_images, encode_images
from ImageProcessing.ImgFunctions import histogram_eq, contrast_stretching, \
    log_compression, reverse_video, gamma_correction, view_histogram_bw, \
    view_color_histogram


# FLASK SERVER SETUP
app = Flask(__name__)
formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = logging.handlers.RotatingFileHandler(
        'app.log',
        maxBytes=1024 * 1024)
handler.setFormatter(formatter)
handler.setLevel("DEBUG")
app.logger.addHandler(handler)


# SERVER ENDPOINT
@app.route("/new_user", methods=["POST"])
def process_images():
    """
    Takes in a request dictionary containing:
        'email' : String representing the user's email
        'hist' : boolean of whether this post-processing method was toggled
        'cont' : boolean of whether this post-processing method was toggled
        'log' : boolean of whether this post-processing method was toggled
        'rev' : boolean of whether this post-processing method was toggled
        'median' : boolean of whether this post-processing method was toggled
        # TODO: write image encode on client side
        'images' : list of ByteString(s)
        # TODO: add whatever other inputs aren't reflected here yet

    Returns: A tuple of length 2.  The first entry is a JSON dictionary for use
    by the client GUI containing the following key-value pairs:

        "proc_im": a list of base64-encoded postprocessed images
        "histDataOrig": a list of histogram data for each original image.  each
            entry is a list that contains two more lists, one for bins and one
            for intensity values.  the list of bins contains integers, and the
            list of intensity values can contain either integers or lists of 3
            integers, depending on whether the image is black and white or
            RGB color, respectively.
        "histDataProc": a list of histogram data for each postprocessed image.
            harbors the same data structure as above.
        "upload_timestamp": a String representing the time at which the server
            received the uploaded images and data
        "latency": a String representing the total latency on the server side

    # TODO: add whatever other outputs aren't reflected here yet
    -list of images that couldn't be read

    The second entry is an integer representing the HTTP status code.
    """
    # Reads in and validates the inputs from the request JSON
    user_data = request.get_json()
    upload_time = datetime.datetime.now()
    try:
        validated_user_data = check_user_data(user_data)
    except KeyError:
        return jsonify("User data dictionary missing keys."), 400
    except ValueError:
        return jsonify("Invalid user attribute sent to server."), 400
    except TypeError:
        return jsonify("User attribute of incorrect type sent to server."), 400
    except RuntimeError:
        return jsonify("Too many postprocessing options chosen."), 400

    # Pulls from the database if there is an existing user, otherwise
    # initializes a new one
    try:
        user = User.Objects.raw(({"_email": validated_user_data["email"]})
                                .first())
        user.uploadedImages = validated_user_data["images"],
        user.uploadTimestamp = upload_time,
        user.processedImages = [],
        user.processTimestamp = "",
        # user.returnExtension = validated_user_data["extension"]
    except errors.DoesNotExist:
        user = User(validated_user_data["email"],
                    previousMetrics={"hist": [0, []],
                                     "cont": [0, []],
                                     "log": [0, []],
                                     "rev": [0, []],
                                     "median": [0, []]},
                    uploadedImages=validated_user_data["images"],
                    uploadTimestamp=upload_time,
                    processedImages=[],
                    processTimestamp="",
                    # returnExtension=validated_user_data["extension"]
                    )
    user.save()

    # Decodes the uploaded images
    try:
        raw_images = decode_images(user.uploadedImages)
    except binascii.Error:
        return jsonify("One of the images was not encoded properly."), 400

    # Calculates histogram data for all original images and packages it
    # to return to GUI client
    orig_histogram_data = []
    for image in user.uploadedImages:
        data_per_image = []
        if image.shape[2] == 1:
            hist, bins = view_histogram_bw(image)
        else:
            hist, bins = view_color_histogram(image)
        data_per_image[0] = bins
        data_per_image[1] = hist
        orig_histogram_data.append(data_per_image)

    # Processes the images and updates the database accordingly
    transformed_image = []
    processing_latency = []
    for image in raw_images:
        if validated_user_data["hist"]:
            transformed_image.append(histogram_eq(image))
            process_time = datetime.datetime.now()
            user.previousMetrics["hist"][0] += 1
            processing_latency.append(process_time-upload_time)
            user.previousMetrics["hist"][1].append(process_time-upload_time)
        elif validated_user_data["cont"]:
            transformed_image.append(contrast_stretching(image))
            process_time = datetime.datetime.now()
            user.previousMetrics["cont"][0] += 1
            processing_latency.append(process_time-upload_time)
            user.previousMetrics["cont"][1].append(process_time-upload_time)
        elif validated_user_data["log"]:
            transformed_image.append(log_compression(image))
            process_time = datetime.datetime.now()
            user.previousMetrics["log"][0] += 1
            processing_latency.append(process_time-upload_time)
            user.previousMetrics["log"][1].append(process_time-upload_time)
        elif validated_user_data["rev"]:
            transformed_image.append(reverse_video(image))
            process_time = datetime.datetime.now()
            user.previousMetrics["rev"][0] += 1
            processing_latency.append(process_time-upload_time)
            user.previousMetrics["rev"][1].append(process_time-upload_time)
        elif validated_user_data["median"]:
            transformed_image.append(gamma_correction(image))
            process_time = datetime.datetime.now()
            user.previousMetrics["median"][0] += 1
            processing_latency.append(process_time-upload_time)
            user.previousMetrics["median"][1].append(process_time-upload_time)
    user.processedImages = transformed_image
    user.processTimestamp = process_time

    # Calculates histogram data for all processed images and packages it
    # to return to GUI client
    proc_histogram_data = []
    # TODO: Properly record image sizes in pixels
    image_sizes = []
    for image in user.processedImages:
        # image_sizes.append(image.size)
        data_per_image = []
        if image.shape[2] == 1:
            hist, bins = view_histogram_bw(image)
        else:
            hist, bins = view_color_histogram(image)
        data_per_image[0] = bins
        data_per_image[1] = hist
        proc_histogram_data.append(data_per_image)

    # Encodes the processed images to prepare to return them to the client
    images_to_return = encode_images(user.processedImages)

    # Calculates the total latency of processing all images
    total_latency = upload_time-upload_time
    for latency in processing_latency:
        total_latency += latency

    return jsonify({"proc_im": images_to_return,
                    "histDataOrig": orig_histogram_data,
                    "histDataProc": proc_histogram_data,
                    "upload_timestamp": user.uploadTimestamp,
                    "latency": total_latency,
                    "image_sizes": image_sizes}), 200


if __name__ == "__main__":
    connect("mongodb://alanr:bme590final@ds241493.mlab.com:41493/bme590final")
    app.run()
