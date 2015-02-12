django-holonet |Build status| |Coverage status| |pypi version|
==============================================================

This package is used to control holonet from a django project.


Quickstart
----------

Install django-holonet:

    $ pip install django-holonet


Settings
--------

HOLONET_RECIPIENT_MODEL = 'appname.Modelname'
    The HOLONET_RECIPIENT_MODEL holds all recipients. All changes in this model are automatically updated in Holonet. The default is settings.AUTH_USER_MODEL.

HOLONET_RECIPIENT_UNIQUE_IDENTIFIER_FIELD = 'fieldname'
    The HOLONET_RECIPIENT_UNIQUE_IDENTIFIER_FIELD is a string with the name of the field in the model that is unique for all elements. the default is 'pk'

HOLONET_RECIPIENT_EMAIL_FIELD = 'fieldname'
    The HOLONET_RECIPIENT_EMAIL_FIELD holds the fieldname that holds the email in the model. The default is 'email'.

HOLONET_MAPPING_MODELS = {}
    This is a dict with all the mappings models which extends the MailMapping class. django-holonet would listen on changes on these models. Each key holds dictionary with settings for for the given mappingmodel. Below is a list of possible settings for a mappingmodel.

* **recipient_relations** (optional): a list of ManyToManyFields with recipients. The to-relation of this field is not important, django-holonet will listen on changes and update the recipient list if there are changes in this relation, but get the recipient-list from get_recipients method on the MailMapping class. The get_recipients method needs to return a list of instances from the RECIPIENT_MODEL class.

Example:
::
    HOLONET_MAPPING_MODELS={
        'tests.Mapping1': {
            'recipient_relations': ['recipients']
        },
        'tests.Mapping2': {}
    }



-------------------

MIT © Abakus Webkom


.. |Build status| image:: https://ci.frigg.io/badges/webkom/django-holonet/
        :target: https://ci.frigg.io/webkom/django-holonet/

.. |Coverage status| image:: http://ci.frigg.io/badges/coverage/webkom/django-holonet/
        :target: https://ci.frigg.io/webkom/django-holonet/

.. |pypi version| image:: https://badge.fury.io/py/django-holonet.png
    :target: http://badge.fury.io/py/django-holonet
