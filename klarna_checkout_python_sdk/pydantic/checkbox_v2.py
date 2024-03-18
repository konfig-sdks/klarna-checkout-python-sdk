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


class CheckboxV2(BaseModel):
    # Text that will be displayed to the consumer aside the checkbox. Links and formatting can be added using Markdown. (max 1000 characters)
    text: str = Field(alias='text')

    # Default state of the additional checkbox. It will use this value when loaded for the first time.
    checked: bool = Field(alias='checked')

    # Whether it is required for the consumer to check the additional checkbox box or not in order to complete the purchase.
    required: bool = Field(alias='required')

    # Identifier used when presenting data back to merchant
    id: str = Field(alias='id')
    class Config:
        arbitrary_types_allowed = True
