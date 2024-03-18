# coding: utf-8

"""
    Klarna Checkout API V3

    The checkout API is used to create a checkout with Klarna and update the checkout order during the purchase. As soon as the purchase is completed the order should be read and handled using the [`Order Management API`](https://docs.klarna.com/api/ordermanagement).\\n\\nRead more on [Klarna checkout](https://docs.klarna.com/klarna-checkout/).

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from klarna_checkout_python_sdk import KlarnaCheckout

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        klarnacheckout = KlarnaCheckout(
        )
        self.assertIsNotNone(klarnacheckout)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
