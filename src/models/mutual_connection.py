from dataclasses import dataclass
from typing import Optional

from src.models.user import GithubUser


@dataclass
class MutualConnection:
    x_user: str
    y_user: str

    we_both_follow: list[GithubUser]
    we_both_get_followed_by: list[GithubUser]

    we_both_follow_count: Optional[int] = None
    we_both_get_followed_by_count: Optional[int] = None

    def __post_init__(self):
        self.we_both_follow_count = len(self.we_both_follow)
        self.we_both_get_followed_by_count = len(self.we_both_get_followed_by)

        self.we_both_follow = sorted(self.we_both_follow, key=lambda x: x.username_lcase)
        self.we_both_get_followed_by = sorted(self.we_both_get_followed_by, key=lambda x: x.username_lcase)
