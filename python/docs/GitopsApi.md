# seldon_deploy_client.GitopsApi

All URIs are relative to *https://X.X.X.X/seldon-deploy/api/v1alpha1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_git_ops_status**](GitopsApi.md#read_git_ops_status) | **GET** /namespaces/{namespace}/gitops-status | 


# **read_git_ops_status**
> object read_git_ops_status(namespace)



Read the GitOps status

### Example
```python
from __future__ import print_function
import time
import seldon_deploy_client
from seldon_deploy_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = seldon_deploy_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = seldon_deploy_client.GitopsApi(seldon_deploy_client.ApiClient(configuration))
namespace = 'namespace_example' # str | Namespace provides a logical grouping of resources

try:
    api_response = api_instance.read_git_ops_status(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitopsApi->read_git_ops_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace provides a logical grouping of resources | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
