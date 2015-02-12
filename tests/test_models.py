#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from mock import Mock

from holonet_django import handlers

from .models import Mapping1


class MappingModelTestCase(TestCase):

    def test_force_update(self):
        handlers.handle_mapping_change = Mock()

        mapping = Mapping1(mail_prefix='holonet_test')

        # Test no pk
        mapping.force_mail_update()
        self.assertEqual(handlers.handle_mapping_change.call_count, 0)

        # Test for saved element
        mapping.save()
        mapping.force_mail_update()
        # Use twise because
        handlers.handle_mapping_change.assert_called_twise_with(mapping, False, None, True)
