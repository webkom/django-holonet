# -*- coding: utf8 -*-
import requests

from .exceptions import HolonetInvalidAPIKey
from .settings import holonet_settings


def api_key():
    if holonet_settings.API_KEY is None or not isinstance(holonet_settings.API_KEY, str):
        raise HolonetInvalidAPIKey()
    return holonet_settings.API_KEY


def api_request(path, data=None, delete=False):
    url = '{}/{}'.format(holonet_settings.HOLONET_API_URL, path)
    if data is None:
        return requests.get(url)
    elif delete:
        return requests.delete(url)
    else:
        return requests.post(url, data)


def change_recipient(tag, address):
    return api_request('recipients/{}/'.format(tag), data={
        'tag': tag,
        'address': address
    })


def delete_recipient(tag):
    return api_request('recipients/{}/'.format(tag), delete=True)


def change_mapping(mapping, created):
    return api_request('mappings/{}/'.format(mapping.mail_prefix), data={
        'mail_prefix': mapping.mail_prefix,
        'recipients': mapping.get_reciptients()
    })


def delete_mapping(mapping):
    return api_request('mappings/{}/'.format(mapping.mail_prefix), delete=True)
