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

from klarna_checkout_python_sdk.pydantic.checkbox import Checkbox
from klarna_checkout_python_sdk.pydantic.checkbox_v2 import CheckboxV2
from klarna_checkout_python_sdk.pydantic.options_allowed_customer_types import OptionsAllowedCustomerTypes

class Options(BaseModel):
    # If true, validate callback must get a positive response to not stop purchase. Default: false.
    require_validate_callback_success: typing.Optional[bool] = Field(None, alias='require_validate_callback_success')

    # Acquiring channel for the order. The possible values are: <ul><li><em>ECOMMERCE for \"E-commerce\"</em></li><li><em>IN_STORE for \"Purchase in boutique\"</em></li><li><em>Default : ECOMMERCE</em></li></ul>
    acquiring_channel: typing.Optional[str] = Field(None, alias='acquiring_channel')

    # If true, VAT is not displayed in Checkout's Order Summary page.
    vat_removed: typing.Optional[bool] = Field(None, alias='vat_removed')

    # If true, the consumer can enter different billing and shipping addresses. Default: false, except for purchase_country DE where default is: true
    allow_separate_shipping_address: typing.Optional[bool] = Field(None, alias='allow_separate_shipping_address')

    # Color for the buttons within the iFrame. Value should be a CSS hex color, e.g. \"#FF9900\"
    color_button: typing.Optional[str] = Field(None, alias='color_button')

    # Color for the text inside the buttons within the iFrame. Value should be a CSS hex color, e.g. \"#FF9900\"
    color_button_text: typing.Optional[str] = Field(None, alias='color_button_text')

    # Color for the checkboxes within the iFrame. Value should be a CSS hex color, e.g. \"#FF9900\"
    color_checkbox: typing.Optional[str] = Field(None, alias='color_checkbox')

    # Color for the checkboxes checkmark within the iFrame. Value should be a CSS hex color, e.g. \"#FF9900\"
    color_checkbox_checkmark: typing.Optional[str] = Field(None, alias='color_checkbox_checkmark')

    # Color for the headers within the iFrame. Value should be a CSS hex color, e.g. \"#FF9900\"
    color_header: typing.Optional[str] = Field(None, alias='color_header')

    # Color for the hyperlinks within the iFrame. Value should be a CSS hex color, e.g. \"#FF9900\"
    color_link: typing.Optional[str] = Field(None, alias='color_link')

    # If true, the consumer cannot skip date of birth. Default: false
    date_of_birth_mandatory: typing.Optional[bool] = Field(None, alias='date_of_birth_mandatory')

    # A message that will be presented on the confirmation page under the headline \"Delivery\" (max 255 characters).
    shipping_details: typing.Optional[str] = Field(None, alias='shipping_details')

    # If specified to false, title becomes optional. Only available for orders for country GB.
    title_mandatory: typing.Optional[bool] = Field(None, alias='title_mandatory')

    additional_checkbox: typing.Optional[Checkbox] = Field(None, alias='additional_checkbox')

    # If true, the user cannot skip national identification number in SE, NO, FI and DK. Default: false. In order to read the national identification number in the validation callback, please contact Klarna’s merchant support.
    national_identification_number_mandatory: typing.Optional[bool] = Field(None, alias='national_identification_number_mandatory')

    # Additional merchant defined field. e.g. Extra terms and conditions to show.  Example: \"ADDITIONAL MERCHANT TERMS! \\[terms link\\](https://merchant.com/extra_terms)\"
    additional_merchant_terms: typing.Optional[str] = Field(None, alias='additional_merchant_terms')

    # If false, the consumer can skip the phone. Only available for orders in DACH countries.
    phone_mandatory: typing.Optional[bool] = Field(None, alias='phone_mandatory')

    # Radius for the border of elements within the iFrame.
    radius_border: typing.Optional[str] = Field(None, alias='radius_border')

    allowed_customer_types: typing.Optional[OptionsAllowedCustomerTypes] = Field(None, alias='allowed_customer_types')

    # If true, the Order Detail subtotals view is expanded when the Klarna Checkout iFrame is loaded. Default: false
    show_subtotal_detail: typing.Optional[bool] = Field(None, alias='show_subtotal_detail')

    additional_checkboxes: typing.Optional[typing.List[CheckboxV2]] = Field(None, alias='additional_checkboxes')

    # Enable verification of National Identification Numbers only in Sweden, Finland and Norway. This option also make the national identification number mandatory. (Not applicable for countries outside of Sweden, Finland and Norway)
    verify_national_identification_number: typing.Optional[bool] = Field(None, alias='verify_national_identification_number')

    # Allow merchant to trigger auto capturing.
    auto_capture: typing.Optional[bool] = Field(None, alias='auto_capture')

    # If true, a client side validation is needed to complete the purchase
    require_client_validation: typing.Optional[bool] = Field(None, alias='require_client_validation')

    # Enables the inline discount module
    enable_discount_module: typing.Optional[bool] = Field(None, alias='enable_discount_module')

    # If true, a optional VAT registration number field will be shown in the address form. Only applies for b2b orders.
    show_vat_registration_number_field: typing.Optional[bool] = Field(None, alias='show_vat_registration_number_field')
    class Config:
        arbitrary_types_allowed = True