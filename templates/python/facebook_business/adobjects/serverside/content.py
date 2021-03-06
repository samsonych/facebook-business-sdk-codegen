# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import pprint

import six


class Content(object):
    """
    Content objects that contain the product IDs associated with the event plus information about the products.
    """
    param_types = {
        'product_id': 'str',
        'quantity': 'str',
        'item_price': 'float'
    }

    def __init__(self, product_id: str = None, quantity: str = None, item_price: float = None):
        self._product_id = None
        self._quantity = None
        self._item_price = None
        if product_id is not None:
            self.product_id = product_id
        if quantity is not None:
            self.quantity = quantity
        if item_price is not None:
            self.item_price = item_price

    @property
    def product_id(self):
        """
        Gets Product Id.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id: str):
        """
        Sets Product Id.
        """
        self._product_id = product_id

    @property
    def quantity(self):
        """
        Gets number of product.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: str):
        """
        Set number of product.
        """
        self._quantity = quantity

    @property
    def item_price(self):
        """
        Gets Item Price.
        :rtype: float
        """
        return self._item_price

    @item_price.setter
    def item_price(self, item_price: float):
        """
        Sets Item Price.
        """
        self._item_price = item_price

    def normalize(self):
        normalized_payload = {
            'id': self.product_id,
            'quantity': self.quantity,
            'item_price': self.item_price,
        }
        normalized_payload: dict = {k: v for k, v in normalized_payload.items() if v is not None}
        return normalized_payload

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.param_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Content, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Content):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
