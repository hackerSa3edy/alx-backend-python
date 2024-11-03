#!/usr/bin/env python3
"""A GitHub org client
"""
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class GithubOrgClient:
    """A client to interact with GitHub organization data.

    Attributes:
        ORG_URL (str): The URL template for GitHub organization API.
        _org_name (str): The name of the GitHub organization.
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize the GithubOrgClient with the organization name.

        Args:
            org_name (str): The name of the GitHub organization.
        """
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Fetch and memoize the organization data from GitHub.

        Returns:
            Dict: The organization data.
        """
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Get the URL for the public repositories of the organization.

        Returns:
            str: The URL for the public repositories.
        """
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """Fetch and memoize the repositories payload from GitHub.

        Returns:
            Dict: The repositories payload.
        """
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """Get the list of public repositories optionally filtered by license.

        Args:
            license (str, optional): The license key to filter repositories.
            Defaults to None.

        Returns:
            List[str]: The list of public repository names.
        """
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]

        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Check if the repository has the specified license.

        Args:
            repo (Dict[str, Dict]): The repository data.
            license_key (str): The license key to check.

        Returns:
            bool: True if the repository has the specified license,
            False otherwise.
        """
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(
                repo,
                ("license", "key")
                ) == license_key
        except KeyError:
            return False
        return has_license
