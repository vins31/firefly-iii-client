# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import firefly_iii_client
from firefly_iii_client.api.import_api import ImportApi  # noqa: E501
from firefly_iii_client.rest import ApiException


class TestImportApi(unittest.TestCase):
    """ImportApi unit test stubs"""

    def setUp(self):
        self.api = firefly_iii_client.api.import_api.ImportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_import(self):
        """Test case for get_import

        Show info on a single import  # noqa: E501
        """
        pass

    def test_get_imports(self):
        """Test case for get_imports

        List al imports  # noqa: E501
        """
        pass

    def test_get_transactions_by_import(self):
        """Test case for get_transactions_by_import

        List all transactions related to the import job. The correlation is made through the tag.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()