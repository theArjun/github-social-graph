from functools import lru_cache
from typing import (
    List,
    Optional,
)

from src.models import (
    GithubUser,
    UserData,
)
from src.utils import get_github_api


PAGE_SIZE = 100


class GitHubRepository:
    @staticmethod
    @lru_cache
    def fetch_followers(username: str, token: Optional[str]) -> List[str]:
        """
        Fetches the followers of a given GitHub user.

        :param username: GitHub username
        :return: List of follower usernames
        :param token: GitHub Token
        :type token: Optional[str]
        """
        followers = []
        page = 1
        while True:
            followers_url = f"https://api.github.com/users/{username}/followers?page={page}&per_page={PAGE_SIZE}"
            page_data = get_github_api(followers_url, token=token)
            if not page_data:
                break
            follower_users = GithubUser.from_dict_list(page_data)
            followers.extend(follower_users)
            if len(page_data) < PAGE_SIZE:
                break
            page += 1
        return followers

    @staticmethod
    @lru_cache
    def fetch_following(username: str, token: Optional[str]) -> List[str]:
        """
        Fetches the users a given GitHub user is following.

        :param username: GitHub username
        :type username: str
        :param token: GitHub Token
        :type token: Optional[str]
        :return: List of usernames the user is following
        """
        following = []
        page = 1
        while True:
            following_url = f"https://api.github.com/users/{username}/following?page={page}&per_page={PAGE_SIZE}"
            page_data = get_github_api(following_url, token=token)
            if not page_data:
                break
            following_users = GithubUser.from_dict_list(page_data)
            following.extend(following_users)
            if len(page_data) < PAGE_SIZE:
                break
            page += 1
        return following

    @staticmethod
    def fetch_all(username: str, token: Optional[str]) -> UserData:
        followers = GitHubRepository.fetch_followers(username, token)
        following = GitHubRepository.fetch_following(username, token)
        return UserData(username, followers, following)
