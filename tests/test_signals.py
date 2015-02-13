#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.utils import override_settings
from mock import Mock

from holonet_django import handlers, validators
from holonet_django.exceptions import HolonetConfigrationError
from holonet_django.signals import (add_signal_listeners, pre_save_mapping_check,
                                    pre_save_recipient_check)
from tests.models import Mapping1, Mapping2, TestRecipientModel


class SignalsTestCase(TestCase):

    def test_recipient_signal(self):

        handlers.handle_recipient_change = Mock()

        test_object = TestRecipientModel(username='test', email='test@holonet.no')
        test_object.save()

        handlers.handle_recipient_change.assert_called_with(test_object, True, None)

    def test_mapping_signal(self):
        handlers.handle_mapping_change = Mock()

        mapping1 = Mapping1(mail_prefix='holonet_test')
        mapping1.save()

        mapping2 = Mapping2(mail_prefix='holonet_test')
        mapping2.save()

        handlers.handle_mapping_change.assert_any_call(mapping1, True, None)
        handlers.handle_mapping_change.assert_any_call(mapping2, True, None)
        self.assertEquals(handlers.handle_mapping_change.call_count, 2)

    def test_recipient_delete_signal(self):
        handlers.handle_recipient_delete = Mock()

        test_object = TestRecipientModel(username='test', email='test@holonet.no')
        test_object.save()
        test_object.delete()

        handlers.handle_recipient_delete.assert_called_once(test_object)

    def test_mapping_recipient_list_change(self):
        mapping1 = Mapping1(mail_prefix='holonet_test')
        mapping1.save()

        test_object = TestRecipientModel(username='test', email='test@holonet.no')
        test_object.save()

        mapping1.recipients.add(test_object)

    def test_mapping_delete_signal(self):
        handlers.handle_mapping_delete = Mock()

        mapping = Mapping1(mail_prefix='holonet_test')
        mapping.save()

        mapping.delete()

        handlers.handle_mapping_delete.assert_called_once_with(mapping)

    @override_settings(HOLONET_MAPPING_MODELS={
        'tests.Mapping1': {
            'recipient_relations': False
        }
    })
    def test_mapping_init_no_list(self):
        self.assertRaisesMessage(
            HolonetConfigrationError,
            'recipient_relations needs to be a list of strings.',
            add_signal_listeners
        )

    @override_settings(HOLONET_MAPPING_MODELS={
        'tests.Mapping1': {
            'recipient_relations': [False]
        }
    })
    def test_mapping_init_no_string_list(self):
        self.assertRaisesMessage(
            HolonetConfigrationError,
            'Each item in recipient_relations need to be a string.',
            add_signal_listeners
        )

    @override_settings(HOLONET_MAPPING_MODELS={
        'tests.Mapping1': {
            'recipient_relations': ['does_not_excist_field']
        }
    })
    def test_mapping_init_list_not_field(self):
        self.assertRaisesMessage(
            HolonetConfigrationError,
            'Could not find the relation_field on the model.',
            add_signal_listeners
        )

    @override_settings(HOLONET_MAPPING_MODELS={
        'tests.Mapping1': {
            'recipient_relations': ['invalid_test_field']
        }
    })
    def test_mapping_init_no_list_invalid_field(self):
        self.assertRaisesMessage(
            HolonetConfigrationError,
            'The relation field needs to be of type models.ManyToManyField',
            add_signal_listeners
        )

    def test_recipient_pre_validator(self):
        self.assertIsNone(pre_save_recipient_check(TestRecipientModel(email='test@holonet.no')))

        self.assertRaises(ValueError, pre_save_recipient_check, TestRecipientModel())

    def test_mapping_pre_validation(self):
        validators.is_prefix_unique = Mock(side_effect=lambda x, y: True)

        self.assertIsNone(pre_save_mapping_check(Mapping1(mail_prefix='holonet_test')))
        self.assertRaisesMessage(ValueError, 'The mail prefix is not valid.',
                                 pre_save_mapping_check, Mapping1())

        orginal = validators.is_prefix_unique
        validators.is_prefix_unique = Mock(side_effect=lambda x, y: False)

        mapping = Mapping1(mail_prefix='holonet_test1')
        self.assertRaisesMessage(ValueError, 'The selected mapping prefix is not unique.',
                                 pre_save_mapping_check, mapping)

        validators.is_prefix_unique = orginal
