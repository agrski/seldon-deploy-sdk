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


class PodList(object):
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
        '_continue': 'str',
        'items': 'list[Pod]',
        'kind': 'str',
        'remaining_item_count': 'int',
        'resource_version': 'str',
        'self_link': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        '_continue': 'continue',
        'items': 'items',
        'kind': 'kind',
        'remaining_item_count': 'remainingItemCount',
        'resource_version': 'resourceVersion',
        'self_link': 'selfLink'
    }

    def __init__(self, api_version=None, _continue=None, items=None, kind=None, remaining_item_count=None, resource_version=None, self_link=None):  # noqa: E501
        """PodList - a model defined in Swagger"""  # noqa: E501

        self._api_version = None
        self.__continue = None
        self._items = None
        self._kind = None
        self._remaining_item_count = None
        self._resource_version = None
        self._self_link = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if _continue is not None:
            self._continue = _continue
        if items is not None:
            self.items = items
        if kind is not None:
            self.kind = kind
        if remaining_item_count is not None:
            self.remaining_item_count = remaining_item_count
        if resource_version is not None:
            self.resource_version = resource_version
        if self_link is not None:
            self.self_link = self_link

    @property
    def api_version(self):
        """Gets the api_version of this PodList.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources +optional  # noqa: E501

        :return: The api_version of this PodList.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this PodList.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources +optional  # noqa: E501

        :param api_version: The api_version of this PodList.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def _continue(self):
        """Gets the _continue of this PodList.  # noqa: E501

        continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.  # noqa: E501

        :return: The _continue of this PodList.  # noqa: E501
        :rtype: str
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        """Sets the _continue of this PodList.

        continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.  # noqa: E501

        :param _continue: The _continue of this PodList.  # noqa: E501
        :type: str
        """

        self.__continue = _continue

    @property
    def items(self):
        """Gets the items of this PodList.  # noqa: E501

        List of pods. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md  # noqa: E501

        :return: The items of this PodList.  # noqa: E501
        :rtype: list[Pod]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PodList.

        List of pods. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md  # noqa: E501

        :param items: The items of this PodList.  # noqa: E501
        :type: list[Pod]
        """

        self._items = items

    @property
    def kind(self):
        """Gets the kind of this PodList.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds +optional  # noqa: E501

        :return: The kind of this PodList.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PodList.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds +optional  # noqa: E501

        :param kind: The kind of this PodList.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def remaining_item_count(self):
        """Gets the remaining_item_count of this PodList.  # noqa: E501

        remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact. +optional  # noqa: E501

        :return: The remaining_item_count of this PodList.  # noqa: E501
        :rtype: int
        """
        return self._remaining_item_count

    @remaining_item_count.setter
    def remaining_item_count(self, remaining_item_count):
        """Sets the remaining_item_count of this PodList.

        remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact. +optional  # noqa: E501

        :param remaining_item_count: The remaining_item_count of this PodList.  # noqa: E501
        :type: int
        """

        self._remaining_item_count = remaining_item_count

    @property
    def resource_version(self):
        """Gets the resource_version of this PodList.  # noqa: E501

        String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency +optional  # noqa: E501

        :return: The resource_version of this PodList.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this PodList.

        String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency +optional  # noqa: E501

        :param resource_version: The resource_version of this PodList.  # noqa: E501
        :type: str
        """

        self._resource_version = resource_version

    @property
    def self_link(self):
        """Gets the self_link of this PodList.  # noqa: E501

        selfLink is a URL representing this object. Populated by the system. Read-only.  DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release. +optional  # noqa: E501

        :return: The self_link of this PodList.  # noqa: E501
        :rtype: str
        """
        return self._self_link

    @self_link.setter
    def self_link(self, self_link):
        """Sets the self_link of this PodList.

        selfLink is a URL representing this object. Populated by the system. Read-only.  DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release. +optional  # noqa: E501

        :param self_link: The self_link of this PodList.  # noqa: E501
        :type: str
        """

        self._self_link = self_link

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
        if issubclass(PodList, dict):
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
        if not isinstance(other, PodList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
