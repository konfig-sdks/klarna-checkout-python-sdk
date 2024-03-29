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


class Order(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "order_tax_amount",
            "order_amount",
            "purchase_country",
            "order_lines",
            "purchase_currency",
            "locale",
        }
        
        class properties:
            
            
            class purchase_country(
                schemas.StrSchema
            ):
                pass
            
            
            class purchase_currency(
                schemas.StrSchema
            ):
                pass
            
            
            class locale(
                schemas.StrSchema
            ):
                pass
            
            
            class order_amount(
                schemas.Int64Schema
            ):
                pass
            
            
            class order_tax_amount(
                schemas.Int64Schema
            ):
                pass
            
            
            class order_lines(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OrderLine']:
                        return OrderLine
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['OrderLine'], typing.List['OrderLine']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'order_lines':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OrderLine':
                    return super().__getitem__(i)
        
            @staticmethod
            def tags() -> typing.Type['OrderTags']:
                return OrderTags
            order_id = schemas.StrSchema
            name = schemas.StrSchema
            status = schemas.StrSchema
        
            @staticmethod
            def billing_address() -> typing.Type['Address']:
                return Address
        
            @staticmethod
            def shipping_address() -> typing.Type['Address']:
                return Address
        
            @staticmethod
            def customer() -> typing.Type['Customer']:
                return Customer
        
            @staticmethod
            def merchant_urls() -> typing.Type['MerchantUrls']:
                return MerchantUrls
            html_snippet = schemas.StrSchema
            
            
            class merchant_reference1(
                schemas.StrSchema
            ):
                pass
            
            
            class merchant_reference2(
                schemas.StrSchema
            ):
                pass
            started_at = schemas.DateTimeSchema
            completed_at = schemas.DateTimeSchema
            last_modified_at = schemas.DateTimeSchema
        
            @staticmethod
            def options() -> typing.Type['Options']:
                return Options
        
            @staticmethod
            def attachment() -> typing.Type['Attachment']:
                return Attachment
            
            
            class external_payment_methods(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PaymentProvider']:
                        return PaymentProvider
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PaymentProvider'], typing.List['PaymentProvider']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'external_payment_methods':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PaymentProvider':
                    return super().__getitem__(i)
            
            
            class external_checkouts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PaymentProvider']:
                        return PaymentProvider
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PaymentProvider'], typing.List['PaymentProvider']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'external_checkouts':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PaymentProvider':
                    return super().__getitem__(i)
        
            @staticmethod
            def shipping_countries() -> typing.Type['OrderShippingCountries']:
                return OrderShippingCountries
            
            
            class shipping_options(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ShippingOption']:
                        return ShippingOption
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ShippingOption'], typing.List['ShippingOption']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'shipping_options':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ShippingOption':
                    return super().__getitem__(i)
            
            
            class merchant_data(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def gui() -> typing.Type['Gui']:
                return Gui
        
            @staticmethod
            def merchant_requested() -> typing.Type['MerchantRequested']:
                return MerchantRequested
        
            @staticmethod
            def selected_shipping_option() -> typing.Type['ShippingOption']:
                return ShippingOption
            recurring = schemas.BoolSchema
            recurring_token = schemas.StrSchema
            
            
            class recurring_description(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def billing_countries() -> typing.Type['OrderBillingCountries']:
                return OrderBillingCountries
            
            
            class discount_lines(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DiscountLine']:
                        return DiscountLine
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DiscountLine'], typing.List['DiscountLine']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'discount_lines':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DiscountLine':
                    return super().__getitem__(i)
            __annotations__ = {
                "purchase_country": purchase_country,
                "purchase_currency": purchase_currency,
                "locale": locale,
                "order_amount": order_amount,
                "order_tax_amount": order_tax_amount,
                "order_lines": order_lines,
                "tags": tags,
                "order_id": order_id,
                "name": name,
                "status": status,
                "billing_address": billing_address,
                "shipping_address": shipping_address,
                "customer": customer,
                "merchant_urls": merchant_urls,
                "html_snippet": html_snippet,
                "merchant_reference1": merchant_reference1,
                "merchant_reference2": merchant_reference2,
                "started_at": started_at,
                "completed_at": completed_at,
                "last_modified_at": last_modified_at,
                "options": options,
                "attachment": attachment,
                "external_payment_methods": external_payment_methods,
                "external_checkouts": external_checkouts,
                "shipping_countries": shipping_countries,
                "shipping_options": shipping_options,
                "merchant_data": merchant_data,
                "gui": gui,
                "merchant_requested": merchant_requested,
                "selected_shipping_option": selected_shipping_option,
                "recurring": recurring,
                "recurring_token": recurring_token,
                "recurring_description": recurring_description,
                "billing_countries": billing_countries,
                "discount_lines": discount_lines,
            }
    
    order_tax_amount: MetaOapg.properties.order_tax_amount
    order_amount: MetaOapg.properties.order_amount
    purchase_country: MetaOapg.properties.purchase_country
    order_lines: MetaOapg.properties.order_lines
    purchase_currency: MetaOapg.properties.purchase_currency
    locale: MetaOapg.properties.locale
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchase_country"]) -> MetaOapg.properties.purchase_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchase_currency"]) -> MetaOapg.properties.purchase_currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_amount"]) -> MetaOapg.properties.order_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_tax_amount"]) -> MetaOapg.properties.order_tax_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_lines"]) -> MetaOapg.properties.order_lines: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'OrderTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_id"]) -> MetaOapg.properties.order_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing_address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer"]) -> 'Customer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_urls"]) -> 'MerchantUrls': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html_snippet"]) -> MetaOapg.properties.html_snippet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_reference1"]) -> MetaOapg.properties.merchant_reference1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_reference2"]) -> MetaOapg.properties.merchant_reference2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["started_at"]) -> MetaOapg.properties.started_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completed_at"]) -> MetaOapg.properties.completed_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_modified_at"]) -> MetaOapg.properties.last_modified_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'Options': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachment"]) -> 'Attachment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_payment_methods"]) -> MetaOapg.properties.external_payment_methods: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_checkouts"]) -> MetaOapg.properties.external_checkouts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_countries"]) -> 'OrderShippingCountries': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_options"]) -> MetaOapg.properties.shipping_options: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_data"]) -> MetaOapg.properties.merchant_data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gui"]) -> 'Gui': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant_requested"]) -> 'MerchantRequested': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selected_shipping_option"]) -> 'ShippingOption': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurring"]) -> MetaOapg.properties.recurring: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurring_token"]) -> MetaOapg.properties.recurring_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurring_description"]) -> MetaOapg.properties.recurring_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing_countries"]) -> 'OrderBillingCountries': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discount_lines"]) -> MetaOapg.properties.discount_lines: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["purchase_country", "purchase_currency", "locale", "order_amount", "order_tax_amount", "order_lines", "tags", "order_id", "name", "status", "billing_address", "shipping_address", "customer", "merchant_urls", "html_snippet", "merchant_reference1", "merchant_reference2", "started_at", "completed_at", "last_modified_at", "options", "attachment", "external_payment_methods", "external_checkouts", "shipping_countries", "shipping_options", "merchant_data", "gui", "merchant_requested", "selected_shipping_option", "recurring", "recurring_token", "recurring_description", "billing_countries", "discount_lines", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchase_country"]) -> MetaOapg.properties.purchase_country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchase_currency"]) -> MetaOapg.properties.purchase_currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_amount"]) -> MetaOapg.properties.order_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_tax_amount"]) -> MetaOapg.properties.order_tax_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_lines"]) -> MetaOapg.properties.order_lines: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['OrderTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_id"]) -> typing.Union[MetaOapg.properties.order_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing_address"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_address"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer"]) -> typing.Union['Customer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_urls"]) -> typing.Union['MerchantUrls', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html_snippet"]) -> typing.Union[MetaOapg.properties.html_snippet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_reference1"]) -> typing.Union[MetaOapg.properties.merchant_reference1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_reference2"]) -> typing.Union[MetaOapg.properties.merchant_reference2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["started_at"]) -> typing.Union[MetaOapg.properties.started_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completed_at"]) -> typing.Union[MetaOapg.properties.completed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_modified_at"]) -> typing.Union[MetaOapg.properties.last_modified_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union['Options', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachment"]) -> typing.Union['Attachment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_payment_methods"]) -> typing.Union[MetaOapg.properties.external_payment_methods, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_checkouts"]) -> typing.Union[MetaOapg.properties.external_checkouts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_countries"]) -> typing.Union['OrderShippingCountries', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_options"]) -> typing.Union[MetaOapg.properties.shipping_options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_data"]) -> typing.Union[MetaOapg.properties.merchant_data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gui"]) -> typing.Union['Gui', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant_requested"]) -> typing.Union['MerchantRequested', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selected_shipping_option"]) -> typing.Union['ShippingOption', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurring"]) -> typing.Union[MetaOapg.properties.recurring, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurring_token"]) -> typing.Union[MetaOapg.properties.recurring_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurring_description"]) -> typing.Union[MetaOapg.properties.recurring_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing_countries"]) -> typing.Union['OrderBillingCountries', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discount_lines"]) -> typing.Union[MetaOapg.properties.discount_lines, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["purchase_country", "purchase_currency", "locale", "order_amount", "order_tax_amount", "order_lines", "tags", "order_id", "name", "status", "billing_address", "shipping_address", "customer", "merchant_urls", "html_snippet", "merchant_reference1", "merchant_reference2", "started_at", "completed_at", "last_modified_at", "options", "attachment", "external_payment_methods", "external_checkouts", "shipping_countries", "shipping_options", "merchant_data", "gui", "merchant_requested", "selected_shipping_option", "recurring", "recurring_token", "recurring_description", "billing_countries", "discount_lines", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        order_tax_amount: typing.Union[MetaOapg.properties.order_tax_amount, decimal.Decimal, int, ],
        order_amount: typing.Union[MetaOapg.properties.order_amount, decimal.Decimal, int, ],
        purchase_country: typing.Union[MetaOapg.properties.purchase_country, str, ],
        order_lines: typing.Union[MetaOapg.properties.order_lines, list, tuple, ],
        purchase_currency: typing.Union[MetaOapg.properties.purchase_currency, str, ],
        locale: typing.Union[MetaOapg.properties.locale, str, ],
        tags: typing.Union['OrderTags', schemas.Unset] = schemas.unset,
        order_id: typing.Union[MetaOapg.properties.order_id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        billing_address: typing.Union['Address', schemas.Unset] = schemas.unset,
        shipping_address: typing.Union['Address', schemas.Unset] = schemas.unset,
        customer: typing.Union['Customer', schemas.Unset] = schemas.unset,
        merchant_urls: typing.Union['MerchantUrls', schemas.Unset] = schemas.unset,
        html_snippet: typing.Union[MetaOapg.properties.html_snippet, str, schemas.Unset] = schemas.unset,
        merchant_reference1: typing.Union[MetaOapg.properties.merchant_reference1, str, schemas.Unset] = schemas.unset,
        merchant_reference2: typing.Union[MetaOapg.properties.merchant_reference2, str, schemas.Unset] = schemas.unset,
        started_at: typing.Union[MetaOapg.properties.started_at, str, datetime, schemas.Unset] = schemas.unset,
        completed_at: typing.Union[MetaOapg.properties.completed_at, str, datetime, schemas.Unset] = schemas.unset,
        last_modified_at: typing.Union[MetaOapg.properties.last_modified_at, str, datetime, schemas.Unset] = schemas.unset,
        options: typing.Union['Options', schemas.Unset] = schemas.unset,
        attachment: typing.Union['Attachment', schemas.Unset] = schemas.unset,
        external_payment_methods: typing.Union[MetaOapg.properties.external_payment_methods, list, tuple, schemas.Unset] = schemas.unset,
        external_checkouts: typing.Union[MetaOapg.properties.external_checkouts, list, tuple, schemas.Unset] = schemas.unset,
        shipping_countries: typing.Union['OrderShippingCountries', schemas.Unset] = schemas.unset,
        shipping_options: typing.Union[MetaOapg.properties.shipping_options, list, tuple, schemas.Unset] = schemas.unset,
        merchant_data: typing.Union[MetaOapg.properties.merchant_data, str, schemas.Unset] = schemas.unset,
        gui: typing.Union['Gui', schemas.Unset] = schemas.unset,
        merchant_requested: typing.Union['MerchantRequested', schemas.Unset] = schemas.unset,
        selected_shipping_option: typing.Union['ShippingOption', schemas.Unset] = schemas.unset,
        recurring: typing.Union[MetaOapg.properties.recurring, bool, schemas.Unset] = schemas.unset,
        recurring_token: typing.Union[MetaOapg.properties.recurring_token, str, schemas.Unset] = schemas.unset,
        recurring_description: typing.Union[MetaOapg.properties.recurring_description, str, schemas.Unset] = schemas.unset,
        billing_countries: typing.Union['OrderBillingCountries', schemas.Unset] = schemas.unset,
        discount_lines: typing.Union[MetaOapg.properties.discount_lines, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Order':
        return super().__new__(
            cls,
            *args,
            order_tax_amount=order_tax_amount,
            order_amount=order_amount,
            purchase_country=purchase_country,
            order_lines=order_lines,
            purchase_currency=purchase_currency,
            locale=locale,
            tags=tags,
            order_id=order_id,
            name=name,
            status=status,
            billing_address=billing_address,
            shipping_address=shipping_address,
            customer=customer,
            merchant_urls=merchant_urls,
            html_snippet=html_snippet,
            merchant_reference1=merchant_reference1,
            merchant_reference2=merchant_reference2,
            started_at=started_at,
            completed_at=completed_at,
            last_modified_at=last_modified_at,
            options=options,
            attachment=attachment,
            external_payment_methods=external_payment_methods,
            external_checkouts=external_checkouts,
            shipping_countries=shipping_countries,
            shipping_options=shipping_options,
            merchant_data=merchant_data,
            gui=gui,
            merchant_requested=merchant_requested,
            selected_shipping_option=selected_shipping_option,
            recurring=recurring,
            recurring_token=recurring_token,
            recurring_description=recurring_description,
            billing_countries=billing_countries,
            discount_lines=discount_lines,
            _configuration=_configuration,
            **kwargs,
        )

from klarna_checkout_python_sdk.model.address import Address
from klarna_checkout_python_sdk.model.attachment import Attachment
from klarna_checkout_python_sdk.model.customer import Customer
from klarna_checkout_python_sdk.model.discount_line import DiscountLine
from klarna_checkout_python_sdk.model.gui import Gui
from klarna_checkout_python_sdk.model.merchant_requested import MerchantRequested
from klarna_checkout_python_sdk.model.merchant_urls import MerchantUrls
from klarna_checkout_python_sdk.model.options import Options
from klarna_checkout_python_sdk.model.order_billing_countries import OrderBillingCountries
from klarna_checkout_python_sdk.model.order_line import OrderLine
from klarna_checkout_python_sdk.model.order_shipping_countries import OrderShippingCountries
from klarna_checkout_python_sdk.model.order_tags import OrderTags
from klarna_checkout_python_sdk.model.payment_provider import PaymentProvider
from klarna_checkout_python_sdk.model.shipping_option import ShippingOption
