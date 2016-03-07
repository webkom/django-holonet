# -*- coding: utf8 -*-

from .exceptions import HolonetConfigurationError
from .settings import holonet_settings


def handle_recipient_change(recipient, created, updated_fields):
    id = getattr(recipient, holonet_settings.RECIPIENT_UNIQUE_IDENTIFIER_FIELD, None)
    email = getattr(recipient, holonet_settings.RECIPIENT_EMAIL_FIELD, None)

    if id is None:
        raise HolonetConfigurationError('Holonet could not find the unique field %s.' %
                                        holonet_settings.RECIPIENT_UNIQUE_IDENTIFIER_FIELD)

    if email is None:
        raise HolonetConfigurationError('Holonet could not find the email field %s.' %
                                        holonet_settings.RECIPIENT_EMAIL_FIELD)

    print('change_recipient', id, email, created, updated_fields)


def handle_mapping_change(mapping, created, updated_fields, force=False):
    print('change_mapping', mapping, created, updated_fields, force)


def handle_recipient_delete(recipient):
    identifier_field = getattr(recipient, holonet_settings.RECIPIENT_UNIQUE_IDENTIFIER_FIELD, None)

    if identifier_field is None:
        raise HolonetConfigurationError('Holonet could not find the unique field %s.' %
                                        holonet_settings.RECIPIENT_UNIQUE_IDENTIFIER_FIELD)

    print('delete_recipient', recipient)


def handle_mapping_delete(mapping):
    print('delete_mapping', mapping)
