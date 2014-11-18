#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from holonet.settings import CLIENT_ID


class TestHolonetSettings(unittest.TestCase):

    def test_client_id(self):
        self.assertIsNone(CLIENT_ID)
