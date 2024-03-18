import typing_extensions

from klarna_checkout_python_sdk.apis.tags import TagValues
from klarna_checkout_python_sdk.apis.tags.order_api import OrderApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ORDER: OrderApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ORDER: OrderApi,
    }
)
