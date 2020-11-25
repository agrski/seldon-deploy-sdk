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


class SSL(object):
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
        'cert_secret_name': 'str'
    }

    attribute_map = {
        'cert_secret_name': 'certSecretName'
    }

    def __init__(self, cert_secret_name=None):  # noqa: E501
        """SSL - a model defined in Swagger"""  # noqa: E501

        self._cert_secret_name = None
        self.discriminator = None

        if cert_secret_name is not None:
            self.cert_secret_name = cert_secret_name

    @property
    def cert_secret_name(self):
        """Gets the cert_secret_name of this SSL.  # noqa: E501


        :return: The cert_secret_name of this SSL.  # noqa: E501
        :rtype: str
        """
        return self._cert_secret_name

    @cert_secret_name.setter
    def cert_secret_name(self, cert_secret_name):
        """Sets the cert_secret_name of this SSL.


        :param cert_secret_name: The cert_secret_name of this SSL.  # noqa: E501
        :type: str
        """

        self._cert_secret_name = cert_secret_name

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
        if issubclass(SSL, dict):
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
        if not isinstance(other, SSL):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
