from dataclasses import (
    asdict,
    is_dataclass,
)
from typing import List

from tabulate import tabulate

from src.models import (
    Difference,
    GithubUser,
    MutualConnection,
)


VALID_HEADERS = [
    "username",
    "html_url",
]


def print_gh_users_as_table(instances: List[GithubUser]):
    """
    Displays the attributes of dataclass instances in a table format.

    :param instances: A list of dataclass instances to be displayed.
    """
    if not instances:
        print("No data to display.")
        return

    # Check if the input is indeed a list of dataclass instances
    if not all(is_dataclass(instance) for instance in instances):
        print("Error: All items must be instances of a dataclass.")
        return

    # Convert dataclass instances to dictionaries
    data = [asdict(instance) for instance in instances]

    table_data = [[data[i][header] for header in VALID_HEADERS] for i in range(len(data))]

    # Use tabulate to display the data
    table = tabulate(table_data, headers=VALID_HEADERS, tablefmt="grid", numalign="center")
    print(table)


def print_difference_as_table(username: str, difference: Difference):
    print(f"\n\nPeople who {username} don't follow back ({difference.i_dont_follow_them_count}):")
    print_gh_users_as_table(difference.i_dont_follow_them)

    print(f"\n\n People who don't follow {username} back ({difference.they_dont_follow_me_count}):")
    print_gh_users_as_table(difference.they_dont_follow_me)

    print(f"\n\n Mutual followers for {username} ({difference.mutual_count}):")
    print_gh_users_as_table(difference.mutual)


def print_mutual_connections_as_table(mutual_connection: MutualConnection):
    print(f"\n\nPeople who ({mutual_connection.x_user}, {mutual_connection.y_user}) both follow:")
    print_gh_users_as_table(mutual_connection.we_both_follow)

    print(f"\n\nPeople who ({mutual_connection.x_user}, {mutual_connection.y_user}) both get followed by:")
    print_gh_users_as_table(mutual_connection.we_both_get_followed_by)
