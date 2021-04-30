import requests


def check_success(url):
    r = requests.get(url).status_code
    if 200 <= r <= 399:
        return "Success"
    else:
        return "Fail"
