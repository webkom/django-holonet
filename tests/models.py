# -*- coding: utf8 -*-

from django.db import models

from holonet_django.models import MailMapping


class TestRecipientModel(models.Model):

    username = models.CharField(max_length=100)
    email = models.EmailField()


class Mapping1(MailMapping):
    recipients = models.ManyToManyField(TestRecipientModel)

    invalid_test_field = 'Just a test value'

    def get_recipients(self):
        return self.recipients.all()


class Mapping2(MailMapping):

    def get_recipients(self):
        return None
