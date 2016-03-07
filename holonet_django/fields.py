# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import validators


class LocalPartField(models.CharField):
    """
    This class represents a model field that stores the local part of an email address. The local
    part is case insensitive.
    """
    description = _('Local part of an email address')
    default_validators = [validators.local_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 254)
        super(LocalPartField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'error_messages': {
                'invalid': _('Enter a valid local_part.'),
            }
        }
        defaults.update(kwargs)
        return super(LocalPartField, self).formfield(**defaults)

    def clean(self, value, model_instance):
        value = super(LocalPartField, self).clean(value, model_instance)
        value = value.lower()
        return value
