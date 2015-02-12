# -*- coding: utf8 -*-
from django.core.exceptions import ImproperlyConfigured
from django.db.models.fields.related import ReverseManyRelatedObjectsDescriptor
from django.db.models.loading import get_model
from django.db.models.signals import m2m_changed, post_delete, post_save
from django.dispatch import receiver

from . import handlers
from .settings import holonet_settings


@receiver(post_save, sender=get_model(*holonet_settings.RECIPIENT_MODEL.split('.')))
def recipient_change(instance, created, update_fields, *args, **kwargs):
    handlers.handle_recipient_change(instance, created, update_fields)


@receiver(post_delete, sender=get_model(*holonet_settings.RECIPIENT_MODEL.split('.')))
def recipient_delete(instance, *args, **kwargs):
    handlers.handle_recipient_delete(instance)


def mapping_change(instance, created, update_fields, *args, **kwargs):
    handlers.handle_mapping_change(instance, created, update_fields)


def mapping_delete(instance, *args, **kwargs):
    handlers.handle_mapping_delete(instance)


def mapping_recipient_list_change(instance, action, *args, **kwargs):
    if action.startswith('post'):
        handlers.handle_mapping_change(instance, created=False, updated_fields=None, force=True)


def add_signal_listeners():
    for table, properties in holonet_settings.MAPPING_MODELS.items():
        model = get_model(*table.split('.'))
        post_save.connect(mapping_change, model)
        post_delete.connect(mapping_delete, model)

        # Add signal på many to many relations
        relation_list = properties.get('recipient_relations', [])
        if not isinstance(relation_list, list):
            raise ImproperlyConfigured('recipient_relations needs to be a list of strings.')

        for relation in relation_list:
            if not isinstance(relation, str):
                raise ImproperlyConfigured('Each item in recipient_relations need to be a string.')

            relation_field = getattr(model, relation, None)
            if relation_field is None:
                raise ImproperlyConfigured('Could not find the relation_field on the model.')

            if not isinstance(relation_field, ReverseManyRelatedObjectsDescriptor):
                raise ImproperlyConfigured('The relation field needs to be of type '
                                           'models.ManyToManyField')

            m2m_changed.connect(mapping_recipient_list_change, relation_field.through)

add_signal_listeners()
