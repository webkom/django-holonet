# -*- coding: utf8 -*-

from django.db.models.loading import get_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from holonet_django import handlers
from holonet_django.settings import holonet_settings


# Listen on changes on recpients
@receiver(post_save, sender=get_model(*holonet_settings.RECIPIENT_MODEL.split('.')))
def recipient_change(instance, *args, **kwargs):
    handlers.handle_recipient_change(instance)


# Listen on mapping changes
def mapping_change(instance, *args, **kwargs):
    handlers.handle_mapping_change(instance)


# Connect all mappingtables to signal
for table, properties in holonet_settings.MAPPING_MODELS.items():
    post_save.connect(mapping_change, get_model(*table.split('.')))