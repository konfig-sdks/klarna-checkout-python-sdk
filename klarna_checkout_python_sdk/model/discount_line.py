# coding: utf-8

"""
    Klarna Checkout API V3

    The checkout API is used to create a checkout with Klarna and update the checkout order during the purchase. As soon as the purchase is completed the order should be read and handled using the [`Order Management API`](https://docs.klarna.com/api/ordermanagement).\\n\\nRead more on [Klarna checkout](https://docs.klarna.com/klarna-checkout/).

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from klarna_checkout_python_sdk import schemas  # noqa: F401


class DiscountLine(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "quantity",
            "total_amount",
            "name",
            "total_tax_amount",
            "unit_price",
            "tax_rate",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
                    min_length = 1
            
            
            class quantity(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_minimum = 0
            
            
            class unit_price(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_maximum = 0
            
            
            class tax_rate(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_maximum = 10000
            
            
            class total_amount(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_maximum = 0
            total_tax_amount = schemas.Int64Schema
            
            
            class reference(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
                    min_length = 0
            
            
            class merchant_data(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 1024
                    min_length = 0
            __annotations__ = {
                "name": name,
                "quantity": quantity,
                "unit_price": unit_price,
                "tax_rate": tax_rate,
                "total_amount": total_amount,
                "total_tax_amount": total_tax_amount,
                "reference": reference,
                "merchant_data": merchant_data,
            }
    
    quantity: MetaOapg.properties.quantity
    total_amount: MetaOapg.properties.total_amount
    name: MetaOapg.properties.name
    total_tax_amount: MetaOapg.properties.total_tax_amount
    unit_price: MetaOapg.properties.unit_price
    tax_rate: MetaOapg.properties.tax_rate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit_price"]) -> MetaOapg.properties.unit_price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_rate"]) -> MetaOapg.properties.tax_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_amount"]) -> MetaOapg.properties.total_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_tax_amount"]) -> MetaOapg.properties.total_tax_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_data"]) -> MetaOapg.properties.merchant_data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "quantity", "unit_price", "tax_rate", "total_amount", "total_tax_amount", "reference", "merchant_data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit_price"]) -> MetaOapg.properties.unit_price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_rate"]) -> MetaOapg.properties.tax_rate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_amount"]) -> MetaOapg.properties.total_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_tax_amount"]) -> MetaOapg.properties.total_tax_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_data"]) -> typing.Union[MetaOapg.properties.merchant_data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "quantity", "unit_price", "tax_rate", "total_amount", "total_tax_amount", "reference", "merchant_data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, ],
        total_amount: typing.Union[MetaOapg.properties.total_amount, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        total_tax_amount: typing.Union[MetaOapg.properties.total_tax_amount, decimal.Decimal, int, ],
        unit_price: typing.Union[MetaOapg.properties.unit_price, decimal.Decimal, int, ],
        tax_rate: typing.Union[MetaOapg.properties.tax_rate, decimal.Decimal, int, ],
        reference: typing.Union[MetaOapg.properties.reference, str, schemas.Unset] = schemas.unset,
        merchant_data: typing.Union[MetaOapg.properties.merchant_data, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DiscountLine':
        return super().__new__(
            cls,
            *args,
            quantity=quantity,
            total_amount=total_amount,
            name=name,
            total_tax_amount=total_tax_amount,
            unit_price=unit_price,
            tax_rate=tax_rate,
            reference=reference,
            merchant_data=merchant_data,
            _configuration=_configuration,
            **kwargs,
        )
