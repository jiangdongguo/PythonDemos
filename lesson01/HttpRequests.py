import requests


def send_get(urlPath):
    response = requests.get(url=urlPath)
    return response.text
