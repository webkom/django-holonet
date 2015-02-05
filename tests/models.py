# -*- coding: utf8 -*-

from django.db import models


class TestRecipientModel(models.Model):

    username = models.CharField(max_length=100)
    email = models.EmailField()
