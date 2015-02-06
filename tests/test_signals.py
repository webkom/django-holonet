#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.test import TestCase
from mock import Mock

from holonet_django import handlers
from tests.models import Mapping1, Mapping2, TestRecipientModel


class SignalsTestCase(TestCase):

    def test_recipient_signal(self):

        handlers.handle_recipient_change = Mock()

        test_object = TestRecipientModel(username='test', email='test@holonet.no')
        test_object.save()

        handlers.handle_recipient_change.assert_called_with(test_object)

    def test_mapping_signal(self):
        handlers.handle_mapping_change = Mock()

        mapping1 = Mapping1()
        mapping1.save()

        mapping2 = Mapping2()
        mapping2.save()

        handlers.handle_mapping_change.assert_any_call(mapping1)
        handlers.handle_mapping_change.assert_any_call(mapping2)
        self.assertEquals(handlers.handle_mapping_change.call_count, 2)
