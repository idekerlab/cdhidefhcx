#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Integration Tests for `cdhidefhcx` package."""

import os

import unittest
from cdhidefhcx import cdhidefhcxcmd

SKIP_REASON = 'CDHIDEFHCX_INTEGRATION_TEST ' \
              'environment variable not set, cannot run integration ' \
              'tests'

@unittest.skipUnless(os.getenv('CDHIDEFHCX_INTEGRATION_TEST') is not None, SKIP_REASON)
class TestIntegrationCdhidefhcx(unittest.TestCase):
    """Tests for `cdhidefhcx` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_something(self):
        """Tests parse arguments"""
        self.assertEqual(1, 1)
