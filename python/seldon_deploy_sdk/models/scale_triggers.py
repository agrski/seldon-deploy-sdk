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


class ScaleTriggers(object):
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
        'authentication_ref': 'ScaledObjectAuthRef',
        'metadata': 'dict(str, str)',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'authentication_ref': 'authenticationRef',
        'metadata': 'metadata',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, authentication_ref=None, metadata=None, name=None, type=None):  # noqa: E501
        """ScaleTriggers - a model defined in Swagger"""  # noqa: E501

        self._authentication_ref = None
        self._metadata = None
        self._name = None
        self._type = None
        self.discriminator = None

        if authentication_ref is not None:
            self.authentication_ref = authentication_ref
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def authentication_ref(self):
        """Gets the authentication_ref of this ScaleTriggers.  # noqa: E501


        :return: The authentication_ref of this ScaleTriggers.  # noqa: E501
        :rtype: ScaledObjectAuthRef
        """
        return self._authentication_ref

    @authentication_ref.setter
    def authentication_ref(self, authentication_ref):
        """Sets the authentication_ref of this ScaleTriggers.


        :param authentication_ref: The authentication_ref of this ScaleTriggers.  # noqa: E501
        :type: ScaledObjectAuthRef
        """

        self._authentication_ref = authentication_ref

    @property
    def metadata(self):
        """Gets the metadata of this ScaleTriggers.  # noqa: E501


        :return: The metadata of this ScaleTriggers.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ScaleTriggers.


        :param metadata: The metadata of this ScaleTriggers.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this ScaleTriggers.  # noqa: E501

        +optional  # noqa: E501

        :return: The name of this ScaleTriggers.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScaleTriggers.

        +optional  # noqa: E501

        :param name: The name of this ScaleTriggers.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ScaleTriggers.  # noqa: E501


        :return: The type of this ScaleTriggers.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScaleTriggers.


        :param type: The type of this ScaleTriggers.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ScaleTriggers, dict):
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
        if not isinstance(other, ScaleTriggers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
