import requests


class colors:
    PINK = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def download_emoji(url, file_path):
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)

