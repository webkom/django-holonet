from django.test import TestCase

from holonet_django.fields import LocalPartField
from holonet_django.validators import ValidationError


class LocalPartFieldTestCase(TestCase):

    def setUp(self):
        self.field = LocalPartField()

    def test_clean(self):
        self.assertEquals(self.field.clean('ValidLocal', None), 'validlocal')
        self.assertRaises(ValidationError, self.field.clean, 'holonet@holonet.com', None)
