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


class QuobyteVolumeSource(object):
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
        'group': 'str',
        'read_only': 'bool',
        'registry': 'str',
        'tenant': 'str',
        'user': 'str',
        'volume': 'str'
    }

    attribute_map = {
        'group': 'group',
        'read_only': 'readOnly',
        'registry': 'registry',
        'tenant': 'tenant',
        'user': 'user',
        'volume': 'volume'
    }

    def __init__(self, group=None, read_only=None, registry=None, tenant=None, user=None, volume=None):  # noqa: E501
        """QuobyteVolumeSource - a model defined in Swagger"""  # noqa: E501

        self._group = None
        self._read_only = None
        self._registry = None
        self._tenant = None
        self._user = None
        self._volume = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if read_only is not None:
            self.read_only = read_only
        if registry is not None:
            self.registry = registry
        if tenant is not None:
            self.tenant = tenant
        if user is not None:
            self.user = user
        if volume is not None:
            self.volume = volume

    @property
    def group(self):
        """Gets the group of this QuobyteVolumeSource.  # noqa: E501

        Group to map volume access to Default is no group +optional  # noqa: E501

        :return: The group of this QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this QuobyteVolumeSource.

        Group to map volume access to Default is no group +optional  # noqa: E501

        :param group: The group of this QuobyteVolumeSource.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def read_only(self):
        """Gets the read_only of this QuobyteVolumeSource.  # noqa: E501

        ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. +optional  # noqa: E501

        :return: The read_only of this QuobyteVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this QuobyteVolumeSource.

        ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. +optional  # noqa: E501

        :param read_only: The read_only of this QuobyteVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def registry(self):
        """Gets the registry of this QuobyteVolumeSource.  # noqa: E501

        Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes  # noqa: E501

        :return: The registry of this QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this QuobyteVolumeSource.

        Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes  # noqa: E501

        :param registry: The registry of this QuobyteVolumeSource.  # noqa: E501
        :type: str
        """

        self._registry = registry

    @property
    def tenant(self):
        """Gets the tenant of this QuobyteVolumeSource.  # noqa: E501

        Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin +optional  # noqa: E501

        :return: The tenant of this QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this QuobyteVolumeSource.

        Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin +optional  # noqa: E501

        :param tenant: The tenant of this QuobyteVolumeSource.  # noqa: E501
        :type: str
        """

        self._tenant = tenant

    @property
    def user(self):
        """Gets the user of this QuobyteVolumeSource.  # noqa: E501

        User to map volume access to Defaults to serivceaccount user +optional  # noqa: E501

        :return: The user of this QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this QuobyteVolumeSource.

        User to map volume access to Defaults to serivceaccount user +optional  # noqa: E501

        :param user: The user of this QuobyteVolumeSource.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def volume(self):
        """Gets the volume of this QuobyteVolumeSource.  # noqa: E501

        Volume is a string that references an already created Quobyte volume by name.  # noqa: E501

        :return: The volume of this QuobyteVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this QuobyteVolumeSource.

        Volume is a string that references an already created Quobyte volume by name.  # noqa: E501

        :param volume: The volume of this QuobyteVolumeSource.  # noqa: E501
        :type: str
        """

        self._volume = volume

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
        if issubclass(QuobyteVolumeSource, dict):
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
        if not isinstance(other, QuobyteVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
