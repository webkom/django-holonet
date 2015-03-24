# -*- coding: utf8 -*-

from . import api
from .exceptions import HolonetConfigrationError
from .settings import holonet_settings


def handle_recipient_change(recipient, created, updated_fields):
    identifier_field = getattr(recipient, holonet_settings.RECIPIENT_UNIQUE_IDENTIFIER_FIELD, None)
    email = getattr(recipient, holonet_settings.RECIPIENT_EMAIL_FIELD, None)

    if identifier_field is None:
        raise HolonetConfigrationError('Holonet could not find the unique field %s.' %
                                       holonet_settings.RECIPIENT_UNIQUE_IDENTIFIER_FIELD)

    api.change_recipient(identifier_field, email)


def handle_mapping_change(mapping, created, updated_fields, force=False):
    api.change_mapping(mapping, created)


def handle_recipient_delete(recipient):
    identifier_field = getattr(recipient, holonet_settings.RECIPIENT_UNIQUE_IDENTIFIER_FIELD, None)

    if identifier_field is None:
        raise HolonetConfigrationError('Holonet could not find the unique field %s.' %
                                       holonet_settings.RECIPIENT_UNIQUE_IDENTIFIER_FIELD)

    api.delete_recipient(identifier_field)


def handle_mapping_delete(mapping):
    api.delete_mapping(mapping)
