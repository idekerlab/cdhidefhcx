#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cdhidefhcx` package."""


import unittest
from cdhidefhcx.runner import CdhidefhcxRunner


class TestCdhidefhcxrunner(unittest.TestCase):
    """Tests for `cdhidefhcx` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_constructor(self):
        """Tests constructor"""
        myobj = CdhidefhcxRunner(0)

        self.assertIsNotNone(myobj)

    def test_run(self):
        """ Tests run()"""
        myobj = CdhidefhcxRunner(4)
        self.assertEqual(4, myobj.run())