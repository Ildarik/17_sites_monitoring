import requests
from whois import whois
from sys import argv
from datetime import datetime

# TODO freeze > requirements

def load_urls4check(filepath):
    with open(filepath, "r") as textfile:
        urls = textfile.readlines()
    return urls


def is_server_respond_with_200(url):
    return requests.get(url).ok


def get_domain_expiration_date(domain_name):
    pass


if __name__ == '__main__':
    filepath = argv[1]
    urls = load_urls4check(filepath)
    for url in urls:
        pass
