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


class SeldonScaledObjectSpec(object):
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
        'advanced': 'AdvancedConfig',
        'cooldown_period': 'int',
        'max_replica_count': 'int',
        'min_replica_count': 'int',
        'polling_interval': 'int',
        'triggers': 'list[ScaleTriggers]'
    }

    attribute_map = {
        'advanced': 'advanced',
        'cooldown_period': 'cooldownPeriod',
        'max_replica_count': 'maxReplicaCount',
        'min_replica_count': 'minReplicaCount',
        'polling_interval': 'pollingInterval',
        'triggers': 'triggers'
    }

    def __init__(self, advanced=None, cooldown_period=None, max_replica_count=None, min_replica_count=None, polling_interval=None, triggers=None):  # noqa: E501
        """SeldonScaledObjectSpec - a model defined in Swagger"""  # noqa: E501

        self._advanced = None
        self._cooldown_period = None
        self._max_replica_count = None
        self._min_replica_count = None
        self._polling_interval = None
        self._triggers = None
        self.discriminator = None

        if advanced is not None:
            self.advanced = advanced
        if cooldown_period is not None:
            self.cooldown_period = cooldown_period
        if max_replica_count is not None:
            self.max_replica_count = max_replica_count
        if min_replica_count is not None:
            self.min_replica_count = min_replica_count
        if polling_interval is not None:
            self.polling_interval = polling_interval
        if triggers is not None:
            self.triggers = triggers

    @property
    def advanced(self):
        """Gets the advanced of this SeldonScaledObjectSpec.  # noqa: E501


        :return: The advanced of this SeldonScaledObjectSpec.  # noqa: E501
        :rtype: AdvancedConfig
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this SeldonScaledObjectSpec.


        :param advanced: The advanced of this SeldonScaledObjectSpec.  # noqa: E501
        :type: AdvancedConfig
        """

        self._advanced = advanced

    @property
    def cooldown_period(self):
        """Gets the cooldown_period of this SeldonScaledObjectSpec.  # noqa: E501

        +optional  # noqa: E501

        :return: The cooldown_period of this SeldonScaledObjectSpec.  # noqa: E501
        :rtype: int
        """
        return self._cooldown_period

    @cooldown_period.setter
    def cooldown_period(self, cooldown_period):
        """Sets the cooldown_period of this SeldonScaledObjectSpec.

        +optional  # noqa: E501

        :param cooldown_period: The cooldown_period of this SeldonScaledObjectSpec.  # noqa: E501
        :type: int
        """

        self._cooldown_period = cooldown_period

    @property
    def max_replica_count(self):
        """Gets the max_replica_count of this SeldonScaledObjectSpec.  # noqa: E501

        +optional  # noqa: E501

        :return: The max_replica_count of this SeldonScaledObjectSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_replica_count

    @max_replica_count.setter
    def max_replica_count(self, max_replica_count):
        """Sets the max_replica_count of this SeldonScaledObjectSpec.

        +optional  # noqa: E501

        :param max_replica_count: The max_replica_count of this SeldonScaledObjectSpec.  # noqa: E501
        :type: int
        """

        self._max_replica_count = max_replica_count

    @property
    def min_replica_count(self):
        """Gets the min_replica_count of this SeldonScaledObjectSpec.  # noqa: E501

        +optional  # noqa: E501

        :return: The min_replica_count of this SeldonScaledObjectSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_replica_count

    @min_replica_count.setter
    def min_replica_count(self, min_replica_count):
        """Sets the min_replica_count of this SeldonScaledObjectSpec.

        +optional  # noqa: E501

        :param min_replica_count: The min_replica_count of this SeldonScaledObjectSpec.  # noqa: E501
        :type: int
        """

        self._min_replica_count = min_replica_count

    @property
    def polling_interval(self):
        """Gets the polling_interval of this SeldonScaledObjectSpec.  # noqa: E501

        +optional  # noqa: E501

        :return: The polling_interval of this SeldonScaledObjectSpec.  # noqa: E501
        :rtype: int
        """
        return self._polling_interval

    @polling_interval.setter
    def polling_interval(self, polling_interval):
        """Sets the polling_interval of this SeldonScaledObjectSpec.

        +optional  # noqa: E501

        :param polling_interval: The polling_interval of this SeldonScaledObjectSpec.  # noqa: E501
        :type: int
        """

        self._polling_interval = polling_interval

    @property
    def triggers(self):
        """Gets the triggers of this SeldonScaledObjectSpec.  # noqa: E501


        :return: The triggers of this SeldonScaledObjectSpec.  # noqa: E501
        :rtype: list[ScaleTriggers]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this SeldonScaledObjectSpec.


        :param triggers: The triggers of this SeldonScaledObjectSpec.  # noqa: E501
        :type: list[ScaleTriggers]
        """

        self._triggers = triggers

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
        if issubclass(SeldonScaledObjectSpec, dict):
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
        if not isinstance(other, SeldonScaledObjectSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
