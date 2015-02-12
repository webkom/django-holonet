# -*- coding: utf8 -*-

from django.core.validators import validate_email as django_email_validate
from django.core.validators import EmailValidator, ValidationError


class PrefixValidator(EmailValidator):

    def __call__(self, prefix):
        value = '%s@holonet.no' % prefix
        super(PrefixValidator, self).__call__(value)

validate_prefix = PrefixValidator()


def validate_email(email):
    try:
        django_email_validate(email)
        return True
    except ValidationError:
        pass
    return False


def validate_local_part(local_part):
    return validate_email('%s@holonet.no' % local_part)


def is_prefix_unique(prefix, mapping_identifier):
    # Todo: Ask the api about this mapping uniqueness
    return True
