# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import seldon_deploy_client
from seldon_deploy_client.api.inference_services_api import InferenceServicesApi  # noqa: E501
from seldon_deploy_client.rest import ApiException


class TestInferenceServicesApi(unittest.TestCase):
    """InferenceServicesApi unit test stubs"""

    def setUp(self):
        self.api = seldon_deploy_client.api.inference_services_api.InferenceServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_inference_service(self):
        """Test case for create_inference_service

        """
        pass

    def test_delete_inference_service(self):
        """Test case for delete_inference_service

        """
        pass

    def test_list_inference_services(self):
        """Test case for list_inference_services

        """
        pass

    def test_read_inference_service(self):
        """Test case for read_inference_service

        """
        pass

    def test_update_inference_service(self):
        """Test case for update_inference_service

        """
        pass

    def test_validate_inference_service(self):
        """Test case for validate_inference_service

        """
        pass


if __name__ == '__main__':
    unittest.main()
