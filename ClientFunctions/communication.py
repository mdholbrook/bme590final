import requests
from Server.serverHelper import encode_images, decode_images


def send_to_server(df):
    """
    Posts GUI info to server and runs through all endpoints to ultimately
    return the required data for display
    Args:
        df: Dictionary of GUI info

    Returns: The output of the new_user endpoint (see documentation)
    """
    encoded_images = encode_images(df['orig_im_names'])
    print(encoded_images)
    json_dict, code = requests.post(
        "https://vcm-7291.vm.duke.edu/new_user", json={
            "email": df['email'],
            "hist": df['hist'],
            "cont": df['cont'],
            "log": df['log'],
            "rev": df['rev'],
            "median": df['median'],
            "images": encoded_images,
        }).json()
    return json_dict, code


# if __name__ == "__main__":
#
#     # send_to_server({"email": "testing@duke.edu",
#     #                 "hist": False,
#     #                 "cont": True,
#     #                 "log": False,
#     #                 "rev": False,
#     #                 "median": False,
#     #                 "images": })
