# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import seldon_deploy_sdk
from seldon_deploy_sdk.api.seldon_deployments_api import SeldonDeploymentsApi  # noqa: E501
from seldon_deploy_sdk.rest import ApiException


class TestSeldonDeploymentsApi(unittest.TestCase):
    """SeldonDeploymentsApi unit test stubs"""

    def setUp(self):
        self.api = seldon_deploy_sdk.api.seldon_deployments_api.SeldonDeploymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_seldon_deployment(self):
        """Test case for create_seldon_deployment

        """
        pass

    def test_delete_seldon_deployment(self):
        """Test case for delete_seldon_deployment

        """
        pass

    def test_list_seldon_deployments(self):
        """Test case for list_seldon_deployments

        """
        pass

    def test_read_seldon_deployment(self):
        """Test case for read_seldon_deployment

        """
        pass

    def test_update_seldon_deployment(self):
        """Test case for update_seldon_deployment

        """
        pass

    def test_validate_seldon_deployment(self):
        """Test case for validate_seldon_deployment

        """
        pass


if __name__ == '__main__':
    unittest.main()
