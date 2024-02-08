from dataclasses import dataclass
from typing import Optional

from src.models.user import GithubUser


@dataclass
class Difference:
    i_dont_follow_them: list[GithubUser]
    they_dont_follow_me: list[GithubUser]
    mutual: list[GithubUser]

    i_dont_follow_them_count: Optional[int] = None
    they_dont_follow_me_count: Optional[int] = None
    mutual_count: Optional[int] = None
    total_count: Optional[int] = None

    def __post_init__(self):
        self.i_dont_follow_them_count = len(self.i_dont_follow_them)
        self.they_dont_follow_me_count = len(self.they_dont_follow_me)
        self.mutual_count = len(self.mutual)
        self.total_count = self.i_dont_follow_them_count + self.they_dont_follow_me_count + self.mutual_count

        # Sort the sets
        self.i_dont_follow_them = sorted(self.i_dont_follow_them, key=lambda x: x.username_lcase)
        self.they_dont_follow_me = sorted(self.they_dont_follow_me, key=lambda x: x.username_lcase)
        self.mutual = sorted(self.mutual, key=lambda x: x.username_lcase)
