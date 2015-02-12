# -*- coding: utf8 -*-

from django.db.models import SlugField


class MailPrefixField(SlugField):

    def __init__(self, *args, **kwargs):
        if 'max_length' in kwargs:
            del kwargs['max_length']
        super(MailPrefixField, self).__init__(max_length=100, blank=False, null=False, *args,
                                              **kwargs)
