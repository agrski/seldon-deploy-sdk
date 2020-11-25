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


class ServiceStatus(object):
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
        'explainer_for': 'str',
        'grpc_endpoint': 'str',
        'http_endpoint': 'str',
        'svc_name': 'str'
    }

    attribute_map = {
        'explainer_for': 'explainerFor',
        'grpc_endpoint': 'grpcEndpoint',
        'http_endpoint': 'httpEndpoint',
        'svc_name': 'svcName'
    }

    def __init__(self, explainer_for=None, grpc_endpoint=None, http_endpoint=None, svc_name=None):  # noqa: E501
        """ServiceStatus - a model defined in Swagger"""  # noqa: E501

        self._explainer_for = None
        self._grpc_endpoint = None
        self._http_endpoint = None
        self._svc_name = None
        self.discriminator = None

        if explainer_for is not None:
            self.explainer_for = explainer_for
        if grpc_endpoint is not None:
            self.grpc_endpoint = grpc_endpoint
        if http_endpoint is not None:
            self.http_endpoint = http_endpoint
        if svc_name is not None:
            self.svc_name = svc_name

    @property
    def explainer_for(self):
        """Gets the explainer_for of this ServiceStatus.  # noqa: E501


        :return: The explainer_for of this ServiceStatus.  # noqa: E501
        :rtype: str
        """
        return self._explainer_for

    @explainer_for.setter
    def explainer_for(self, explainer_for):
        """Sets the explainer_for of this ServiceStatus.


        :param explainer_for: The explainer_for of this ServiceStatus.  # noqa: E501
        :type: str
        """

        self._explainer_for = explainer_for

    @property
    def grpc_endpoint(self):
        """Gets the grpc_endpoint of this ServiceStatus.  # noqa: E501


        :return: The grpc_endpoint of this ServiceStatus.  # noqa: E501
        :rtype: str
        """
        return self._grpc_endpoint

    @grpc_endpoint.setter
    def grpc_endpoint(self, grpc_endpoint):
        """Sets the grpc_endpoint of this ServiceStatus.


        :param grpc_endpoint: The grpc_endpoint of this ServiceStatus.  # noqa: E501
        :type: str
        """

        self._grpc_endpoint = grpc_endpoint

    @property
    def http_endpoint(self):
        """Gets the http_endpoint of this ServiceStatus.  # noqa: E501


        :return: The http_endpoint of this ServiceStatus.  # noqa: E501
        :rtype: str
        """
        return self._http_endpoint

    @http_endpoint.setter
    def http_endpoint(self, http_endpoint):
        """Sets the http_endpoint of this ServiceStatus.


        :param http_endpoint: The http_endpoint of this ServiceStatus.  # noqa: E501
        :type: str
        """

        self._http_endpoint = http_endpoint

    @property
    def svc_name(self):
        """Gets the svc_name of this ServiceStatus.  # noqa: E501


        :return: The svc_name of this ServiceStatus.  # noqa: E501
        :rtype: str
        """
        return self._svc_name

    @svc_name.setter
    def svc_name(self, svc_name):
        """Sets the svc_name of this ServiceStatus.


        :param svc_name: The svc_name of this ServiceStatus.  # noqa: E501
        :type: str
        """

        self._svc_name = svc_name

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
        if issubclass(ServiceStatus, dict):
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
        if not isinstance(other, ServiceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
