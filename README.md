<div align="left">

[![Visit Klarna](./header.png)](https://klarna.com)

# Klarna<a id="klarna"></a>

The checkout API is used to create a checkout with Klarna and update the checkout order during the purchase. As soon as the purchase is completed the order should be read and handled using the [`Order Management API`](https://docs.klarna.com/api/ordermanagement).\\n\\nRead more on [Klarna checkout](https://docs.klarna.com/klarna-checkout/).


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`klarnacheckout.order.abort_order`](#klarnacheckoutorderabort_order)
  * [`klarnacheckout.order.create_new_order`](#klarnacheckoutordercreate_new_order)
  * [`klarnacheckout.order.get_order_details`](#klarnacheckoutorderget_order_details)
  * [`klarnacheckout.order.update_order`](#klarnacheckoutorderupdate_order)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Klarna&serviceName=Checkout&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from klarna_checkout_python_sdk import KlarnaCheckout, ApiException

klarnacheckout = KlarnaCheckout(
)

try:
    # Abort an order
    abort_order_response = klarnacheckout.order.abort_order(
        order_id="order_id_example",
    )
    print(abort_order_response)
except ApiException as e:
    print("Exception when calling OrderApi.abort_order: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from klarna_checkout_python_sdk import KlarnaCheckout, ApiException

klarnacheckout = KlarnaCheckout(
)

async def main():
    try:
        # Abort an order
        abort_order_response = await klarnacheckout.order.aabort_order(
            order_id="order_id_example",
        )
        print(abort_order_response)
    except ApiException as e:
        print("Exception when calling OrderApi.abort_order: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from klarna_checkout_python_sdk import KlarnaCheckout, ApiException

klarnacheckout = KlarnaCheckout(
)

try:
    # Abort an order
    abort_order_response = klarnacheckout.order.raw.abort_order(
        order_id="order_id_example",
    )
    pprint(abort_order_response.body)
    pprint(abort_order_response.body["purchase_country"])
    pprint(abort_order_response.body["purchase_currency"])
    pprint(abort_order_response.body["locale"])
    pprint(abort_order_response.body["order_amount"])
    pprint(abort_order_response.body["order_tax_amount"])
    pprint(abort_order_response.body["order_lines"])
    pprint(abort_order_response.body["tags"])
    pprint(abort_order_response.body["order_id"])
    pprint(abort_order_response.body["name"])
    pprint(abort_order_response.body["status"])
    pprint(abort_order_response.body["billing_address"])
    pprint(abort_order_response.body["shipping_address"])
    pprint(abort_order_response.body["customer"])
    pprint(abort_order_response.body["merchant_urls"])
    pprint(abort_order_response.body["html_snippet"])
    pprint(abort_order_response.body["merchant_reference1"])
    pprint(abort_order_response.body["merchant_reference2"])
    pprint(abort_order_response.body["started_at"])
    pprint(abort_order_response.body["completed_at"])
    pprint(abort_order_response.body["last_modified_at"])
    pprint(abort_order_response.body["options"])
    pprint(abort_order_response.body["attachment"])
    pprint(abort_order_response.body["external_payment_methods"])
    pprint(abort_order_response.body["external_checkouts"])
    pprint(abort_order_response.body["shipping_countries"])
    pprint(abort_order_response.body["shipping_options"])
    pprint(abort_order_response.body["merchant_data"])
    pprint(abort_order_response.body["gui"])
    pprint(abort_order_response.body["merchant_requested"])
    pprint(abort_order_response.body["selected_shipping_option"])
    pprint(abort_order_response.body["recurring"])
    pprint(abort_order_response.body["recurring_token"])
    pprint(abort_order_response.body["recurring_description"])
    pprint(abort_order_response.body["billing_countries"])
    pprint(abort_order_response.body["discount_lines"])
    pprint(abort_order_response.headers)
    pprint(abort_order_response.status)
    pprint(abort_order_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OrderApi.abort_order: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `klarnacheckout.order.abort_order`<a id="klarnacheckoutorderabort_order"></a>

Mark an order as aborted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
abort_order_response = klarnacheckout.order.abort_order(
    order_id="order_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### order_id: `str`<a id="order_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./klarna_checkout_python_sdk/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checkout/v3/orders/{order_id}/abort` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `klarnacheckout.order.create_new_order`<a id="klarnacheckoutordercreate_new_order"></a>

To create a new order simply provide a JSON object with the applicable properties.<br>The location of the newly created checkout order can be found in the location header of the response.<br>Please note: This is the url that should be used for future interactions (read and update) with the order, i.e. do not construct the order url based on the order id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_order_response = klarnacheckout.order.create_new_order(
    purchase_country="US",
    purchase_currency="USD",
    locale="en-US",
    order_amount=50000,
    order_tax_amount=4545,
    order_lines=[
        {
            "type": "physical",
            "reference": "19-402-USA",
            "name": "Red T-Shirt",
            "quantity": 5,
            "quantity_unit": "pcs",
            "unit_price": 10000,
            "tax_rate": 1000,
            "total_amount": 50000,
            "total_discount_amount": 0,
            "total_tax_amount": 4545,
            "merchant_data": "{\"marketplace_seller_info\":[{\"product_category\":\"Women's Fashion\",\"product_name\":\"Women Sweatshirt\"}]}",
            "product_url": "https://www.example.com/products/f2a8d7e34",
            "image_url": "https://www.exampleobjects.com/product-image-1200x1200.jpg",
        }
    ],
    tags=[
        "string_example"
    ],
    order_id="f3392f8b-6116-4073-ab96-e330819e2c07",
    name="Women's Fashion",
    status="CHECKOUT_INCOMPLETE",
    billing_address={
        "title": "Mr",
        "given_name": "John",
        "family_name": "Doe",
        "email": "john@doe.com",
        "street_address": "Lombard St 10",
        "street_address2": "Apt 214",
        "street_name": "Lombard St",
        "street_number": "10",
        "house_extension": "B",
        "postal_code": "90210",
        "city": "Beverly Hills",
        "region": "CA",
        "phone": "333444555",
        "country": "US",
        "care_of": "C/O",
    },
    shipping_address={
        "title": "Mr",
        "given_name": "John",
        "family_name": "Doe",
        "email": "john@doe.com",
        "street_address": "Lombard St 10",
        "street_address2": "Apt 214",
        "street_name": "Lombard St",
        "street_number": "10",
        "house_extension": "B",
        "postal_code": "90210",
        "city": "Beverly Hills",
        "region": "CA",
        "phone": "333444555",
        "country": "US",
        "care_of": "C/O",
    },
    customer={
        "type": "person",
        "gender": "male",
        "date_of_birth": "1995-10-20",
        "organization_registration_id": "556737-0431",
    },
    merchant_urls={
        "terms": "https://www.example.com/terms.html",
        "checkout": "https://www.example.com/checkout.html",
        "confirmation": "https://www.example.com/confirmation.html",
        "push": "https://www.example.com/api/push",
        "validation": "https://www.example.com/api/validation",
        "notification": "https://www.example.com/api/pending",
        "cancellation_terms": "https://www.example.com/terms/cancellation.html",
        "shipping_option_update": "https://www.example.com/api/shipment",
        "address_update": "https://www.example.com/api/address",
        "country_change": "https://www.example.com/api/country",
    },
    html_snippet="<div id='klarna-checkout-container'><script>alert('Initializing Klarna Checkout');</script></div>",
    merchant_reference1="45aa52f387871e3a210645d4",
    merchant_reference2="45aa52f387871e3a210645d4",
    started_at="1970-01-01T00:00:00.00Z",
    completed_at="1970-01-01T00:00:00.00Z",
    last_modified_at="1970-01-01T00:00:00.00Z",
    options={
        "color_button": "#FF9900",
        "color_button_text": "#FF9900",
        "color_checkbox": "#FF9900",
        "color_checkbox_checkmark": "#FF9900",
        "color_header": "#FF9900",
        "color_link": "#FF9900",
        "shipping_details": "Delivered within 1-3 working days",
        "radius_border": "5",
    },
    attachment={
        "body": "{\"hotel_reservation_details\": [{\"pnr\": \"VH67899\",\"hotel_intinerary\": [{\"hotel_name\": \"Hotel ltd.\",\"address\": {\"street_address\": \"Storgatan 3\",\"postal_code\": \"113 35\",\"city\": \"Stockholm\",\"country\": \"Sweden\"},\"start_time\": \"2019-01-31T15:00:00Z\",\"end_time\": \"2019-01-31T15:30:00Z\",\"number_of_rooms\": 2,\"ticket_delivery_method\": \"email\",\"ticket_delivery_recipient\": \"jonas.larlsson@klarna.com\",\"hotel_price\": 23050,\"class\": \"Business\",\"passenger_id\": [1]}],\"passengers\": [{\"id\": 1,\"title\": \"mr\",\"first_name\": \"Adam\",\"last_name\": \"Adamson\"}],\"insurance\": [{\"insurance_company\": \"Insurance Company X\",\"insurance_type\": \"travel\",\"insurance_price\": 0}],\"affiliate_name\": \"TradeMaxi AB\"}],\"air_reservation_details\": [{\"pnr\": \"VH67899\",\"intinerary\": [{\"departure\": \"ARN\",\"departure_city\": \"Stockholm\",\"arrival\": \"NCE\",\"arrival_city\": \"Nice\",\"carrier\": \"SK\",\"segment_price\": 34000,\"departure_date\": \"2019-01-30T15:00:00Z\",\"ticket_delivery_method\": \"email\",\"ticket_delivery_recipient\": \"jonas.larlsson@klarna.com\",\"passenger_id\": [1]}],\"passengers\": [{\"id\": 1,\"title\": \"mr\",\"first_name\": \"Adam\",\"last_name\": \"Adamson\"}],\"insurance\": [{\"insurance_company\": \"Insurance Company X\",\"insurance_type\": \"travel\",\"insurance_price\": 0}],\"affiliate_name\": \"TradeMaxi AB\"}],\"customer_account_info\": [{\"unique_account_identifier\": \"12345\",\"account_registration_date\": \"2016-01-24T15:00:00Z\",\"account_last_modified\": \"2017-01-24T15:00:00Z\"}],\"payment_history_full\": [{\"payment_option\": \"card\",\"number_paid_purchases\": 2,\"total_amount_paid_purchases\": 1234,\"date_of_last_paid_purchase\": \"2018-01-24T15:00:00Z\",\"date_of_first_paid_purchase\": \"2018-01-24T15:00:00Z\"}]}",
        "content_type": "application/vnd.klarna.internal.emd-v2+json",
    },
    external_payment_methods=[
        {
            "description": "an American company operating a worldwide online payments system",
            "name": "PayhereUs",
            "label": "continue",
            "redirect_url": "https://www.example.com/us/start",
            "image_url": "https://www.exampleobjects.com/product-image-1200x1200.jpg",
        }
    ],
    external_checkouts=[
        {
            "description": "an American company operating a worldwide online payments system",
            "name": "PayhereUs",
            "label": "continue",
            "redirect_url": "https://www.example.com/us/start",
            "image_url": "https://www.exampleobjects.com/product-image-1200x1200.jpg",
        }
    ],
    shipping_countries=[
        "string_example"
    ],
    shipping_options=[
        {
            "description": "Delivery by 4:30 pm",
            "id": "express_priority",
            "name": "EXPRESS 1-2 Days",
            "promo": "Christmas Promotion",
            "price": 1,
            "tax_amount": 1,
            "tax_rate": 1,
            "shipping_method": "PickUpStore",
            "tms_reference": "a1b2c3d4-e4f6-g7h8-i9j0-k1l2m3n4o5p6",
        }
    ],
    merchant_data="{\"marketplace_seller_info\":[{\"product_category\":\"Women's Fashion\",\"product_name\":\"Women Sweatshirt\"}]}",
    gui={
    },
    merchant_requested={
    },
    selected_shipping_option={
        "description": "Delivery by 4:30 pm",
        "id": "express_priority",
        "name": "EXPRESS 1-2 Days",
        "promo": "Christmas Promotion",
        "price": 1,
        "tax_amount": 1,
        "tax_rate": 1,
        "shipping_method": "PickUpStore",
        "tms_reference": "a1b2c3d4-e4f6-g7h8-i9j0-k1l2m3n4o5p6",
    },
    recurring=True,
    recurring_token="string_example",
    recurring_description="",
    billing_countries=[
        "string_example"
    ],
    discount_lines=[
        {
            "name": "Super deal",
            "quantity": 5,
            "unit_price": -10000,
            "tax_rate": 1000,
            "total_amount": -2500,
            "total_tax_amount": -123,
            "reference": "645f54bb-dbb7-6e1f-83bd-bc81a2c3a258",
            "merchant_data": "{\"card_number\":\"5551234567890\"}",
        }
    ],
    klarna_partner="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### purchase_country: `str`<a id="purchase_country-str"></a>

The purchase country of the merchant's store. The format to be used is ISO 3166 alpha-2. Eg: GB, SE, DE, US, etc.   Note: purchase country and currency need to match the defined merchant configuration. For global configuration read this https://docs.klarna.com/klarna-checkout/popular-use-cases/selling-to-multiple-countries/

##### purchase_currency: `str`<a id="purchase_currency-str"></a>

The purchase currency of the merchant's store. The format to be used is ISO 4217. Eg: USD, EUR, SEK, GBP, etc.  Note: purchase country and currency need to match the defined merchant configuration. For global configuration read this https://docs.klarna.com/klarna-checkout/popular-use-cases/selling-to-multiple-countries/

##### locale: `str`<a id="locale-str"></a>

Used to define the language and region of the customer. RFC 1766 customer's locale.

##### order_amount: `int`<a id="order_amount-int"></a>

Total amount of the order including tax and any available discounts. The value should be in non-negative minor units.  Example: 25 Euros should be 2500.

##### order_tax_amount: `int`<a id="order_tax_amount-int"></a>

Total tax amount of the order. The value should be in non-negative minor units.  Example: 25 Euros should be 2500.

##### order_lines: List[`OrderLine`]<a id="order_lines-listorderline"></a>

An array containing list of line items that are part of this order. Maximum of 1000 line items could be processed in a single order.

##### tags: [`OrderTags`](./klarna_checkout_python_sdk/type/order_tags.py)<a id="tags-ordertagsklarna_checkout_python_sdktypeorder_tagspy"></a>

##### order_id: `str`<a id="order_id-str"></a>

Unique order ID that will be used for the entire lifecycle of the order. (max 255 characters)

##### name: `str`<a id="name-str"></a>

The merchant name (max 255 characters).

##### status: `str`<a id="status-str"></a>

The current status of the order. The status will be ‘incomplete’ until the customer has been successfully authorized.

##### billing_address: [`Address`](./klarna_checkout_python_sdk/type/address.py)<a id="billing_address-addressklarna_checkout_python_sdktypeaddresspy"></a>


##### shipping_address: [`Address`](./klarna_checkout_python_sdk/type/address.py)<a id="shipping_address-addressklarna_checkout_python_sdktypeaddresspy"></a>


##### customer: [`Customer`](./klarna_checkout_python_sdk/type/customer.py)<a id="customer-customerklarna_checkout_python_sdktypecustomerpy"></a>


##### merchant_urls: [`MerchantUrls`](./klarna_checkout_python_sdk/type/merchant_urls.py)<a id="merchant_urls-merchanturlsklarna_checkout_python_sdktypemerchant_urlspy"></a>


##### html_snippet: `str`<a id="html_snippet-str"></a>

The HTML snippet that is used to render the checkout in an iframe.

##### merchant_reference1: `str`<a id="merchant_reference1-str"></a>

Used for storing merchant's internal order number or other reference. If set, will be shown on the confirmation page as \\\"order number\\\" . The value is also available in the settlement files. (max 255 characters). Example: \\\"45aa52f387871e3a210645d4\\\"

##### merchant_reference2: `str`<a id="merchant_reference2-str"></a>

Used for storing merchant's internal order number or other reference. The value is available in the settlement files. (max 255 characters). Example: \\\"45aa52f387871e3a210645d4\\\"

##### started_at: `datetime`<a id="started_at-datetime"></a>

ISO 8601 datetime. The date and time when the order has been created. The format will be as follows: \\\"yyyy-mm-ddThh:mm:ssZ\\\"

##### completed_at: `datetime`<a id="completed_at-datetime"></a>

ISO 8601 datetime. The date and time when the order has been completed. The format will be as follows: \\\"yyyy-mm-ddThh:mm:ssZ\\\"

##### last_modified_at: `datetime`<a id="last_modified_at-datetime"></a>

ISO 8601 datetime. The date and time when the order was last modified. The format will be as follows: \\\"yyyy-mm-ddThh:mm:ssZ\\\"

##### options: [`Options`](./klarna_checkout_python_sdk/type/options.py)<a id="options-optionsklarna_checkout_python_sdktypeoptionspy"></a>


##### attachment: [`Attachment`](./klarna_checkout_python_sdk/type/attachment.py)<a id="attachment-attachmentklarna_checkout_python_sdktypeattachmentpy"></a>


##### external_payment_methods: List[`PaymentProvider`]<a id="external_payment_methods-listpaymentprovider"></a>

List of external payment methods that will be displayed as part of payment methods in the checkout.

##### external_checkouts: List[`PaymentProvider`]<a id="external_checkouts-listpaymentprovider"></a>

List of external checkouts that will be displayed as part of payment methods in the checkout. The image_url is required, and the image size has to be 276x48px

##### shipping_countries: [`OrderShippingCountries`](./klarna_checkout_python_sdk/type/order_shipping_countries.py)<a id="shipping_countries-ordershippingcountriesklarna_checkout_python_sdktypeorder_shipping_countriespy"></a>

##### shipping_options: List[`ShippingOption`]<a id="shipping_options-listshippingoption"></a>

A list of shipping options available for this order.

##### merchant_data: `str`<a id="merchant_data-str"></a>

Pass through field to send any information about the order to be used later for reference while retrieving the order details (max 6000 characters).

##### gui: [`Gui`](./klarna_checkout_python_sdk/type/gui.py)<a id="gui-guiklarna_checkout_python_sdktypeguipy"></a>


##### merchant_requested: [`MerchantRequested`](./klarna_checkout_python_sdk/type/merchant_requested.py)<a id="merchant_requested-merchantrequestedklarna_checkout_python_sdktypemerchant_requestedpy"></a>


##### selected_shipping_option: [`ShippingOption`](./klarna_checkout_python_sdk/type/shipping_option.py)<a id="selected_shipping_option-shippingoptionklarna_checkout_python_sdktypeshipping_optionpy"></a>


##### recurring: `bool`<a id="recurring-bool"></a>

Indicates whether this purchase will create a token that can be used by the merchant to create recurring purchases. This must be enabled for the merchant to use. Default: false  Depending on specified country, recurring could be used for the following payment methods: Pay Later, Direct Debit, Card.

##### recurring_token: `str`<a id="recurring_token-str"></a>

Token to be used when creating recurring orders.

##### recurring_description: `str`<a id="recurring_description-str"></a>

Description to be added to the recurring order.

##### billing_countries: [`OrderBillingCountries`](./klarna_checkout_python_sdk/type/order_billing_countries.py)<a id="billing_countries-orderbillingcountriesklarna_checkout_python_sdktypeorder_billing_countriespy"></a>

##### discount_lines: List[`DiscountLine`]<a id="discount_lines-listdiscountline"></a>

List of discounts applied to this order via the KCO discount-service

##### klarna_partner: `str`<a id="klarna_partner-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Order`](./klarna_checkout_python_sdk/type/order.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./klarna_checkout_python_sdk/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checkout/v3/orders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `klarnacheckout.order.get_order_details`<a id="klarnacheckoutorderget_order_details"></a>

Get the full details of a Klarna checkout order.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_order_details_response = klarnacheckout.order.get_order_details(
    order_id="order_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### order_id: `str`<a id="order_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./klarna_checkout_python_sdk/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checkout/v3/orders/{order_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `klarnacheckout.order.update_order`<a id="klarnacheckoutorderupdate_order"></a>

To update an order simply provide a JSON object with the properties you want to update. Properties not provided in the request will stay the same.<br>Please note: an order can only be updated when the status is checkout_incomplete

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_order_response = klarnacheckout.order.update_order(
    purchase_country="US",
    purchase_currency="USD",
    locale="en-US",
    order_amount=50000,
    order_tax_amount=4545,
    order_lines=[
        {
            "type": "physical",
            "reference": "19-402-USA",
            "name": "Red T-Shirt",
            "quantity": 5,
            "quantity_unit": "pcs",
            "unit_price": 10000,
            "tax_rate": 1000,
            "total_amount": 50000,
            "total_discount_amount": 0,
            "total_tax_amount": 4545,
            "merchant_data": "{\"marketplace_seller_info\":[{\"product_category\":\"Women's Fashion\",\"product_name\":\"Women Sweatshirt\"}]}",
            "product_url": "https://www.example.com/products/f2a8d7e34",
            "image_url": "https://www.exampleobjects.com/product-image-1200x1200.jpg",
        }
    ],
    order_id="order_id_example",
    tags=[
        "string_example"
    ],
    order_id="f3392f8b-6116-4073-ab96-e330819e2c07",
    name="Women's Fashion",
    status="CHECKOUT_INCOMPLETE",
    billing_address={
        "title": "Mr",
        "given_name": "John",
        "family_name": "Doe",
        "email": "john@doe.com",
        "street_address": "Lombard St 10",
        "street_address2": "Apt 214",
        "street_name": "Lombard St",
        "street_number": "10",
        "house_extension": "B",
        "postal_code": "90210",
        "city": "Beverly Hills",
        "region": "CA",
        "phone": "333444555",
        "country": "US",
        "care_of": "C/O",
    },
    shipping_address={
        "title": "Mr",
        "given_name": "John",
        "family_name": "Doe",
        "email": "john@doe.com",
        "street_address": "Lombard St 10",
        "street_address2": "Apt 214",
        "street_name": "Lombard St",
        "street_number": "10",
        "house_extension": "B",
        "postal_code": "90210",
        "city": "Beverly Hills",
        "region": "CA",
        "phone": "333444555",
        "country": "US",
        "care_of": "C/O",
    },
    customer={
        "type": "person",
        "gender": "male",
        "date_of_birth": "1995-10-20",
        "organization_registration_id": "556737-0431",
    },
    merchant_urls={
        "terms": "https://www.example.com/terms.html",
        "checkout": "https://www.example.com/checkout.html",
        "confirmation": "https://www.example.com/confirmation.html",
        "push": "https://www.example.com/api/push",
        "validation": "https://www.example.com/api/validation",
        "notification": "https://www.example.com/api/pending",
        "cancellation_terms": "https://www.example.com/terms/cancellation.html",
        "shipping_option_update": "https://www.example.com/api/shipment",
        "address_update": "https://www.example.com/api/address",
        "country_change": "https://www.example.com/api/country",
    },
    html_snippet="<div id='klarna-checkout-container'><script>alert('Initializing Klarna Checkout');</script></div>",
    merchant_reference1="45aa52f387871e3a210645d4",
    merchant_reference2="45aa52f387871e3a210645d4",
    started_at="1970-01-01T00:00:00.00Z",
    completed_at="1970-01-01T00:00:00.00Z",
    last_modified_at="1970-01-01T00:00:00.00Z",
    options={
        "color_button": "#FF9900",
        "color_button_text": "#FF9900",
        "color_checkbox": "#FF9900",
        "color_checkbox_checkmark": "#FF9900",
        "color_header": "#FF9900",
        "color_link": "#FF9900",
        "shipping_details": "Delivered within 1-3 working days",
        "radius_border": "5",
    },
    attachment={
        "body": "{\"hotel_reservation_details\": [{\"pnr\": \"VH67899\",\"hotel_intinerary\": [{\"hotel_name\": \"Hotel ltd.\",\"address\": {\"street_address\": \"Storgatan 3\",\"postal_code\": \"113 35\",\"city\": \"Stockholm\",\"country\": \"Sweden\"},\"start_time\": \"2019-01-31T15:00:00Z\",\"end_time\": \"2019-01-31T15:30:00Z\",\"number_of_rooms\": 2,\"ticket_delivery_method\": \"email\",\"ticket_delivery_recipient\": \"jonas.larlsson@klarna.com\",\"hotel_price\": 23050,\"class\": \"Business\",\"passenger_id\": [1]}],\"passengers\": [{\"id\": 1,\"title\": \"mr\",\"first_name\": \"Adam\",\"last_name\": \"Adamson\"}],\"insurance\": [{\"insurance_company\": \"Insurance Company X\",\"insurance_type\": \"travel\",\"insurance_price\": 0}],\"affiliate_name\": \"TradeMaxi AB\"}],\"air_reservation_details\": [{\"pnr\": \"VH67899\",\"intinerary\": [{\"departure\": \"ARN\",\"departure_city\": \"Stockholm\",\"arrival\": \"NCE\",\"arrival_city\": \"Nice\",\"carrier\": \"SK\",\"segment_price\": 34000,\"departure_date\": \"2019-01-30T15:00:00Z\",\"ticket_delivery_method\": \"email\",\"ticket_delivery_recipient\": \"jonas.larlsson@klarna.com\",\"passenger_id\": [1]}],\"passengers\": [{\"id\": 1,\"title\": \"mr\",\"first_name\": \"Adam\",\"last_name\": \"Adamson\"}],\"insurance\": [{\"insurance_company\": \"Insurance Company X\",\"insurance_type\": \"travel\",\"insurance_price\": 0}],\"affiliate_name\": \"TradeMaxi AB\"}],\"customer_account_info\": [{\"unique_account_identifier\": \"12345\",\"account_registration_date\": \"2016-01-24T15:00:00Z\",\"account_last_modified\": \"2017-01-24T15:00:00Z\"}],\"payment_history_full\": [{\"payment_option\": \"card\",\"number_paid_purchases\": 2,\"total_amount_paid_purchases\": 1234,\"date_of_last_paid_purchase\": \"2018-01-24T15:00:00Z\",\"date_of_first_paid_purchase\": \"2018-01-24T15:00:00Z\"}]}",
        "content_type": "application/vnd.klarna.internal.emd-v2+json",
    },
    external_payment_methods=[
        {
            "description": "an American company operating a worldwide online payments system",
            "name": "PayhereUs",
            "label": "continue",
            "redirect_url": "https://www.example.com/us/start",
            "image_url": "https://www.exampleobjects.com/product-image-1200x1200.jpg",
        }
    ],
    external_checkouts=[
        {
            "description": "an American company operating a worldwide online payments system",
            "name": "PayhereUs",
            "label": "continue",
            "redirect_url": "https://www.example.com/us/start",
            "image_url": "https://www.exampleobjects.com/product-image-1200x1200.jpg",
        }
    ],
    shipping_countries=[
        "string_example"
    ],
    shipping_options=[
        {
            "description": "Delivery by 4:30 pm",
            "id": "express_priority",
            "name": "EXPRESS 1-2 Days",
            "promo": "Christmas Promotion",
            "price": 1,
            "tax_amount": 1,
            "tax_rate": 1,
            "shipping_method": "PickUpStore",
            "tms_reference": "a1b2c3d4-e4f6-g7h8-i9j0-k1l2m3n4o5p6",
        }
    ],
    merchant_data="{\"marketplace_seller_info\":[{\"product_category\":\"Women's Fashion\",\"product_name\":\"Women Sweatshirt\"}]}",
    gui={
    },
    merchant_requested={
    },
    selected_shipping_option={
        "description": "Delivery by 4:30 pm",
        "id": "express_priority",
        "name": "EXPRESS 1-2 Days",
        "promo": "Christmas Promotion",
        "price": 1,
        "tax_amount": 1,
        "tax_rate": 1,
        "shipping_method": "PickUpStore",
        "tms_reference": "a1b2c3d4-e4f6-g7h8-i9j0-k1l2m3n4o5p6",
    },
    recurring=True,
    recurring_token="string_example",
    recurring_description="",
    billing_countries=[
        "string_example"
    ],
    discount_lines=[
        {
            "name": "Super deal",
            "quantity": 5,
            "unit_price": -10000,
            "tax_rate": 1000,
            "total_amount": -2500,
            "total_tax_amount": -123,
            "reference": "645f54bb-dbb7-6e1f-83bd-bc81a2c3a258",
            "merchant_data": "{\"card_number\":\"5551234567890\"}",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### order_id: `str`<a id="order_id-str"></a>

##### requestBody: [`Order`](./klarna_checkout_python_sdk/type/order.py)<a id="requestbody-orderklarna_checkout_python_sdktypeorderpy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Order`](./klarna_checkout_python_sdk/pydantic/order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checkout/v3/orders/{order_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
