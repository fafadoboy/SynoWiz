# swagger_client.DefaultApi

All URIs are relative to *http://localhost/practice/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executions_get**](DefaultApi.md#executions_get) | **GET** /executions | List all practice executions
[**executions_post**](DefaultApi.md#executions_post) | **POST** /executions | Record a new practice execution
[**sets_get**](DefaultApi.md#sets_get) | **GET** /sets | List all practice sets
[**sets_post**](DefaultApi.md#sets_post) | **POST** /sets | Create a new practice set


# **executions_get**
> list[PracticeExecution] executions_get()

List all practice executions

Retrieve a list of all practice executions

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    # List all practice executions
    api_response = api_instance.executions_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->executions_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PracticeExecution]**](PracticeExecution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **executions_post**
> executions_post(practice_execution)

Record a new practice execution

Record the results of a new practice execution

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
practice_execution = swagger_client.PracticeExecution() # PracticeExecution | The practice execution to record

try: 
    # Record a new practice execution
    api_instance.executions_post(practice_execution)
except ApiException as e:
    print "Exception when calling DefaultApi->executions_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **practice_execution** | [**PracticeExecution**](PracticeExecution.md)| The practice execution to record | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sets_get**
> list[PracticeSet] sets_get()

List all practice sets

Retrieve a list of all practice sets

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    # List all practice sets
    api_response = api_instance.sets_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->sets_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PracticeSet]**](PracticeSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sets_post**
> sets_post(practice_set)

Create a new practice set

Create a new practice set

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
practice_set = swagger_client.PracticeSet() # PracticeSet | The practice set to create

try: 
    # Create a new practice set
    api_instance.sets_post(practice_set)
except ApiException as e:
    print "Exception when calling DefaultApi->sets_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **practice_set** | [**PracticeSet**](PracticeSet.md)| The practice set to create | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

