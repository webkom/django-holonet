# -*- coding: utf8 -*-

from django.test import TestCase

from holonet_django.validators import ValidationError, domain_validator, local_validator


class ValidatorsTestCase(TestCase):

    def test_validate_local_part(self):
        validator = local_validator
        self.assertIsNone(validator('holonet'))
        self.assertRaises(ValidationError, validator, 'error@address')

    def test_validate_domain(self):
        validator = domain_validator
        self.assertIsNone(validator('holonet.com'))
        self.assertRaises(ValidationError, validator, 'holonet')
