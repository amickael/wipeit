import datetime as dt

from wipeit.client import AuthorizedClient
from wipeit.history import CommentHistory


if __name__ == "__main__":
    client = AuthorizedClient(["identity", "edit", "history"])
    history = CommentHistory(client)
    start_dt = dt.datetime.now() - dt.timedelta(weeks=52)
    end_dt = dt.datetime.now() - dt.timedelta(weeks=2)
    for item in history.filter_by_date():
        print(item)
