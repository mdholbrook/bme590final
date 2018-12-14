import requests
from Server.serverHelper import *


def send_to_server(df):
    """
    Posts GUI info to server and runs through all endpoints to ultimately
    return the required data for display
    Args:
        df: Dictionary of GUI info

    Returns: The output of the new_user endpoint (see documentation)
    """

    # Load communication information
    comms = read_comms()
    send_address = comms[1]

    encoded_images = encode_images_from_file(df['load_filenames'])
    # json_dict, code = requests.post(
    #     "https://vcm-7291.vm.duke.edu/new_user", json={
    #         "email": df['email'],
    #         "hist": df['hist'],
    #         "cont": df['cont'],
    #         "log": df['log'],
    #         "rev": df['rev'],
    #         "median": df['median'],
    #         "images": encoded_images,
    #     }).json()

    try:
        json_dict = requests.post(
            send_address + "/new_user", json={
                "email": df['email'],
                "hist": df['hist'],
                "cont": df['cont'],
                "log": df['log'],
                "rev": df['rev'],
                "gamma": df['gamma'],
                "images": encoded_images,
            }).json()

        # json_dict['error'] = ['']
    #
    except BaseException:
        return 'Server unavailable!'

    # Decode images
    json_dict["proc_im"] = decode_images(json_dict["proc_im"])
    print(json_dict["proc_im"])

    return json_dict
