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

from klarna_checkout_python_sdk.type.delivery_details_v1 import DeliveryDetailsV1
from klarna_checkout_python_sdk.type.selected_addon import SelectedAddon

class RequiredShippingOption(TypedDict):
    # id
    id: str

    # Name.
    name: str

    # Price including tax.
    price: int

    # Tax amount.
    tax_amount: int

    # Non-negative. In percent, two implicit decimals. I.e 2500 = 25%.
    tax_rate: int

class OptionalShippingOption(TypedDict, total=False):
    # Description.
    description: str

    # Promotion name. To be used if this shipping option is promotional.
    promo: str

    # If true, this option will be preselected when checkout loads. Default: false
    preselected: bool

    # Shipping method. Possible values:<ul><li>PickUpStore</li><li>Home</li><li>BoxReg</li><li>BoxUnreg</li><li>PickUpPoint</li><li>Own</li><li>Postal</li><li>DHLPackstation</li><li>Digital</li></ul> If DHLPackstation is selected the correct form will be displayed.
    shipping_method: str

    delivery_details: DeliveryDetailsV1

    # TMS reference. Required to map completed orders to shipments reserved in TMS.
    tms_reference: str

    selected_addons: typing.List[SelectedAddon]

class ShippingOption(RequiredShippingOption, OptionalShippingOption):
    pass
