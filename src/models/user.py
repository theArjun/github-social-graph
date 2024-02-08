from dataclasses import dataclass
from typing import (
    Any,
    List,
    Optional,
    Type,
    TypeVar,
    cast,
)


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class GithubUser:
    username: str
    _id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    _type: str
    site_admin: bool

    # Custom props
    username_lcase: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "GithubUser":
        assert isinstance(obj, dict)
        username = from_str(obj.get("login"))
        _id = from_int(obj.get("id"))
        node_id = from_str(obj.get("node_id"))
        avatar_url = from_str(obj.get("avatar_url"))
        gravatar_id = from_str(obj.get("gravatar_id"))
        url = from_str(obj.get("url"))
        html_url = from_str(obj.get("html_url"))
        followers_url = from_str(obj.get("followers_url"))
        following_url = from_str(obj.get("following_url"))
        gists_url = from_str(obj.get("gists_url"))
        starred_url = from_str(obj.get("starred_url"))
        subscriptions_url = from_str(obj.get("subscriptions_url"))
        organizations_url = from_str(obj.get("organizations_url"))
        repos_url = from_str(obj.get("repos_url"))
        events_url = from_str(obj.get("events_url"))
        received_events_url = from_str(obj.get("received_events_url"))
        _type = from_str(obj.get("type"))
        site_admin = from_bool(obj.get("site_admin"))
        return GithubUser(
            username,
            _id,
            node_id,
            avatar_url,
            gravatar_id,
            url,
            html_url,
            followers_url,
            following_url,
            gists_url,
            starred_url,
            subscriptions_url,
            organizations_url,
            repos_url,
            events_url,
            received_events_url,
            _type,
            site_admin,
        )

    def __post_init__(self):
        self.username_lcase = self.username.lower()

    @classmethod
    def from_dict_list(cls, users_list: list[dict]) -> List["GithubUser"]:
        return [GithubUser.from_dict(x) for x in users_list]


@dataclass(frozen=True)
class UserData:
    username: str
    followers: List[GithubUser]
    following: List[GithubUser]
