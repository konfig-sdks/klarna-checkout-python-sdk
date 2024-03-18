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


class Subscription(BaseModel):
    # The cadence unit for this.  Example: \"DAY\"
    interval: Literal["DAY", "WEEK", "MONTH", "YEAR"] = Field(alias='interval')

    # The number of intervals.  Example: 30
    interval_count: int = Field(alias='interval_count')

    # The name of the subscription product.  Example: \"Premium Account\"
    name: typing.Optional[str] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True