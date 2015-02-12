# -*- coding: utf8 -*-

from django.db.models import SlugField

from . import validators


class MailPrefixField(SlugField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 100
        kwargs['blank'] = False
        kwargs['null'] = False
        kwargs['unique'] = True
        kwargs['validators'] = [validators.validate_prefix]
        super(MailPrefixField, self).__init__(*args, **kwargs)
