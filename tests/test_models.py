#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.contenttypes.models import ContentType
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

    def test_mapping_id_no_pk(self):
        mapping = Mapping1(mail_prefix='holonet_test')
        self.assertRaises(ValueError, mapping.get_mapping_id)

    def test_mapping_id(self):
        mapping = Mapping1(mail_prefix='holonet_test')
        mapping.save()
        self.assertEquals(mapping.get_mapping_id(), '%s.%s' %
                          (ContentType.objects.get_for_model(mapping), mapping.pk))
