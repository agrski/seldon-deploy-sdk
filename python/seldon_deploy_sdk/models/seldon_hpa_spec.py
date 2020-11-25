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


class SeldonHpaSpec(object):
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
        'max_replicas': 'int',
        'metrics': 'list[MetricSpec]',
        'min_replicas': 'int'
    }

    attribute_map = {
        'max_replicas': 'maxReplicas',
        'metrics': 'metrics',
        'min_replicas': 'minReplicas'
    }

    def __init__(self, max_replicas=None, metrics=None, min_replicas=None):  # noqa: E501
        """SeldonHpaSpec - a model defined in Swagger"""  # noqa: E501

        self._max_replicas = None
        self._metrics = None
        self._min_replicas = None
        self.discriminator = None

        if max_replicas is not None:
            self.max_replicas = max_replicas
        if metrics is not None:
            self.metrics = metrics
        if min_replicas is not None:
            self.min_replicas = min_replicas

    @property
    def max_replicas(self):
        """Gets the max_replicas of this SeldonHpaSpec.  # noqa: E501


        :return: The max_replicas of this SeldonHpaSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """Sets the max_replicas of this SeldonHpaSpec.


        :param max_replicas: The max_replicas of this SeldonHpaSpec.  # noqa: E501
        :type: int
        """

        self._max_replicas = max_replicas

    @property
    def metrics(self):
        """Gets the metrics of this SeldonHpaSpec.  # noqa: E501


        :return: The metrics of this SeldonHpaSpec.  # noqa: E501
        :rtype: list[MetricSpec]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this SeldonHpaSpec.


        :param metrics: The metrics of this SeldonHpaSpec.  # noqa: E501
        :type: list[MetricSpec]
        """

        self._metrics = metrics

    @property
    def min_replicas(self):
        """Gets the min_replicas of this SeldonHpaSpec.  # noqa: E501


        :return: The min_replicas of this SeldonHpaSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """Sets the min_replicas of this SeldonHpaSpec.


        :param min_replicas: The min_replicas of this SeldonHpaSpec.  # noqa: E501
        :type: int
        """

        self._min_replicas = min_replicas

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
        if issubclass(SeldonHpaSpec, dict):
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
        if not isinstance(other, SeldonHpaSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
