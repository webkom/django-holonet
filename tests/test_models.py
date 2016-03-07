# -*- coding: utf-8 -*-

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from mock import patch

from .models import Mapping1


class MappingModelTestCase(TestCase):

    @patch('holonet_django.handlers.handle_mapping_change')
    def test_force_update(self, mock_handler):
        mapping = Mapping1(mail_prefix='holonet_test')

        # Test no pk
        mapping.force_mail_update()
        self.assertEqual(mock_handler.call_count, 0)

        # Test for saved element
        mapping.save()
        mock_handler.assert_called_once_with(mapping, created=True, updated_fields=None)
        mock_handler.reset_mock()

        mapping.force_mail_update()
        mock_handler.assert_called_once_with(mapping, created=False, updated_fields=None,
                                             force=True)

    def test_mapping_id_no_pk(self):
        mapping = Mapping1(mail_prefix='holonet_test')
        self.assertRaises(ValueError, mapping.get_mapping_id)

    def test_mapping_id(self):
        mapping = Mapping1(mail_prefix='holonet_test')
        mapping.save()
        self.assertEquals(mapping.get_mapping_id(), '%s.%s' %
                          (ContentType.objects.get_for_model(mapping), mapping.pk))
