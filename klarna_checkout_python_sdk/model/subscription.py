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


class Subscription(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "interval_count",
            "interval",
        }
        
        class properties:
            
            
            class interval(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "DAY": "DAY",
                        "WEEK": "WEEK",
                        "MONTH": "MONTH",
                        "YEAR": "YEAR",
                    }
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("DAY")
                
                @schemas.classproperty
                def WEEK(cls):
                    return cls("WEEK")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("MONTH")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("YEAR")
            
            
            class interval_count(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = 1
            name = schemas.StrSchema
            __annotations__ = {
                "interval": interval,
                "interval_count": interval_count,
                "name": name,
            }
    
    interval_count: MetaOapg.properties.interval_count
    interval: MetaOapg.properties.interval
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interval"]) -> MetaOapg.properties.interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interval_count"]) -> MetaOapg.properties.interval_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["interval", "interval_count", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interval"]) -> MetaOapg.properties.interval: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interval_count"]) -> MetaOapg.properties.interval_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["interval", "interval_count", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        interval_count: typing.Union[MetaOapg.properties.interval_count, decimal.Decimal, int, ],
        interval: typing.Union[MetaOapg.properties.interval, str, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Subscription':
        return super().__new__(
            cls,
            *args,
            interval_count=interval_count,
            interval=interval,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )
