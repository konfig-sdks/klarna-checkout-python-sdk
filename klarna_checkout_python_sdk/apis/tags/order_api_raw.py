# coding: utf-8

"""
    Klarna Checkout API V3

    The checkout API is used to create a checkout with Klarna and update the checkout order during the purchase. As soon as the purchase is completed the order should be read and handled using the [`Order Management API`](https://docs.klarna.com/api/ordermanagement).\\n\\nRead more on [Klarna checkout](https://docs.klarna.com/klarna-checkout/).

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from klarna_checkout_python_sdk.paths.checkout_v3_orders_order_id_abort.post import AbortOrderRaw
from klarna_checkout_python_sdk.paths.checkout_v3_orders.post import CreateNewOrderRaw
from klarna_checkout_python_sdk.paths.checkout_v3_orders_order_id.get import GetOrderDetailsRaw
from klarna_checkout_python_sdk.paths.checkout_v3_orders_order_id.post import UpdateOrderRaw


class OrderApiRaw(
    AbortOrderRaw,
    CreateNewOrderRaw,
    GetOrderDetailsRaw,
    UpdateOrderRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
