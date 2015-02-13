# -*- coding: utf8 -*-
from django.db.models.fields.related import ReverseManyRelatedObjectsDescriptor
from django.db.models.loading import get_model
from django.db.models.signals import m2m_changed, post_delete, post_save, pre_save
from django.dispatch import receiver

from . import handlers, validators
from .exceptions import HolonetConfigrationError
from .settings import holonet_settings


@receiver(post_save, sender=get_model(*holonet_settings.RECIPIENT_MODEL.split('.')))
def recipient_change(instance, created, update_fields, *args, **kwargs):
    handlers.handle_recipient_change(instance, created, update_fields)


@receiver(post_delete, sender=get_model(*holonet_settings.RECIPIENT_MODEL.split('.')))
def recipient_delete(instance, *args, **kwargs):
    handlers.handle_recipient_delete(instance)


@receiver(pre_save, sender=get_model(*holonet_settings.RECIPIENT_MODEL.split('.')))
def pre_save_recipient_check(instance, *args, **kwargs):
    field = getattr(instance, holonet_settings.RECIPIENT_EMAIL_FIELD, None)
    validation = validators.validate_email(field)
    if not validation:
        raise ValueError('The email value is not valid.')


def mapping_change(instance, created, update_fields, *args, **kwargs):
    handlers.handle_mapping_change(instance, created, update_fields)


def mapping_delete(instance, *args, **kwargs):
    handlers.handle_mapping_delete(instance)


def mapping_recipient_list_change(instance, action, *args, **kwargs):
    if action.startswith('post'):
        handlers.handle_mapping_change(instance, created=False, updated_fields=None, force=True)


def pre_save_mapping_check(instance, *args, **kwargs):
    prefix = instance.mail_prefix
    validation = validators.validate_local_part(prefix)
    is_unique = validators.is_prefix_unique(prefix, instance.get_mapping_id)
    if not validation:
        raise ValueError('The mail prefix is not valid.')
    if not is_unique:
        raise ValueError('The selected mapping prefix is not unique.')


def add_signal_listeners():
    for table, properties in holonet_settings.MAPPING_MODELS.items():
        model = get_model(*table.split('.'))
        post_save.connect(mapping_change, model)
        post_delete.connect(mapping_delete, model)
        pre_save.connect(pre_save_mapping_check, model)

        # Add signal på many to many relations
        relation_list = properties.get('recipient_relations', [])
        if not isinstance(relation_list, list):
            raise HolonetConfigrationError('recipient_relations needs to be a list of strings.')

        for relation in relation_list:
            if not isinstance(relation, str):
                raise HolonetConfigrationError('Each item in recipient_relations need to be a '
                                               'string.')

            relation_field = getattr(model, relation, None)
            if relation_field is None:
                raise HolonetConfigrationError('Could not find the relation_field on the model.')

            if not isinstance(relation_field, ReverseManyRelatedObjectsDescriptor):
                raise HolonetConfigrationError('The relation field needs to be of type '
                                               'models.ManyToManyField')

            m2m_changed.connect(mapping_recipient_list_change, relation_field.through)

add_signal_listeners()
