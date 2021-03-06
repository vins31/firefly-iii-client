# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from firefly_iii_client.api_client import ApiClient


class TagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_tag(self, tag, **kwargs):  # noqa: E501
        """Delete an tag.  # noqa: E501

        Delete an tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tag(tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag: Either the tag itself or the tag ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_tag_with_http_info(tag, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_tag_with_http_info(tag, **kwargs)  # noqa: E501
            return data

    def delete_tag_with_http_info(self, tag, **kwargs):  # noqa: E501
        """Delete an tag.  # noqa: E501

        Delete an tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tag_with_http_info(tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag: Either the tag itself or the tag ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tag" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in local_var_params or
                local_var_params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `delete_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tags/{tag}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tag(self, tag, **kwargs):  # noqa: E501
        """Get a single tag.  # noqa: E501

        Get a single tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tag(tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag: Either the tag itself or the tag ID. (required)
        :param int page: Page number
        :return: TagSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tag_with_http_info(tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tag_with_http_info(tag, **kwargs)  # noqa: E501
            return data

    def get_tag_with_http_info(self, tag, **kwargs):  # noqa: E501
        """Get a single tag.  # noqa: E501

        Get a single tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tag_with_http_info(tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag: Either the tag itself or the tag ID. (required)
        :param int page: Page number
        :return: TagSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tag', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tag" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in local_var_params or
                local_var_params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `get_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']  # noqa: E501

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tags/{tag}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagSingle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tags(self, **kwargs):  # noqa: E501
        """List all tags.  # noqa: E501

        List all of the user's tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tags(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number
        :return: TagArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tags_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_tags_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_tags_with_http_info(self, **kwargs):  # noqa: E501
        """List all tags.  # noqa: E501

        List all of the user's tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tags_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number
        :return: TagArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tags" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transactions_by_tag(self, tag, **kwargs):  # noqa: E501
        """List all transactions with this tag.  # noqa: E501

        List all transactions with this tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_by_tag(tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag: Either the tag itself or the tag ID. (required)
        :param int page: Page number. The default pagination is 50.
        :param str start: A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive). 
        :param str end: A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive). 
        :param str type: Optional filter on the transaction type(s) returned.
        :return: TransactionArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transactions_by_tag_with_http_info(tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transactions_by_tag_with_http_info(tag, **kwargs)  # noqa: E501
            return data

    def get_transactions_by_tag_with_http_info(self, tag, **kwargs):  # noqa: E501
        """List all transactions with this tag.  # noqa: E501

        List all transactions with this tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_by_tag_with_http_info(tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag: Either the tag itself or the tag ID. (required)
        :param int page: Page number. The default pagination is 50.
        :param str start: A date formatted YYYY-MM-DD. This is the start date of the selected range (inclusive). 
        :param str end: A date formatted YYYY-MM-DD. This is the end date of the selected range (inclusive). 
        :param str type: Optional filter on the transaction type(s) returned.
        :return: TransactionArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tag', 'page', 'start', 'end', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions_by_tag" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in local_var_params or
                local_var_params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `get_transactions_by_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']  # noqa: E501

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tags/{tag}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def store_tag(self, tag_update, **kwargs):  # noqa: E501
        """Store a new tag  # noqa: E501

        Creates a new tag. The data required can be submitted as a JSON body or as a list of parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_tag(tag_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagUpdate tag_update: JSON array or key=value pairs with the necessary tag information. See the model for the exact specifications. (required)
        :return: TagSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.store_tag_with_http_info(tag_update, **kwargs)  # noqa: E501
        else:
            (data) = self.store_tag_with_http_info(tag_update, **kwargs)  # noqa: E501
            return data

    def store_tag_with_http_info(self, tag_update, **kwargs):  # noqa: E501
        """Store a new tag  # noqa: E501

        Creates a new tag. The data required can be submitted as a JSON body or as a list of parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.store_tag_with_http_info(tag_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagUpdate tag_update: JSON array or key=value pairs with the necessary tag information. See the model for the exact specifications. (required)
        :return: TagSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tag_update']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method store_tag" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag_update' is set
        if ('tag_update' not in local_var_params or
                local_var_params['tag_update'] is None):
            raise ValueError("Missing the required parameter `tag_update` when calling `store_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tag_update' in local_var_params:
            body_params = local_var_params['tag_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tags', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagSingle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_tag(self, tag, tag_update, **kwargs):  # noqa: E501
        """Update existing tag.  # noqa: E501

        Update existing tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tag(tag, tag_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag: Either the tag itself or the tag ID. (required)
        :param TagUpdate tag_update: JSON array with updated tag information. See the model for the exact specifications. (required)
        :return: TagSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_tag_with_http_info(tag, tag_update, **kwargs)  # noqa: E501
        else:
            (data) = self.update_tag_with_http_info(tag, tag_update, **kwargs)  # noqa: E501
            return data

    def update_tag_with_http_info(self, tag, tag_update, **kwargs):  # noqa: E501
        """Update existing tag.  # noqa: E501

        Update existing tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tag_with_http_info(tag, tag_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag: Either the tag itself or the tag ID. (required)
        :param TagUpdate tag_update: JSON array with updated tag information. See the model for the exact specifications. (required)
        :return: TagSingle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tag', 'tag_update']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_tag" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in local_var_params or
                local_var_params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `update_tag`")  # noqa: E501
        # verify the required parameter 'tag_update' is set
        if ('tag_update' not in local_var_params or
                local_var_params['tag_update'] is None):
            raise ValueError("Missing the required parameter `tag_update` when calling `update_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tag_update' in local_var_params:
            body_params = local_var_params['tag_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['firefly_iii_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/tags/{tag}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagSingle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
