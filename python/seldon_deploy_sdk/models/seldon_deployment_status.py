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


class SeldonDeploymentStatus(object):
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
        'address': 'SeldonAddressable',
        'deployment_status': 'dict(str, DeploymentStatus)',
        'description': 'str',
        'replicas': 'int',
        'service_status': 'dict(str, ServiceStatus)',
        'state': 'StatusState'
    }

    attribute_map = {
        'address': 'address',
        'deployment_status': 'deploymentStatus',
        'description': 'description',
        'replicas': 'replicas',
        'service_status': 'serviceStatus',
        'state': 'state'
    }

    def __init__(self, address=None, deployment_status=None, description=None, replicas=None, service_status=None, state=None):  # noqa: E501
        """SeldonDeploymentStatus - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._deployment_status = None
        self._description = None
        self._replicas = None
        self._service_status = None
        self._state = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if deployment_status is not None:
            self.deployment_status = deployment_status
        if description is not None:
            self.description = description
        if replicas is not None:
            self.replicas = replicas
        if service_status is not None:
            self.service_status = service_status
        if state is not None:
            self.state = state

    @property
    def address(self):
        """Gets the address of this SeldonDeploymentStatus.  # noqa: E501


        :return: The address of this SeldonDeploymentStatus.  # noqa: E501
        :rtype: SeldonAddressable
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SeldonDeploymentStatus.


        :param address: The address of this SeldonDeploymentStatus.  # noqa: E501
        :type: SeldonAddressable
        """

        self._address = address

    @property
    def deployment_status(self):
        """Gets the deployment_status of this SeldonDeploymentStatus.  # noqa: E501


        :return: The deployment_status of this SeldonDeploymentStatus.  # noqa: E501
        :rtype: dict(str, DeploymentStatus)
        """
        return self._deployment_status

    @deployment_status.setter
    def deployment_status(self, deployment_status):
        """Sets the deployment_status of this SeldonDeploymentStatus.


        :param deployment_status: The deployment_status of this SeldonDeploymentStatus.  # noqa: E501
        :type: dict(str, DeploymentStatus)
        """

        self._deployment_status = deployment_status

    @property
    def description(self):
        """Gets the description of this SeldonDeploymentStatus.  # noqa: E501


        :return: The description of this SeldonDeploymentStatus.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SeldonDeploymentStatus.


        :param description: The description of this SeldonDeploymentStatus.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def replicas(self):
        """Gets the replicas of this SeldonDeploymentStatus.  # noqa: E501


        :return: The replicas of this SeldonDeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this SeldonDeploymentStatus.


        :param replicas: The replicas of this SeldonDeploymentStatus.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def service_status(self):
        """Gets the service_status of this SeldonDeploymentStatus.  # noqa: E501


        :return: The service_status of this SeldonDeploymentStatus.  # noqa: E501
        :rtype: dict(str, ServiceStatus)
        """
        return self._service_status

    @service_status.setter
    def service_status(self, service_status):
        """Sets the service_status of this SeldonDeploymentStatus.


        :param service_status: The service_status of this SeldonDeploymentStatus.  # noqa: E501
        :type: dict(str, ServiceStatus)
        """

        self._service_status = service_status

    @property
    def state(self):
        """Gets the state of this SeldonDeploymentStatus.  # noqa: E501


        :return: The state of this SeldonDeploymentStatus.  # noqa: E501
        :rtype: StatusState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SeldonDeploymentStatus.


        :param state: The state of this SeldonDeploymentStatus.  # noqa: E501
        :type: StatusState
        """

        self._state = state

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
        if issubclass(SeldonDeploymentStatus, dict):
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
        if not isinstance(other, SeldonDeploymentStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
