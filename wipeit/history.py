from abc import ABC, abstractmethod
import datetime as dt
from typing import Iterable, TypeVar, Generic
import uuid

from praw.models import Comment, Submission, ListingGenerator
from praw.models.reddit.mixins import UserContentMixin

from wipeit.client import AuthorizedClient

T = TypeVar("T", bound=UserContentMixin)


class BaseHistory(ABC, Generic[T]):
    def __init__(self, client: AuthorizedClient):
        self.client = client
        self.user = self.client.user.me()

    @property
    @abstractmethod
    def history(self) -> ListingGenerator:
        raise NotImplementedError("Property 'history' must be defined.")

    def filter_by_date(
        self, start_dt: dt.datetime = None, end_dt: dt.datetime = None
    ) -> Iterable[T]:
        # Parse start timestamp, default to 0
        if start_dt:
            start_ts = start_dt.timestamp()
        else:
            start_ts = 0

        # Parse end timestamp, default to now
        if end_dt:
            end_ts = end_dt.timestamp()
        else:
            end_ts = dt.datetime.now().timestamp()

        # Iterate
        for item in self.history:
            if start_ts <= item.created <= end_ts:
                yield item

    def wipe(
        self,
        start_dt: dt.datetime = None,
        end_dt: dt.datetime = None,
        overwrite: bool = False,
    ) -> Iterable[T]:
        items = self.filter_by_date(start_dt, end_dt)
        for item in items:
            if overwrite:
                item.edit(uuid.uuid4().hex)
            item.delete()
            yield item


class CommentHistory(BaseHistory[Comment]):
    @property
    def history(self) -> ListingGenerator:
        return self.user.comments.new()


class SubmissionHistory(BaseHistory[Submission]):
    @property
    def history(self) -> ListingGenerator:
        return self.user.submissions.new()
