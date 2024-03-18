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


class MerchantRequested(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            additional_checkbox = schemas.BoolSchema
            
            
            class additional_checkboxes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MerchantRequestedCheckbox']:
                        return MerchantRequestedCheckbox
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MerchantRequestedCheckbox'], typing.List['MerchantRequestedCheckbox']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'additional_checkboxes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MerchantRequestedCheckbox':
                    return super().__getitem__(i)
            __annotations__ = {
                "additional_checkbox": additional_checkbox,
                "additional_checkboxes": additional_checkboxes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_checkbox"]) -> MetaOapg.properties.additional_checkbox: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_checkboxes"]) -> MetaOapg.properties.additional_checkboxes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["additional_checkbox", "additional_checkboxes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_checkbox"]) -> typing.Union[MetaOapg.properties.additional_checkbox, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_checkboxes"]) -> typing.Union[MetaOapg.properties.additional_checkboxes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["additional_checkbox", "additional_checkboxes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        additional_checkbox: typing.Union[MetaOapg.properties.additional_checkbox, bool, schemas.Unset] = schemas.unset,
        additional_checkboxes: typing.Union[MetaOapg.properties.additional_checkboxes, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MerchantRequested':
        return super().__new__(
            cls,
            *args,
            additional_checkbox=additional_checkbox,
            additional_checkboxes=additional_checkboxes,
            _configuration=_configuration,
            **kwargs,
        )

from klarna_checkout_python_sdk.model.merchant_requested_checkbox import MerchantRequestedCheckbox