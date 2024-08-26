#!/usr/bin/env python3
"""Tests for client module"""
import unittest
from unittest.mock import Mock, patch, MagicMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Implements unit tests for the client module"""
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mocked_get_json: MagicMock) -> None:
        """tests the `org` method of GithubOrgClient"""
        mock_response = {
                'login': 'test-org',
                'repos_url': 'https://api.github.com/orgs/test-org/repos'
            }
        mocked_get_json.return_value = mock_response

        test_org = GithubOrgClient(org_name)
        result = test_org.org

        expected_url = f'https://api.github.com/orgs/{org_name}'
        mocked_get_json.assert_called_once_with(expected_url)

        self.assertEqual(result, mock_response)
