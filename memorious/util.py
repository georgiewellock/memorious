import os
from uuid import uuid4


def random_filename(path=None):
    """Make a UUID-based file name which is extremely unlikely
    to exist already."""
    filename = uuid4().hex
    if path is not None:
        filename = os.path.join(path, filename)
    return filename

def html_filename(path=None, url):
    """ Replace special characters in url and create filename using full url"""
    url = str(url)
    url = url.replace('/', '_')
    url = url.replace('?', '')
    filename = url.replace(':', '')
    if path is not None:
        filename = os.path.join(path, filename)
    return filename

def file_filename(path=None, url):
    url_parts = str(url).split('/')
    filename = url_parts[-1]
    if path is not None:
        filename = os.path.join(path, filename)
    return filename
