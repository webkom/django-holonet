# -*- coding: utf8 -*-

from django.test import TestCase

from holonet_django.validators import (ValidationError, is_prefix_unique, validate_email,
                                       validate_local_part, validate_prefix)


class ValidatorsTestCase(TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email('test@holonet.no'))

        self.assertFalse(validate_email('test@test@holonet.no'))

    def test_validate_local_part(self):
        self.assertTrue(validate_local_part('test'))

        self.assertFalse(validate_local_part('test@holonet.no'))

    def test_is_mapping_unique(self):
        self.assertTrue(is_prefix_unique('test', 'tests.Mapping1.1'))

    def test_validate_prefix(self):
        self.assertIsNone(validate_prefix('test_holonet'))
        self.assertRaises(ValidationError, validate_prefix, 'test@holonet.no')
