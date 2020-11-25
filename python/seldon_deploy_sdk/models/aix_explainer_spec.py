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


class AIXExplainerSpec(object):
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
        'config': 'dict(str, str)',
        'resources': 'ResourceRequirements',
        'runtime_version': 'str',
        'storage_uri': 'str',
        'type': 'AIXExplainerType'
    }

    attribute_map = {
        'config': 'config',
        'resources': 'resources',
        'runtime_version': 'runtimeVersion',
        'storage_uri': 'storageUri',
        'type': 'type'
    }

    def __init__(self, config=None, resources=None, runtime_version=None, storage_uri=None, type=None):  # noqa: E501
        """AIXExplainerSpec - a model defined in Swagger"""  # noqa: E501

        self._config = None
        self._resources = None
        self._runtime_version = None
        self._storage_uri = None
        self._type = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if resources is not None:
            self.resources = resources
        if runtime_version is not None:
            self.runtime_version = runtime_version
        if storage_uri is not None:
            self.storage_uri = storage_uri
        if type is not None:
            self.type = type

    @property
    def config(self):
        """Gets the config of this AIXExplainerSpec.  # noqa: E501

        Inline custom parameter settings for explainer  # noqa: E501

        :return: The config of this AIXExplainerSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this AIXExplainerSpec.

        Inline custom parameter settings for explainer  # noqa: E501

        :param config: The config of this AIXExplainerSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._config = config

    @property
    def resources(self):
        """Gets the resources of this AIXExplainerSpec.  # noqa: E501


        :return: The resources of this AIXExplainerSpec.  # noqa: E501
        :rtype: ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this AIXExplainerSpec.


        :param resources: The resources of this AIXExplainerSpec.  # noqa: E501
        :type: ResourceRequirements
        """

        self._resources = resources

    @property
    def runtime_version(self):
        """Gets the runtime_version of this AIXExplainerSpec.  # noqa: E501

        Defaults to latest AIX Version  # noqa: E501

        :return: The runtime_version of this AIXExplainerSpec.  # noqa: E501
        :rtype: str
        """
        return self._runtime_version

    @runtime_version.setter
    def runtime_version(self, runtime_version):
        """Sets the runtime_version of this AIXExplainerSpec.

        Defaults to latest AIX Version  # noqa: E501

        :param runtime_version: The runtime_version of this AIXExplainerSpec.  # noqa: E501
        :type: str
        """

        self._runtime_version = runtime_version

    @property
    def storage_uri(self):
        """Gets the storage_uri of this AIXExplainerSpec.  # noqa: E501

        The location of a trained explanation model  # noqa: E501

        :return: The storage_uri of this AIXExplainerSpec.  # noqa: E501
        :rtype: str
        """
        return self._storage_uri

    @storage_uri.setter
    def storage_uri(self, storage_uri):
        """Sets the storage_uri of this AIXExplainerSpec.

        The location of a trained explanation model  # noqa: E501

        :param storage_uri: The storage_uri of this AIXExplainerSpec.  # noqa: E501
        :type: str
        """

        self._storage_uri = storage_uri

    @property
    def type(self):
        """Gets the type of this AIXExplainerSpec.  # noqa: E501


        :return: The type of this AIXExplainerSpec.  # noqa: E501
        :rtype: AIXExplainerType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AIXExplainerSpec.


        :param type: The type of this AIXExplainerSpec.  # noqa: E501
        :type: AIXExplainerType
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
        if issubclass(AIXExplainerSpec, dict):
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
        if not isinstance(other, AIXExplainerSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
