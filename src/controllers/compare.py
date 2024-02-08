import os

from src.repositories import GitHubRepository
from src.services import (
    compare_followers_following,
    print_difference_as_table,
)


MY_GITHUB_TOKEN = os.environ.get("MY_GITHUB_TOKEN")


def compare(username: str, list_organizations=bool) -> None:
    user_data = GitHubRepository.fetch_all(username, token=MY_GITHUB_TOKEN)
    difference = compare_followers_following(user_data, list_organizations)
    print_difference_as_table(username, difference)
    print(f"Total followers for {username}: {len(user_data.followers)}")
    print(f"Total following {username}: {len(user_data.following)}")
