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


class PaymentProvider(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "redirect_url",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class redirect_url(
                schemas.StrSchema
            ):
                pass
            
            
            class description(
                schemas.StrSchema
            ):
                pass
            fee = schemas.Int64Schema
        
            @staticmethod
            def countries() -> typing.Type['PaymentProviderCountries']:
                return PaymentProviderCountries
            label = schemas.StrSchema
            
            
            class image_url(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "name": name,
                "redirect_url": redirect_url,
                "description": description,
                "fee": fee,
                "countries": countries,
                "label": label,
                "image_url": image_url,
            }
    
    name: MetaOapg.properties.name
    redirect_url: MetaOapg.properties.redirect_url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> MetaOapg.properties.redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fee"]) -> MetaOapg.properties.fee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countries"]) -> 'PaymentProviderCountries': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_url"]) -> MetaOapg.properties.image_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "redirect_url", "description", "fee", "countries", "label", "image_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> MetaOapg.properties.redirect_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fee"]) -> typing.Union[MetaOapg.properties.fee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countries"]) -> typing.Union['PaymentProviderCountries', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_url"]) -> typing.Union[MetaOapg.properties.image_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "redirect_url", "description", "fee", "countries", "label", "image_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        redirect_url: typing.Union[MetaOapg.properties.redirect_url, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        fee: typing.Union[MetaOapg.properties.fee, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        countries: typing.Union['PaymentProviderCountries', schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        image_url: typing.Union[MetaOapg.properties.image_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentProvider':
        return super().__new__(
            cls,
            *args,
            name=name,
            redirect_url=redirect_url,
            description=description,
            fee=fee,
            countries=countries,
            label=label,
            image_url=image_url,
            _configuration=_configuration,
            **kwargs,
        )

from klarna_checkout_python_sdk.model.payment_provider_countries import PaymentProviderCountries
