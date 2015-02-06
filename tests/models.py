# -*- coding: utf8 -*-

from django.db import models


class TestRecipientModel(models.Model):

    username = models.CharField(max_length=100)
    email = models.EmailField()


class Mapping1(models.Model):
    pass


class Mapping2(models.Model):
    pass
