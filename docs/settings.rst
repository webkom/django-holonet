Settings
--------

.. currentmodule:: django.conf.settings

.. attribute:: HOLONET_RECIPIENT_MODEL

    **Default:** `settings.AUTH_USER_MODEL`

    It holds all recipients. All changes in this model are automatically
    updated in Holonet.

.. attribute:: HOLONET_RECIPIENT_UNIQUE_IDENTIFIER_FIELD

    **Default:** `'pk'`

    The HOLONET_RECIPIENT_UNIQUE_IDENTIFIER_FIELD is a string with the name of
    the field in the model that is unique for all elements. the default is 'pk'

.. attribute:: HOLONET_RECIPIENT_EMAIL_FIELD

    **Default:** `'email'`

    The HOLONET_RECIPIENT_EMAIL_FIELD holds the fieldname that holds the email in
    the model.

.. attribute:: HOLONET_MAPPING_MODELS

    **Default:** `{}`

    This is a dict with all the mappings models which extends the MailMapping
    class. django-holonet would listen on changes on these models. Each key
    holds dictionary with settings for for the given mappingmodel. Below is a
    list of possible settings for a mappingmodel.

    * **recipient_relations** (optional): a list of ManyToManyFields with recipients.
      The to-relation of this field is not important, django-holonet will listen on
      changes and update the recipient list if there are changes in this relation,
      but get the recipient-list from get_recipients method on the MailMapping class.
      The get_recipients method needs to return a list of instances from the
      RECIPIENT_MODEL class.

    Example:
    ::
        HOLONET_MAPPING_MODELS = {
            'tests.Mapping1': {
                'recipient_relations': ['recipients']
            },
            'tests.Mapping2': {}
        }
