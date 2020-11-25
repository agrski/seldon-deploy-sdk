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


class TransformerSpec(object):
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
        'batcher': 'Batcher',
        'custom': 'CustomSpec',
        'logger': 'Logger',
        'max_replicas': 'int',
        'min_replicas': 'int',
        'parallelism': 'int',
        'service_account_name': 'str'
    }

    attribute_map = {
        'batcher': 'batcher',
        'custom': 'custom',
        'logger': 'logger',
        'max_replicas': 'maxReplicas',
        'min_replicas': 'minReplicas',
        'parallelism': 'parallelism',
        'service_account_name': 'serviceAccountName'
    }

    def __init__(self, batcher=None, custom=None, logger=None, max_replicas=None, min_replicas=None, parallelism=None, service_account_name=None):  # noqa: E501
        """TransformerSpec - a model defined in Swagger"""  # noqa: E501

        self._batcher = None
        self._custom = None
        self._logger = None
        self._max_replicas = None
        self._min_replicas = None
        self._parallelism = None
        self._service_account_name = None
        self.discriminator = None

        if batcher is not None:
            self.batcher = batcher
        if custom is not None:
            self.custom = custom
        if logger is not None:
            self.logger = logger
        if max_replicas is not None:
            self.max_replicas = max_replicas
        if min_replicas is not None:
            self.min_replicas = min_replicas
        if parallelism is not None:
            self.parallelism = parallelism
        if service_account_name is not None:
            self.service_account_name = service_account_name

    @property
    def batcher(self):
        """Gets the batcher of this TransformerSpec.  # noqa: E501


        :return: The batcher of this TransformerSpec.  # noqa: E501
        :rtype: Batcher
        """
        return self._batcher

    @batcher.setter
    def batcher(self, batcher):
        """Sets the batcher of this TransformerSpec.


        :param batcher: The batcher of this TransformerSpec.  # noqa: E501
        :type: Batcher
        """

        self._batcher = batcher

    @property
    def custom(self):
        """Gets the custom of this TransformerSpec.  # noqa: E501


        :return: The custom of this TransformerSpec.  # noqa: E501
        :rtype: CustomSpec
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this TransformerSpec.


        :param custom: The custom of this TransformerSpec.  # noqa: E501
        :type: CustomSpec
        """

        self._custom = custom

    @property
    def logger(self):
        """Gets the logger of this TransformerSpec.  # noqa: E501


        :return: The logger of this TransformerSpec.  # noqa: E501
        :rtype: Logger
        """
        return self._logger

    @logger.setter
    def logger(self, logger):
        """Sets the logger of this TransformerSpec.


        :param logger: The logger of this TransformerSpec.  # noqa: E501
        :type: Logger
        """

        self._logger = logger

    @property
    def max_replicas(self):
        """Gets the max_replicas of this TransformerSpec.  # noqa: E501

        This is the up bound for autoscaler to scale to +optional  # noqa: E501

        :return: The max_replicas of this TransformerSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """Sets the max_replicas of this TransformerSpec.

        This is the up bound for autoscaler to scale to +optional  # noqa: E501

        :param max_replicas: The max_replicas of this TransformerSpec.  # noqa: E501
        :type: int
        """

        self._max_replicas = max_replicas

    @property
    def min_replicas(self):
        """Gets the min_replicas of this TransformerSpec.  # noqa: E501

        Minimum number of replicas which defaults to 1, when minReplicas = 0 pods scale down to 0 in case of no traffic +optional  # noqa: E501

        :return: The min_replicas of this TransformerSpec.  # noqa: E501
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """Sets the min_replicas of this TransformerSpec.

        Minimum number of replicas which defaults to 1, when minReplicas = 0 pods scale down to 0 in case of no traffic +optional  # noqa: E501

        :param min_replicas: The min_replicas of this TransformerSpec.  # noqa: E501
        :type: int
        """

        self._min_replicas = min_replicas

    @property
    def parallelism(self):
        """Gets the parallelism of this TransformerSpec.  # noqa: E501

        Parallelism specifies how many requests can be processed concurrently, this sets the hard limit of the container concurrency(https://knative.dev/docs/serving/autoscaling/concurrency).  # noqa: E501

        :return: The parallelism of this TransformerSpec.  # noqa: E501
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this TransformerSpec.

        Parallelism specifies how many requests can be processed concurrently, this sets the hard limit of the container concurrency(https://knative.dev/docs/serving/autoscaling/concurrency).  # noqa: E501

        :param parallelism: The parallelism of this TransformerSpec.  # noqa: E501
        :type: int
        """

        self._parallelism = parallelism

    @property
    def service_account_name(self):
        """Gets the service_account_name of this TransformerSpec.  # noqa: E501

        ServiceAccountName is the name of the ServiceAccount to use to run the service +optional  # noqa: E501

        :return: The service_account_name of this TransformerSpec.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this TransformerSpec.

        ServiceAccountName is the name of the ServiceAccount to use to run the service +optional  # noqa: E501

        :param service_account_name: The service_account_name of this TransformerSpec.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

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
        if issubclass(TransformerSpec, dict):
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
        if not isinstance(other, TransformerSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
