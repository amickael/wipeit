import datetime as dt

from wipeit.client import AuthorizedClient
from wipeit.history import SubmissionHistory


if __name__ == "__main__":
    history = SubmissionHistory(AuthorizedClient(["identity", "edit", "history"]))
    for i in history.filter_by_date(dt.datetime.now() - dt.timedelta(weeks=52)):
        print(i.shortlink)
