# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from seldon_deploy_client.api_client import ApiClient


class PredictApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def predict_file_inference_service(self, name, namespace, predict_file, **kwargs):  # noqa: E501
        """predict_file_inference_service  # noqa: E501

        Create Inference Service prediction  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.predict_file_inference_service(name, namespace, predict_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param file predict_file: PredictionFile (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.predict_file_inference_service_with_http_info(name, namespace, predict_file, **kwargs)  # noqa: E501
        else:
            (data) = self.predict_file_inference_service_with_http_info(name, namespace, predict_file, **kwargs)  # noqa: E501
            return data

    def predict_file_inference_service_with_http_info(self, name, namespace, predict_file, **kwargs):  # noqa: E501
        """predict_file_inference_service  # noqa: E501

        Create Inference Service prediction  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.predict_file_inference_service_with_http_info(name, namespace, predict_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param file predict_file: PredictionFile (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'predict_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method predict_file_inference_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `predict_file_inference_service`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `predict_file_inference_service`")  # noqa: E501
        # verify the required parameter 'predict_file' is set
        if ('predict_file' not in params or
                params['predict_file'] is None):
            raise ValueError("Missing the required parameter `predict_file` when calling `predict_file_inference_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'predict_file' in params:
            local_var_files['predictFile'] = params['predict_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespace}/inferenceservices/{name}/predictfile', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def predict_file_seldon_deployment(self, name, namespace, predict_file, **kwargs):  # noqa: E501
        """predict_file_seldon_deployment  # noqa: E501

        Create Seldon Deployment prediction  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.predict_file_seldon_deployment(name, namespace, predict_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param file predict_file: PredictionFile (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.predict_file_seldon_deployment_with_http_info(name, namespace, predict_file, **kwargs)  # noqa: E501
        else:
            (data) = self.predict_file_seldon_deployment_with_http_info(name, namespace, predict_file, **kwargs)  # noqa: E501
            return data

    def predict_file_seldon_deployment_with_http_info(self, name, namespace, predict_file, **kwargs):  # noqa: E501
        """predict_file_seldon_deployment  # noqa: E501

        Create Seldon Deployment prediction  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.predict_file_seldon_deployment_with_http_info(name, namespace, predict_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param file predict_file: PredictionFile (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'predict_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method predict_file_seldon_deployment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `predict_file_seldon_deployment`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `predict_file_seldon_deployment`")  # noqa: E501
        # verify the required parameter 'predict_file' is set
        if ('predict_file' not in params or
                params['predict_file'] is None):
            raise ValueError("Missing the required parameter `predict_file` when calling `predict_file_seldon_deployment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'predict_file' in params:
            local_var_files['predictFile'] = params['predict_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespace}/seldondeployments/{name}/predictfile', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def predict_inference_service(self, name, namespace, prediction, **kwargs):  # noqa: E501
        """predict_inference_service  # noqa: E501

        Create Inference Service prediction  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.predict_inference_service(name, namespace, prediction, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param object prediction: Prediction (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.predict_inference_service_with_http_info(name, namespace, prediction, **kwargs)  # noqa: E501
        else:
            (data) = self.predict_inference_service_with_http_info(name, namespace, prediction, **kwargs)  # noqa: E501
            return data

    def predict_inference_service_with_http_info(self, name, namespace, prediction, **kwargs):  # noqa: E501
        """predict_inference_service  # noqa: E501

        Create Inference Service prediction  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.predict_inference_service_with_http_info(name, namespace, prediction, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param object prediction: Prediction (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'prediction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method predict_inference_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `predict_inference_service`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `predict_inference_service`")  # noqa: E501
        # verify the required parameter 'prediction' is set
        if ('prediction' not in params or
                params['prediction'] is None):
            raise ValueError("Missing the required parameter `prediction` when calling `predict_inference_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'prediction' in params:
            body_params = params['prediction']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespace}/inferenceservices/{name}/predict', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def predict_seldon_deployment(self, name, namespace, prediction, **kwargs):  # noqa: E501
        """predict_seldon_deployment  # noqa: E501

        Create Seldon Deployment prediction  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.predict_seldon_deployment(name, namespace, prediction, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param object prediction: Prediction (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.predict_seldon_deployment_with_http_info(name, namespace, prediction, **kwargs)  # noqa: E501
        else:
            (data) = self.predict_seldon_deployment_with_http_info(name, namespace, prediction, **kwargs)  # noqa: E501
            return data

    def predict_seldon_deployment_with_http_info(self, name, namespace, prediction, **kwargs):  # noqa: E501
        """predict_seldon_deployment  # noqa: E501

        Create Seldon Deployment prediction  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.predict_seldon_deployment_with_http_info(name, namespace, prediction, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param object prediction: Prediction (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'prediction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method predict_seldon_deployment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `predict_seldon_deployment`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `predict_seldon_deployment`")  # noqa: E501
        # verify the required parameter 'prediction' is set
        if ('prediction' not in params or
                params['prediction'] is None):
            raise ValueError("Missing the required parameter `prediction` when calling `predict_seldon_deployment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'prediction' in params:
            body_params = params['prediction']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespace}/seldondeployments/{name}/predict', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_predict_curl_inference_service(self, name, namespace, prediction, **kwargs):  # noqa: E501
        """read_predict_curl_inference_service  # noqa: E501

        Read the specified Inference Service predict curl  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_predict_curl_inference_service(name, namespace, prediction, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param object prediction: Prediction (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_predict_curl_inference_service_with_http_info(name, namespace, prediction, **kwargs)  # noqa: E501
        else:
            (data) = self.read_predict_curl_inference_service_with_http_info(name, namespace, prediction, **kwargs)  # noqa: E501
            return data

    def read_predict_curl_inference_service_with_http_info(self, name, namespace, prediction, **kwargs):  # noqa: E501
        """read_predict_curl_inference_service  # noqa: E501

        Read the specified Inference Service predict curl  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_predict_curl_inference_service_with_http_info(name, namespace, prediction, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param object prediction: Prediction (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'prediction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_predict_curl_inference_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `read_predict_curl_inference_service`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `read_predict_curl_inference_service`")  # noqa: E501
        # verify the required parameter 'prediction' is set
        if ('prediction' not in params or
                params['prediction'] is None):
            raise ValueError("Missing the required parameter `prediction` when calling `read_predict_curl_inference_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'prediction' in params:
            body_params = params['prediction']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespace}/inferenceservices/{name}/predictcurl', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_predict_curl_seldon_deployment(self, name, namespace, prediction, **kwargs):  # noqa: E501
        """read_predict_curl_seldon_deployment  # noqa: E501

        Read the specified Seldon Deployment predict curl  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_predict_curl_seldon_deployment(name, namespace, prediction, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param object prediction: Prediction (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_predict_curl_seldon_deployment_with_http_info(name, namespace, prediction, **kwargs)  # noqa: E501
        else:
            (data) = self.read_predict_curl_seldon_deployment_with_http_info(name, namespace, prediction, **kwargs)  # noqa: E501
            return data

    def read_predict_curl_seldon_deployment_with_http_info(self, name, namespace, prediction, **kwargs):  # noqa: E501
        """read_predict_curl_seldon_deployment  # noqa: E501

        Read the specified Seldon Deployment predict curl  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_predict_curl_seldon_deployment_with_http_info(name, namespace, prediction, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name identifies a resource (required)
        :param str namespace: Namespace provides a logical grouping of resources (required)
        :param object prediction: Prediction (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'namespace', 'prediction']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_predict_curl_seldon_deployment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `read_predict_curl_seldon_deployment`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `read_predict_curl_seldon_deployment`")  # noqa: E501
        # verify the required parameter 'prediction' is set
        if ('prediction' not in params or
                params['prediction'] is None):
            raise ValueError("Missing the required parameter `prediction` when calling `read_predict_curl_seldon_deployment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'prediction' in params:
            body_params = params['prediction']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespace}/seldondeployments/{name}/predictcurl', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
