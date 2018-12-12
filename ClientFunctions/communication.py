import requests


def send_to_server(df):
    """
    Posts GUI info to server for imageprocessing endpoint
    Args:
        df: Dictionary of GUI info

    Returns: Posts a request to server

    """
    ext = ""
    if df["JPEG"]:
        ext = "JPEG"
    elif df["PNG"]:
        ext = "PNG"
    elif df["TIFF"]:
        ext = "TIFF"
    requests.post("https://vcm-7640.vm.duke.edu/imageprocessing", json={
        "email": df['email'],
        "hist": df['hist'],
        "cont": df['cont'],
        "log": df['log'],
        "rev": df['rev'],
        "median": df['median'],
        "images": df['orig_im'],
        "extension": ext
    })
