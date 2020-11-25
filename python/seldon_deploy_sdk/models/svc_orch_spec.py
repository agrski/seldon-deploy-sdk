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


class SvcOrchSpec(object):
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
        'env': 'list[EnvVar]',
        'replicas': 'int',
        'resources': 'ResourceRequirements'
    }

    attribute_map = {
        'env': 'env',
        'replicas': 'replicas',
        'resources': 'resources'
    }

    def __init__(self, env=None, replicas=None, resources=None):  # noqa: E501
        """SvcOrchSpec - a model defined in Swagger"""  # noqa: E501

        self._env = None
        self._replicas = None
        self._resources = None
        self.discriminator = None

        if env is not None:
            self.env = env
        if replicas is not None:
            self.replicas = replicas
        if resources is not None:
            self.resources = resources

    @property
    def env(self):
        """Gets the env of this SvcOrchSpec.  # noqa: E501


        :return: The env of this SvcOrchSpec.  # noqa: E501
        :rtype: list[EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this SvcOrchSpec.


        :param env: The env of this SvcOrchSpec.  # noqa: E501
        :type: list[EnvVar]
        """

        self._env = env

    @property
    def replicas(self):
        """Gets the replicas of this SvcOrchSpec.  # noqa: E501


        :return: The replicas of this SvcOrchSpec.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this SvcOrchSpec.


        :param replicas: The replicas of this SvcOrchSpec.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def resources(self):
        """Gets the resources of this SvcOrchSpec.  # noqa: E501


        :return: The resources of this SvcOrchSpec.  # noqa: E501
        :rtype: ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this SvcOrchSpec.


        :param resources: The resources of this SvcOrchSpec.  # noqa: E501
        :type: ResourceRequirements
        """

        self._resources = resources

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
        if issubclass(SvcOrchSpec, dict):
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
        if not isinstance(other, SvcOrchSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
