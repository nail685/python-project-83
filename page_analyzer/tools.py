from urllib.parse import urlparse

import requests
import validators
from bs4 import BeautifulSoup


def is_valid(url):
    return (len(url) <= 255 and validators.url(url))


def normalize_url(url):
    url_parse = urlparse(url)
    scheme = url_parse.scheme
    hostname = url_parse.netloc
    return f'{scheme.lower()}://{hostname.lower()}'


def get_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    return response


def get_status_code(response):
    return response.status_code


def get_tags(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    
    find_h1 = soup.find("h1")
    h1 = '' if find_h1 is None else find_h1.text
    if len(h1) > 255:
        h1 = h1[:254]
            
    find_title = soup.find("title")
    title = '' if find_title is None else find_title.text
    if len(title) > 255:
        title = title[:254]
            
    find_meta = soup.find("meta", {"name": "description"})
    if find_meta and "content" in find_meta.attrs:
        meta = find_meta["content"]
        if len(meta) > 255:
            meta = meta[:254]
    else:
        meta = ""

    return {"h1": h1, "title": title, "description": meta}
