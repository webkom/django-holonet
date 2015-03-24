# -*- coding: utf8 -*-

from .exceptions import HolonetInvalidAPIKey
from .settings import holonet_settings


def api_key():
    if holonet_settings.API_KEY is None or not isinstance(holonet_settings.API_KEY, str):
        raise HolonetInvalidAPIKey()
    return holonet_settings.API_KEY


def change_recipient(tag, address):
    pass


def delete_recipient(tag):
    pass


def change_mapping(mapping, created):
    pass


def delete_mapping(tag):
    pass
