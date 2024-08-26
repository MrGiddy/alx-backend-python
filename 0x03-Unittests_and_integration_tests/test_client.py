#!/usr/bin/env python3
"""Tests for client module"""
from typing import Dict
import unittest
from unittest.mock import Mock, PropertyMock, patch, MagicMock

from requests import HTTPError
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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

    def test_public_repos_url(self) -> None:
        """tests the `_public_repos_url` property of GithubOrgClient"""
        with patch(
                'client.GithubOrgClient.org', new_callable=PropertyMock
                ) as mocked_org:
            mocked_org.return_value = {
                'login': 'test-org',
                'repos_url': 'https://api.github.com/orgs/test-org/repos'
            }

            test_org = GithubOrgClient('test-org')
            result = test_org._public_repos_url

            expected_url = 'https://api.github.com/orgs/test-org/repos'
            self.assertEqual(result, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json: MagicMock) -> None:
        """test the `public_repos` method of GithubOrgClient"""
        mock_response = [
            {'id': 123, 'name': 'drumkit-wp'},
            {'id': 456, 'name': 'car-trumps'},
            {'id': 789, 'name': 'nfc-talk'}
        ]
        mocked_get_json.return_value = mock_response

        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock
                ) as mocked_public_repos_url:
            mock_url = 'https://api.github.com/orgs/test-org/repos'
            mocked_public_repos_url.return_value = mock_url

            test_org = GithubOrgClient('test-org')
            result = test_org.public_repos()

            self.assertEqual(result, ['drumkit-wp', 'car-trumps', 'nfc-talk'])
            mocked_public_repos_url.assert_called_once()

        mocked_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """test `has_license` method of GithubOrgClient"""
        test_org = GithubOrgClient('test-org')
        result = test_org.has_license(repo, key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Implements integration tests for GithubOrgClient"""
    @classmethod
    def setUpClass(cls) -> None:
        """sets up class fixtures before integration tests"""
        # mapping urls to their corresponding payloads
        payloads = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def side_effect(url):
            if url in payloads:
                return Mock(json=payloads.get(url))
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=side_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """tears down class fixtures after integration tests"""
        cls.get_patcher.stop()
