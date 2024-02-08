import os

from src.repositories import GitHubRepository
from src.services import (
    get_mutual_connections,
    print_mutual_connections_as_table,
)


MY_GITHUB_TOKEN = os.environ.get("MY_GITHUB_TOKEN")


def mutual(x_user: str, y_user: str) -> None:
    x_user_data = GitHubRepository.fetch_all(x_user, token=MY_GITHUB_TOKEN)
    y_user_data = GitHubRepository.fetch_all(y_user, token=MY_GITHUB_TOKEN)
    mutual_connection = get_mutual_connections(x_user_data, y_user_data)
    print_mutual_connections_as_table(mutual_connection)
