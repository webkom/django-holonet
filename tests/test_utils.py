from django.test import TestCase, override_settings

from holonet_django import utils


class UtilsTestCase(TestCase):

    @override_settings(HOLONET_API_URL='http://127.0.0.1/')
    def test_create_url(self):
        namespace = '/test/'
        endpoint = '/endpoint/'
        method = '/detail'

        self.assertEqual(utils.create_url(namespace, endpoint, method),
                         'http://127.0.0.1/api/test/endpoint/detail/')
