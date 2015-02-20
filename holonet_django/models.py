# -*- coding: utf8 -*-

from abc import abstractmethod

from django.contrib.contenttypes.models import ContentType
from django.db import models

from . import handlers
from .fields import MailPrefixField


class MailMapping(models.Model):
    """
    Extend this model to create mappings.
    """

    mail_prefix = MailPrefixField()

    class Meta:
        abstract = True

    @abstractmethod
    def get_recipients(self):
        """
        Return all recipients of this mapping.
        Implement this function and return a list of recipients.
        Returns list of recipients. This needs to be of the same type as the RECIPIENT_MODEL class
        defined in settings.
        """
        raise NotImplementedError('Please impliment the get_recipients on the mapping model.')

    def force_mail_update(self):
        """
        This function forces update of the list. Use this if you don't store recipients in a
        many to many relation.
        """
        if self.pk:
            handlers.handle_mapping_change(self, created=False, updated_fields=None, force=True)

    def get_mapping_id(self):
        if not self.pk:
            raise ValueError('The model needs to have a pk before you can get the id.')
        return '%s.%s' % (ContentType.objects.get_for_model(self), self.pk)
