#!/usr/bin/env python3
"""Unit testing for client module"""

import unittest
from typing import Dict
from unittest.mock import patch, Mock, PropertyMock

from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing GithubOrgClient methods"""

    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get: Mock):
        """Test that GithubOrgClient.org returns the correct payload"""
        payload: Dict[str, str] = {"org_name": org_name}

        mock_get.return_value = lambda: payload
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org(), payload)
        mock_get.assert_called_once()

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url returns the correct URL
        """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            url = "https://google.com"
            mock_org.return_value = {"repos_url": url}

            github_org_client = GithubOrgClient("google")
            self.assertEqual(github_org_client._public_repos_url, url)

    @patch('client.get_json')
    def test_public_repos(self, get_mock):
        """
        Test that GithubOrgClient.public_repos returns the correct
        list of repositories
        """
        get_mock.return_value = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "Apache"}}
        ]

        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as repos_mock:
            repos_mock.return_value = "mocked_repos_url"

            github_client = GithubOrgClient("mocked_repos_url")
            self.assertEqual(github_client.public_repos(license="MIT"),
                             ["repo1"])
            get_mock.assert_called_once()
            repos_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, result):
        """
        Test that GithubOrgClient.has_license returns the correct
        boolean value
        """
        github_client = GithubOrgClient("org_name")
        self.assertEqual(github_client.has_license(repo, license), result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class for Integration test of fixtures"""

    @classmethod
    def setUpClass(cls):
        """A class method called before tests in an individual class are run"""
        config = {
            "return_value.json.side_effect": [
                cls.org_payload,
                cls.repos_payload,
                cls.org_payload,
                cls.repos_payload,
            ]
        }
        cls.get_patcher = patch("requests.get", **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """Integration test: public repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for public repos with License"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests in an individual class have run"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
