import argparse


def get_args_params() -> dict:
    parser = argparse.ArgumentParser(
        description="A CLI tool to know about GitHub social connections."
    )
    parser.add_argument(
        "-u",
        "--username",
        type=str,
        nargs=1,
        required=False,
        help="Username to compare followers and following. Example: --username octocat",
    )
    parser.add_argument(
        "--orgs",
        action="store_true",
        required=False,
        help="Include organizations in the comparison. Example: --orgs",
    )
    parser.add_argument(
        "--users",
        type=str,
        nargs=2,
        required=False,
        help="Two users to compare mutual connections. Example: --users octocat hubot",
    )

    args = parser.parse_args()
    username = args.username[0] if args.username else None
    list_organizations = args.orgs
    users = args.users

    params = {"is_single_user": False}
    if username:
        params |= {
            "username": username,
            "list_organizations": list_organizations,
            "is_single_user": True,
        }

    elif users:
        x_user, y_user = users
        params |= {"x_user": x_user, "y_user": y_user}

    return params
