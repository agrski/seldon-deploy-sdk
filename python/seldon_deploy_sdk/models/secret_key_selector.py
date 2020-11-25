# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SecretKeySelector(object):
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
        'key': 'str',
        'name': 'str',
        'optional': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'optional': 'optional'
    }

    def __init__(self, key=None, name=None, optional=None):  # noqa: E501
        """SecretKeySelector - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._name = None
        self._optional = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if optional is not None:
            self.optional = optional

    @property
    def key(self):
        """Gets the key of this SecretKeySelector.  # noqa: E501

        The key of the secret to select from.  Must be a valid secret key.  # noqa: E501

        :return: The key of this SecretKeySelector.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SecretKeySelector.

        The key of the secret to select from.  Must be a valid secret key.  # noqa: E501

        :param key: The key of this SecretKeySelector.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this SecretKeySelector.  # noqa: E501

        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? +optional  # noqa: E501

        :return: The name of this SecretKeySelector.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecretKeySelector.

        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? +optional  # noqa: E501

        :param name: The name of this SecretKeySelector.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def optional(self):
        """Gets the optional of this SecretKeySelector.  # noqa: E501

        Specify whether the Secret or its key must be defined +optional  # noqa: E501

        :return: The optional of this SecretKeySelector.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this SecretKeySelector.

        Specify whether the Secret or its key must be defined +optional  # noqa: E501

        :param optional: The optional of this SecretKeySelector.  # noqa: E501
        :type: bool
        """

        self._optional = optional

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
        if issubclass(SecretKeySelector, dict):
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
        if not isinstance(other, SecretKeySelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
