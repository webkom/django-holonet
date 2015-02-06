# -*- coding: utf8 -*-

from holonet_django.settings import holonet_settings


def handle_recipient_change(recipient):
    id = getattr(recipient, holonet_settings.RECIPIENT_UNIQUE_IDENTIFIER_FIELD, None)
    email = getattr(recipient, holonet_settings.RECIPIENT_EMAIL_FIELD, None)

    if id is None:
        raise RuntimeError('Holonet could not find the unique field %s.' %
                           holonet_settings.RECIPIENT_UNIQUE_IDENTIFIER_FIELD)

    return id, email
