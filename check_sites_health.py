import requests
from whois import whois
from sys import argv
from datetime import datetime

# TODO freeze > requirements

def load_urls4check(filepath):
    with open(filepath, "r") as textfile:
        urls = textfile.read().splitlines()
    return urls


def is_server_respond_with_200(url):
    return requests.get(url).ok


def get_domain_expiration_date(domain_name):
    whois_data = whois(domain_name)
    return whois_data['expiration_date']


if __name__ == '__main__':
    filepath = argv[1]
    urls = load_urls4check(filepath)
    for url in urls:
        print(url)
        print('Отвечает на запрос статусом HTTP 200: ', is_server_respond_with_200(url))
        tdelta = get_domain_expiration_date(url) - datetime.now()
        print('Доменное имя проплачено как минимум на 1 месяц вперед: ', tdelta.days > 30)
        print()
