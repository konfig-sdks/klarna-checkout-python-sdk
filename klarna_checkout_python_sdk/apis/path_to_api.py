import typing_extensions

from klarna_checkout_python_sdk.paths import PathValues
from klarna_checkout_python_sdk.apis.paths.checkout_v3_orders import CheckoutV3Orders
from klarna_checkout_python_sdk.apis.paths.checkout_v3_orders_order_id import CheckoutV3OrdersOrderId
from klarna_checkout_python_sdk.apis.paths.checkout_v3_orders_order_id_abort import CheckoutV3OrdersOrderIdAbort

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CHECKOUT_V3_ORDERS: CheckoutV3Orders,
        PathValues.CHECKOUT_V3_ORDERS_ORDER_ID: CheckoutV3OrdersOrderId,
        PathValues.CHECKOUT_V3_ORDERS_ORDER_ID_ABORT: CheckoutV3OrdersOrderIdAbort,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CHECKOUT_V3_ORDERS: CheckoutV3Orders,
        PathValues.CHECKOUT_V3_ORDERS_ORDER_ID: CheckoutV3OrdersOrderId,
        PathValues.CHECKOUT_V3_ORDERS_ORDER_ID_ABORT: CheckoutV3OrdersOrderIdAbort,
    }
)
