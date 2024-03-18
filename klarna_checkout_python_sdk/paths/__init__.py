# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from klarna_checkout_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CHECKOUT_V3_ORDERS = "/checkout/v3/orders"
    CHECKOUT_V3_ORDERS_ORDER_ID = "/checkout/v3/orders/{order_id}"
    CHECKOUT_V3_ORDERS_ORDER_ID_ABORT = "/checkout/v3/orders/{order_id}/abort"
