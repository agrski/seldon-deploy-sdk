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


class ContainerStateTerminated(object):
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
        'container_id': 'str',
        'exit_code': 'int',
        'finished_at': 'Time',
        'message': 'str',
        'reason': 'str',
        'signal': 'int',
        'started_at': 'Time'
    }

    attribute_map = {
        'container_id': 'containerID',
        'exit_code': 'exitCode',
        'finished_at': 'finishedAt',
        'message': 'message',
        'reason': 'reason',
        'signal': 'signal',
        'started_at': 'startedAt'
    }

    def __init__(self, container_id=None, exit_code=None, finished_at=None, message=None, reason=None, signal=None, started_at=None):  # noqa: E501
        """ContainerStateTerminated - a model defined in Swagger"""  # noqa: E501

        self._container_id = None
        self._exit_code = None
        self._finished_at = None
        self._message = None
        self._reason = None
        self._signal = None
        self._started_at = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        if exit_code is not None:
            self.exit_code = exit_code
        if finished_at is not None:
            self.finished_at = finished_at
        if message is not None:
            self.message = message
        if reason is not None:
            self.reason = reason
        if signal is not None:
            self.signal = signal
        if started_at is not None:
            self.started_at = started_at

    @property
    def container_id(self):
        """Gets the container_id of this ContainerStateTerminated.  # noqa: E501

        Container's ID in the format 'docker://<container_id>' +optional  # noqa: E501

        :return: The container_id of this ContainerStateTerminated.  # noqa: E501
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this ContainerStateTerminated.

        Container's ID in the format 'docker://<container_id>' +optional  # noqa: E501

        :param container_id: The container_id of this ContainerStateTerminated.  # noqa: E501
        :type: str
        """

        self._container_id = container_id

    @property
    def exit_code(self):
        """Gets the exit_code of this ContainerStateTerminated.  # noqa: E501

        Exit status from the last termination of the container  # noqa: E501

        :return: The exit_code of this ContainerStateTerminated.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this ContainerStateTerminated.

        Exit status from the last termination of the container  # noqa: E501

        :param exit_code: The exit_code of this ContainerStateTerminated.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def finished_at(self):
        """Gets the finished_at of this ContainerStateTerminated.  # noqa: E501


        :return: The finished_at of this ContainerStateTerminated.  # noqa: E501
        :rtype: Time
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this ContainerStateTerminated.


        :param finished_at: The finished_at of this ContainerStateTerminated.  # noqa: E501
        :type: Time
        """

        self._finished_at = finished_at

    @property
    def message(self):
        """Gets the message of this ContainerStateTerminated.  # noqa: E501

        Message regarding the last termination of the container +optional  # noqa: E501

        :return: The message of this ContainerStateTerminated.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ContainerStateTerminated.

        Message regarding the last termination of the container +optional  # noqa: E501

        :param message: The message of this ContainerStateTerminated.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """Gets the reason of this ContainerStateTerminated.  # noqa: E501

        (brief) reason from the last termination of the container +optional  # noqa: E501

        :return: The reason of this ContainerStateTerminated.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ContainerStateTerminated.

        (brief) reason from the last termination of the container +optional  # noqa: E501

        :param reason: The reason of this ContainerStateTerminated.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def signal(self):
        """Gets the signal of this ContainerStateTerminated.  # noqa: E501

        Signal from the last termination of the container +optional  # noqa: E501

        :return: The signal of this ContainerStateTerminated.  # noqa: E501
        :rtype: int
        """
        return self._signal

    @signal.setter
    def signal(self, signal):
        """Sets the signal of this ContainerStateTerminated.

        Signal from the last termination of the container +optional  # noqa: E501

        :param signal: The signal of this ContainerStateTerminated.  # noqa: E501
        :type: int
        """

        self._signal = signal

    @property
    def started_at(self):
        """Gets the started_at of this ContainerStateTerminated.  # noqa: E501


        :return: The started_at of this ContainerStateTerminated.  # noqa: E501
        :rtype: Time
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this ContainerStateTerminated.


        :param started_at: The started_at of this ContainerStateTerminated.  # noqa: E501
        :type: Time
        """

        self._started_at = started_at

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
        if issubclass(ContainerStateTerminated, dict):
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
        if not isinstance(other, ContainerStateTerminated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
