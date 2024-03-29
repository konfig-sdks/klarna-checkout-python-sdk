# coding: utf-8

"""
    Klarna Checkout API V3

    The checkout API is used to create a checkout with Klarna and update the checkout order during the purchase. As soon as the purchase is completed the order should be read and handled using the [`Order Management API`](https://docs.klarna.com/api/ordermanagement).\\n\\nRead more on [Klarna checkout](https://docs.klarna.com/klarna-checkout/).

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredMerchantUrls(TypedDict):
    # URL for the terms and conditions page of the merchant. The URL will be displayed inside the Klarna Checkout iFrame.(max 2000 characters) Example: \"https://merchant.com/terms\"
    terms: str

    # URL for the checkout page of the merchant. (max 2000 characters) Example: \"https://merchant.com/checkout\"
    checkout: str

    # URL of the merchant confirmation page. The consumer will be redirected back to the confirmation page if the authorization is successful after the customer clicks on the ‘Place Order’ button inside checkout. The special characters of the confirmation URL should be encoded, e.g. the \"space\" character should be written as \"%20\". Then, on top of that, the whole confirmation URL should be encoded. E.g. the \"space\" character should become \"%2520\". (max 2000 characters) Example: \"https://merchant.com/confirmation\"
    confirmation: str

    # URL that will be used for push notification when an order is completed. Should be different than checkout and confirmation URLs. (max 2000 characters) Example: \"https://merchant.com/push\"
    push: str

class OptionalMerchantUrls(TypedDict, total=False):
    # URL that will be requested for final merchant validation. (must be https, max 2000 characters) Example: \"https://merchant.com/validation\"
    validation: str

    # URL for notifications on pending orders. (max 2000 characters) Example: \"https://merchant.com/notification/{checkout.order.id}\"
    notification: str

    # URL for the cancellation terms page of the merchant. The URL will be displayed in the email that is sent to the customer after the order is captured.(max 2000 characters) Example: \"https://merchant.com/terms/cancelation\"
    cancellation_terms: str

    # URL for shipping option update. (must be https, max 2000 characters) Example: \"https://merchant.com/shippingoptionupdate\"
    shipping_option_update: str

    # URL for shipping, tax and purchase currency updates. Will be called on address changes. (must be https, max 2000 characters) Example: \"https://merchant.com/addressupdate\"
    address_update: str

    # URL for shipping, tax and purchase currency updates. Will be called on billing or shipping country changes. (must be https, max 2000 characters) Example: \"https://merchant.com/countrychange\"
    country_change: str

class MerchantUrls(RequiredMerchantUrls, OptionalMerchantUrls):
    pass
