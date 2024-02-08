from src.controllers import (
    compare,
    mutual,
)
from src.utils import get_args_params


def main():
    params = get_args_params()
    is_single_user = params.get("username")
    if is_single_user:
        compare(
            username=params["username"],
            list_organizations=params.get("list_organizations", False),
        )
    else:
        mutual(
            x_user=params["x_user"],
            y_user=params["y_user"],
        )


if __name__ == "__main__":
    main()
