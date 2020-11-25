# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InferenceServiceList(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        'items': 'list[InferenceService]',
        'kind': 'str',
        'metadata': 'ListMeta'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'items': 'items',
        'kind': 'kind',
        'metadata': 'metadata'
    }

    def __init__(self, api_version=None, items=None, kind=None, metadata=None):  # noqa: E501
        """InferenceServiceList - a model defined in Swagger"""  # noqa: E501

        self._api_version = None
        self._items = None
        self._kind = None
        self._metadata = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if items is not None:
            self.items = items
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata

    @property
    def api_version(self):
        """Gets the api_version of this InferenceServiceList.  # noqa: E501


        :return: The api_version of this InferenceServiceList.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this InferenceServiceList.


        :param api_version: The api_version of this InferenceServiceList.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def items(self):
        """Gets the items of this InferenceServiceList.  # noqa: E501


        :return: The items of this InferenceServiceList.  # noqa: E501
        :rtype: list[InferenceService]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this InferenceServiceList.


        :param items: The items of this InferenceServiceList.  # noqa: E501
        :type: list[InferenceService]
        """

        self._items = items

    @property
    def kind(self):
        """Gets the kind of this InferenceServiceList.  # noqa: E501


        :return: The kind of this InferenceServiceList.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this InferenceServiceList.


        :param kind: The kind of this InferenceServiceList.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this InferenceServiceList.  # noqa: E501


        :return: The metadata of this InferenceServiceList.  # noqa: E501
        :rtype: ListMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InferenceServiceList.


        :param metadata: The metadata of this InferenceServiceList.  # noqa: E501
        :type: ListMeta
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InferenceServiceList, dict):
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
        if not isinstance(other, InferenceServiceList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
