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


class ExternalMetricSource(object):
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
        'metric_name': 'str',
        'metric_selector': 'LabelSelector',
        'target_average_value': 'Quantity',
        'target_value': 'Quantity'
    }

    attribute_map = {
        'metric_name': 'metricName',
        'metric_selector': 'metricSelector',
        'target_average_value': 'targetAverageValue',
        'target_value': 'targetValue'
    }

    def __init__(self, metric_name=None, metric_selector=None, target_average_value=None, target_value=None):  # noqa: E501
        """ExternalMetricSource - a model defined in Swagger"""  # noqa: E501

        self._metric_name = None
        self._metric_selector = None
        self._target_average_value = None
        self._target_value = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if metric_selector is not None:
            self.metric_selector = metric_selector
        if target_average_value is not None:
            self.target_average_value = target_average_value
        if target_value is not None:
            self.target_value = target_value

    @property
    def metric_name(self):
        """Gets the metric_name of this ExternalMetricSource.  # noqa: E501

        metricName is the name of the metric in question.  # noqa: E501

        :return: The metric_name of this ExternalMetricSource.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this ExternalMetricSource.

        metricName is the name of the metric in question.  # noqa: E501

        :param metric_name: The metric_name of this ExternalMetricSource.  # noqa: E501
        :type: str
        """

        self._metric_name = metric_name

    @property
    def metric_selector(self):
        """Gets the metric_selector of this ExternalMetricSource.  # noqa: E501


        :return: The metric_selector of this ExternalMetricSource.  # noqa: E501
        :rtype: LabelSelector
        """
        return self._metric_selector

    @metric_selector.setter
    def metric_selector(self, metric_selector):
        """Sets the metric_selector of this ExternalMetricSource.


        :param metric_selector: The metric_selector of this ExternalMetricSource.  # noqa: E501
        :type: LabelSelector
        """

        self._metric_selector = metric_selector

    @property
    def target_average_value(self):
        """Gets the target_average_value of this ExternalMetricSource.  # noqa: E501


        :return: The target_average_value of this ExternalMetricSource.  # noqa: E501
        :rtype: Quantity
        """
        return self._target_average_value

    @target_average_value.setter
    def target_average_value(self, target_average_value):
        """Sets the target_average_value of this ExternalMetricSource.


        :param target_average_value: The target_average_value of this ExternalMetricSource.  # noqa: E501
        :type: Quantity
        """

        self._target_average_value = target_average_value

    @property
    def target_value(self):
        """Gets the target_value of this ExternalMetricSource.  # noqa: E501


        :return: The target_value of this ExternalMetricSource.  # noqa: E501
        :rtype: Quantity
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        """Sets the target_value of this ExternalMetricSource.


        :param target_value: The target_value of this ExternalMetricSource.  # noqa: E501
        :type: Quantity
        """

        self._target_value = target_value

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
        if issubclass(ExternalMetricSource, dict):
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
        if not isinstance(other, ExternalMetricSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other