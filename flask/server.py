# IMPORTS
from flask import Flask, jsonify, request
import logging.handlers
import datetime

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


# SERVER ENDPOINTS
@app.route("/new_user", methods=["POST"])
def post_new_user():
    """
    Takes in request dictionary containing:
        'email' : String representing the user's email
        'load_filenames' : list of String(s) representing the filepath(s)
        'hist' : boolean of whether this post-processing method was toggled
        'cont' : boolean of whether this post-processing method was toggled
        'log' : boolean of whether this post-processing method was toggled
        'rev' : boolean of whether this post-processing method was toggled
        'median' : boolean of whether this post-processing method was toggled

        uploaded image(s) : list of ByteStrings
        extension type of requested return image --> String

    Fields for database:
        -user's email address --> String (primary key)
        -dictionary with:
            -previously selected modes of postprocessing as keys -->
            list of whatever data type that ends up being
            -list as value with:
                -frequency of previously selected modes --> int
                -list of latencies (i.e. runtime) of all previous trials of
                said postprocessing action --> list of floats
        -currently uploaded image(s) --> list of ByteStrings
        -timestamp of current request receipt --> String (datetime)
        -currently postprocessed image(s) --> list of ByteStrings
        -timestamp of current image postprocessing completion --> String
        (datetime)
        -current extension type of requested return image --> String

    Returns: A tuple of length 2.  The first entry is a JSON dictionary for use
    by the client GUI containing the following key-value pairs:

    <Insert key-value pairs here>

    The second entry is an integer representing the HTTP status code.
    """
    user_data = request.get_json()
    upload_time = datetime.datetime.now()
    from flask.validateServer import check_user_data
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

    # TODO: initialize user in the Mongo database

    # TODO: Check number of images; prepare to loop through if necessary

    transformed_image = []

    if validated_user_data["hist"]:
        # TODO: add histogram equalization function here
        print()
    elif validated_user_data["cont"]:
        # TODO: add contrast stretching function here
        print()
    elif validated_user_data["log"]:
        # TODO: add log compression function here
        print()
    elif validated_user_data["rev"]:
        # TODO: add reverse video function here
        print()
    elif validated_user_data["median"]:
        # TODO: add median function here
        print()

    return jsonify(), 200


if __name__ == "__main__":
    # TODO: Add Mongo connect here
    app.run()
