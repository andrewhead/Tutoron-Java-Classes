#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import logging
import unittest

from tutorons.modules.java_classes.views import explain_code


logging.basicConfig(level=logging.INFO, format="%(message)s")


class FooExplanationTest(unittest.TestCase):

    def test_explain_ArrayList_with_insight(self):
        explanation = explain_code("ArrayList")
        self.assertIn("list returned from asList", explanation)
