# -*- coding: utf8 -*-

from abc import abstractmethod

from django.db import models

from . import handlers
from .fields import MailPrefixField


class MailMapping(models.Model):

    mail_prefix = MailPrefixField()

    @abstractmethod
    def get_recipients(self):
        """
        Return all recipients of this mapping.
        Implement this function and return a list of recipients.
        :return: list of recipients. This needs to be of the same type as the RECIPIENT_MODEL class
        defined in settings.
        """
        raise NotImplementedError('Please impliment the get_recipients on the mapping model.')

    def force_mail_update(self):
        """
        This function forces update of the list. Use this if you don't store recipients in a
        many to many relation.
        :return: None
        """
        if self.pk:
            handlers.handle_mapping_change(self, created=False, updated_fields=None, force=True)

    class Meta:
        abstract = True
