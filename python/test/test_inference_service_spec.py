# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import seldon_deploy_sdk
from seldon_deploy_sdk.models.inference_service_spec import InferenceServiceSpec  # noqa: E501
from seldon_deploy_sdk.rest import ApiException


class TestInferenceServiceSpec(unittest.TestCase):
    """InferenceServiceSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInferenceServiceSpec(self):
        """Test InferenceServiceSpec"""
        # FIXME: construct object with mandatory attributes with example values
        # model = seldon_deploy_sdk.models.inference_service_spec.InferenceServiceSpec()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
