#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.test import TestCase
from mock import Mock

from holonet_django import handlers
from tests.models import TestRecipientModel


class SignalsTestCase(TestCase):

    def test_recipient_signal(self):

        handlers.handle_recipient_change = Mock(side_effect=lambda x: x)

        test_object = TestRecipientModel(username='test', email='test@holonet.no')
        test_object.save()

        handlers.handle_recipient_change.assert_called_with(test_object)
