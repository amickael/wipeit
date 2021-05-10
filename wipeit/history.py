from abc import ABC, abstractmethod
import datetime as dt
from typing import Iterable, TypeVar, Generic

from praw.models import Comment, Submission, ListingGenerator

from wipeit.client import AuthorizedClient

T = TypeVar("T")


class BaseHistory(ABC, Generic[T]):
    def __init__(self, client: AuthorizedClient):
        self.client = client
        self.user = self.client.user.me()

    @property
    @abstractmethod
    def history(self) -> ListingGenerator:
        raise NotImplementedError("Property 'history' must be defined.")

    def filter_by_date(
        self, start_dt: dt.datetime, end_dt: dt.datetime = None
    ) -> Iterable[T]:
        if not end_dt:
            end_dt = dt.datetime.now()
        start_ts, end_ts = [start_dt.timestamp(), end_dt.timestamp()]
        return [item for item in self.history if start_ts <= item.created <= end_ts]


class CommentHistory(BaseHistory[Comment]):
    @property
    def history(self) -> ListingGenerator:
        return self.user.comments.new()


class SubmissionHistory(BaseHistory[Submission]):
    @property
    def history(self) -> ListingGenerator:
        return self.user.submissions.new()
