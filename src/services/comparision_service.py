from src.models import (
    Difference,
    UserData,
)


def compare_followers_following(user_data: UserData, list_organizations=False) -> Difference:
    """
    Compares the list of followers and following to identify differences.

    :param user_data: A user data object containing the user's followers and following
    :type user_data: UserData
    :param list_organizations: Whether to include organizations in the comparison
    :type list_organizations: bool
    :return: A Difference object containing the differences
    """

    if list_organizations:
        followers_set = {follower.username for follower in user_data.followers}
        following_set = {followed.username for followed in user_data.following}
    else:
        followers_set = {follower.username for follower in user_data.followers if follower._type == "User"}
        following_set = {followed.username for followed in user_data.following if followed._type == "User"}

    i_dont_follow_them = followers_set.difference(following_set)
    they_dont_follow_me = following_set.difference(followers_set)
    mutual = followers_set.intersection(following_set)

    i_dont_follow_them_users = [follower for follower in user_data.followers if follower.username in i_dont_follow_them]
    they_dont_follow_me_users = [
        followed for followed in user_data.following if followed.username in they_dont_follow_me
    ]
    mutual_users = [user for user in user_data.followers if user.username in mutual]

    difference = Difference(i_dont_follow_them_users, they_dont_follow_me_users, mutual_users)
    return difference
