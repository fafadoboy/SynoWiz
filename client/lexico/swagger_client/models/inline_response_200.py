# coding: utf-8

"""
    Lexico Service

    API for managing words in the lexico service

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class InlineResponse200(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, current_page=None, page_size=None, total_pages=None, total_words=None, words=None):
        """
        InlineResponse200 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'current_page': 'int',
            'page_size': 'int',
            'total_pages': 'int',
            'total_words': 'int',
            'words': 'list[Word]'
        }

        self.attribute_map = {
            'current_page': 'currentPage',
            'page_size': 'pageSize',
            'total_pages': 'totalPages',
            'total_words': 'totalWords',
            'words': 'words'
        }

        self._current_page = current_page
        self._page_size = page_size
        self._total_pages = total_pages
        self._total_words = total_words
        self._words = words

    @property
    def current_page(self):
        """
        Gets the current_page of this InlineResponse200.


        :return: The current_page of this InlineResponse200.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """
        Sets the current_page of this InlineResponse200.


        :param current_page: The current_page of this InlineResponse200.
        :type: int
        """

        self._current_page = current_page

    @property
    def page_size(self):
        """
        Gets the page_size of this InlineResponse200.


        :return: The page_size of this InlineResponse200.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this InlineResponse200.


        :param page_size: The page_size of this InlineResponse200.
        :type: int
        """

        self._page_size = page_size

    @property
    def total_pages(self):
        """
        Gets the total_pages of this InlineResponse200.


        :return: The total_pages of this InlineResponse200.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """
        Sets the total_pages of this InlineResponse200.


        :param total_pages: The total_pages of this InlineResponse200.
        :type: int
        """

        self._total_pages = total_pages

    @property
    def total_words(self):
        """
        Gets the total_words of this InlineResponse200.


        :return: The total_words of this InlineResponse200.
        :rtype: int
        """
        return self._total_words

    @total_words.setter
    def total_words(self, total_words):
        """
        Sets the total_words of this InlineResponse200.


        :param total_words: The total_words of this InlineResponse200.
        :type: int
        """

        self._total_words = total_words

    @property
    def words(self):
        """
        Gets the words of this InlineResponse200.


        :return: The words of this InlineResponse200.
        :rtype: list[Word]
        """
        return self._words

    @words.setter
    def words(self, words):
        """
        Sets the words of this InlineResponse200.


        :param words: The words of this InlineResponse200.
        :type: list[Word]
        """

        self._words = words

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
