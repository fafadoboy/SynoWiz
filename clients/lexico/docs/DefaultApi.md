# swagger_client.DefaultApi

All URIs are relative to *http://localhost/lexico/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**words_get**](DefaultApi.md#words_get) | **GET** /words | List all words
[**words_post**](DefaultApi.md#words_post) | **POST** /words | Create a new word
[**words_word_id_get**](DefaultApi.md#words_word_id_get) | **GET** /words/{wordID} | Get a word by ID
[**words_word_id_patch**](DefaultApi.md#words_word_id_patch) | **PATCH** /words/{wordID} | Update a word by ID


# **words_get**
> InlineResponse200 words_get(page=page, page_size=page_size)

List all words

Retrieve a paginated list of all words

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
page = 1 # int | Page number of the word list (optional) (default to 1)
page_size = 10 # int | Number of words per page (optional) (default to 10)

try: 
    # List all words
    api_response = api_instance.words_get(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->words_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of the word list | [optional] [default to 1]
 **page_size** | **int**| Number of words per page | [optional] [default to 10]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **words_post**
> words_post(word)

Create a new word

Add a new word to the lexico

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
word = swagger_client.Word() # Word | Word to add

try: 
    # Create a new word
    api_instance.words_post(word)
except ApiException as e:
    print "Exception when calling DefaultApi->words_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **word** | [**Word**](Word.md)| Word to add | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **words_word_id_get**
> Word words_word_id_get(word_id)

Get a word by ID

Retrieve a word by its unique ID

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
word_id = 'word_id_example' # str | Unique ID of the word

try: 
    # Get a word by ID
    api_response = api_instance.words_word_id_get(word_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->words_word_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **word_id** | **str**| Unique ID of the word | 

### Return type

[**Word**](Word.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **words_word_id_patch**
> words_word_id_patch(word_id, word_update)

Update a word by ID

Update the details of a word by its unique ID

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
word_id = 'word_id_example' # str | Unique ID of the word to update
word_update = swagger_client.WordUpdate() # WordUpdate | Word attributes to update

try: 
    # Update a word by ID
    api_instance.words_word_id_patch(word_id, word_update)
except ApiException as e:
    print "Exception when calling DefaultApi->words_word_id_patch: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **word_id** | **str**| Unique ID of the word to update | 
 **word_update** | [**WordUpdate**](WordUpdate.md)| Word attributes to update | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

