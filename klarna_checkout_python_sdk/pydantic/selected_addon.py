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


class SelectedAddon(BaseModel):
    type: typing.Optional[str] = Field(None, alias='type')

    price: typing.Optional[int] = Field(None, alias='price')

    external_id: typing.Optional[str] = Field(None, alias='external_id')

    user_input: typing.Optional[str] = Field(None, alias='user_input')
    class Config:
        arbitrary_types_allowed = True
