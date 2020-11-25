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


class AnalyticsProps(object):
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
        'build_time': 'str',
        'build_version': 'str',
        'git_branch': 'str',
        'git_commit': 'str',
        'git_status': 'str',
        'release_type': 'str',
        'distinct_id': 'str',
        'token': 'str'
    }

    attribute_map = {
        'build_time': 'BuildTime',
        'build_version': 'BuildVersion',
        'git_branch': 'GitBranch',
        'git_commit': 'GitCommit',
        'git_status': 'GitStatus',
        'release_type': 'ReleaseType',
        'distinct_id': 'distinct_id',
        'token': 'token'
    }

    def __init__(self, build_time=None, build_version=None, git_branch=None, git_commit=None, git_status=None, release_type=None, distinct_id=None, token=None):  # noqa: E501
        """AnalyticsProps - a model defined in Swagger"""  # noqa: E501

        self._build_time = None
        self._build_version = None
        self._git_branch = None
        self._git_commit = None
        self._git_status = None
        self._release_type = None
        self._distinct_id = None
        self._token = None
        self.discriminator = None

        if build_time is not None:
            self.build_time = build_time
        if build_version is not None:
            self.build_version = build_version
        if git_branch is not None:
            self.git_branch = git_branch
        if git_commit is not None:
            self.git_commit = git_commit
        if git_status is not None:
            self.git_status = git_status
        if release_type is not None:
            self.release_type = release_type
        if distinct_id is not None:
            self.distinct_id = distinct_id
        if token is not None:
            self.token = token

    @property
    def build_time(self):
        """Gets the build_time of this AnalyticsProps.  # noqa: E501


        :return: The build_time of this AnalyticsProps.  # noqa: E501
        :rtype: str
        """
        return self._build_time

    @build_time.setter
    def build_time(self, build_time):
        """Sets the build_time of this AnalyticsProps.


        :param build_time: The build_time of this AnalyticsProps.  # noqa: E501
        :type: str
        """

        self._build_time = build_time

    @property
    def build_version(self):
        """Gets the build_version of this AnalyticsProps.  # noqa: E501


        :return: The build_version of this AnalyticsProps.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this AnalyticsProps.


        :param build_version: The build_version of this AnalyticsProps.  # noqa: E501
        :type: str
        """

        self._build_version = build_version

    @property
    def git_branch(self):
        """Gets the git_branch of this AnalyticsProps.  # noqa: E501


        :return: The git_branch of this AnalyticsProps.  # noqa: E501
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        """Sets the git_branch of this AnalyticsProps.


        :param git_branch: The git_branch of this AnalyticsProps.  # noqa: E501
        :type: str
        """

        self._git_branch = git_branch

    @property
    def git_commit(self):
        """Gets the git_commit of this AnalyticsProps.  # noqa: E501


        :return: The git_commit of this AnalyticsProps.  # noqa: E501
        :rtype: str
        """
        return self._git_commit

    @git_commit.setter
    def git_commit(self, git_commit):
        """Sets the git_commit of this AnalyticsProps.


        :param git_commit: The git_commit of this AnalyticsProps.  # noqa: E501
        :type: str
        """

        self._git_commit = git_commit

    @property
    def git_status(self):
        """Gets the git_status of this AnalyticsProps.  # noqa: E501


        :return: The git_status of this AnalyticsProps.  # noqa: E501
        :rtype: str
        """
        return self._git_status

    @git_status.setter
    def git_status(self, git_status):
        """Sets the git_status of this AnalyticsProps.


        :param git_status: The git_status of this AnalyticsProps.  # noqa: E501
        :type: str
        """

        self._git_status = git_status

    @property
    def release_type(self):
        """Gets the release_type of this AnalyticsProps.  # noqa: E501


        :return: The release_type of this AnalyticsProps.  # noqa: E501
        :rtype: str
        """
        return self._release_type

    @release_type.setter
    def release_type(self, release_type):
        """Sets the release_type of this AnalyticsProps.


        :param release_type: The release_type of this AnalyticsProps.  # noqa: E501
        :type: str
        """

        self._release_type = release_type

    @property
    def distinct_id(self):
        """Gets the distinct_id of this AnalyticsProps.  # noqa: E501


        :return: The distinct_id of this AnalyticsProps.  # noqa: E501
        :rtype: str
        """
        return self._distinct_id

    @distinct_id.setter
    def distinct_id(self, distinct_id):
        """Sets the distinct_id of this AnalyticsProps.


        :param distinct_id: The distinct_id of this AnalyticsProps.  # noqa: E501
        :type: str
        """

        self._distinct_id = distinct_id

    @property
    def token(self):
        """Gets the token of this AnalyticsProps.  # noqa: E501


        :return: The token of this AnalyticsProps.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AnalyticsProps.


        :param token: The token of this AnalyticsProps.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(AnalyticsProps, dict):
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
        if not isinstance(other, AnalyticsProps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
