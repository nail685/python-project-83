from urllib.parse import urlparse

import requests
import validators
from bs4 import BeautifulSoup


def validate(url):
    return (len(url) <= 255 and validators.url(url))


def normalize_url(url):
    url_parse = urlparse(url)
    scheme = url_parse.scheme
    hostname = url_parse.netloc
    return f'{scheme.lower()}://{hostname.lower()}'


def get_status_code(response):
    return response.status_code


def get_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    return response


def get_tags(response):
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.find('title').text or ''
    h1 = soup.find('h1').text or ''
    meta = soup.find('meta', {'name': "description"})
    if meta['content']:
        meta = meta['content']
    else:
        meta = ''
    return {'h1': h1, 'title': title, 'description': meta}
