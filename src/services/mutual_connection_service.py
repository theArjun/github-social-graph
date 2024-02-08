from src.models import (
    MutualConnection,
    UserData,
)


def get_mutual_connections(x_user: UserData, y_user: UserData) -> MutualConnection:
    """
    Get mutual connections between two users.

    :param x_user: A UserData object for the first user
    :param y_user: A UserData object for the second user
    :return: A MutualConnection object containing the mutual connections
    """

    x_followers_set = {follower.username for follower in x_user.followers}
    y_followers_set = {follower.username for follower in y_user.followers}

    x_following_set = {followed.username for followed in x_user.following}
    y_following_set = {followed.username for followed in y_user.following}

    we_both_follow = x_following_set.intersection(y_following_set)
    we_both_get_followed_by = x_followers_set.intersection(y_followers_set)

    we_both_follow_users = [follower for follower in x_user.followers if follower.username in we_both_follow]

    we_both_get_followed_by_users = [
        followed for followed in x_user.following if followed.username in we_both_get_followed_by
    ]

    return MutualConnection(
        x_user=x_user.username,
        y_user=y_user.username,
        we_both_follow=we_both_follow_users,
        we_both_get_followed_by=we_both_get_followed_by_users,
    )
