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
from pydantic import BaseModel, Field, RootModel

from klarna_checkout_python_sdk.pydantic.product_identifiers import ProductIdentifiers
from klarna_checkout_python_sdk.pydantic.shipping_attributes import ShippingAttributes
from klarna_checkout_python_sdk.pydantic.subscription import Subscription

class OrderLine(BaseModel):
    # Descriptive name of the order line item (max 255 characters)
    name: str = Field(alias='name')

    # Non-negative number. Quantity of the order line item.
    quantity: int = Field(alias='quantity')

    # Minor units. Includes tax, excludes discount. (max value: 100000000).  Example: 100 Euros should be 10000.
    unit_price: int = Field(alias='unit_price')

    # Non-negative value. The percentage value is represented with two implicit decimals. (max 10000)  Example: 25% should be 2500.
    tax_rate: int = Field(alias='tax_rate')

    # Minor units. Includes tax and discount.   Example: 25 euros should be 2500 Value = (quantity x unit_price) - total_discount_amount. (max value: 100000000)
    total_amount: int = Field(alias='total_amount')

    # Must be within ±1 of total_amount - total_amount \\* 10000 / (10000 + tax_rate). Negative when type is discount.
    total_tax_amount: int = Field(alias='total_tax_amount')

    # Type of the order line item. The possible values are:<ul><li><em>physical (physical good)</em></li><li><em>discount</em></li><li><em>shipping_fee</em></li><li><em>sales_tax (depends on the country/city, usually called VAT)</em></li><li><em>digital (digital good)</em></li><li><em>gift_card</em></li><li><em>store_credit (credit from the merchant)</em></li><li><em>surcharge (extra charge)</em></li></ul>
    type: typing.Optional[str] = Field(None, alias='type')

    # Article number, SKU or similar. (max 255 characters)
    reference: typing.Optional[str] = Field(None, alias='reference')

    subscription: typing.Optional[Subscription] = Field(None, alias='subscription')

    # Unit used to describe the quantity, e.g. kg, pcs... If defined has to be 1-8 characters
    quantity_unit: typing.Optional[str] = Field(None, alias='quantity_unit')

    # Non-negative minor units. Includes tax.  Example: 25 euros should be 2500
    total_discount_amount: typing.Optional[int] = Field(None, alias='total_discount_amount')

    # Property used to store additional metadata per item that will be returned whenever an order is read from Klarna. Pass through field. (max 1024 characters).
    merchant_data: typing.Optional[str] = Field(None, alias='merchant_data')

    # URL to the product page that can be later embedded in communications between Klarna and the customer. (max 1024 characters)
    product_url: typing.Optional[str] = Field(None, alias='product_url')

    # URL to an image that can be later embedded in communications between Klarna and the customer. (max 1024 characters)  Improves post-purchase customer experiences.
    image_url: typing.Optional[str] = Field(None, alias='image_url')

    product_identifiers: typing.Optional[ProductIdentifiers] = Field(None, alias='product_identifiers')

    shipping_attributes: typing.Optional[ShippingAttributes] = Field(None, alias='shipping_attributes')
    class Config:
        arbitrary_types_allowed = True
