import datetime as dt

from wipeit.client import AuthorizedClient


reddit = AuthorizedClient(["identity", "edit", "history"])
user = reddit.user.me()
comments = user.comments.new()
for comment in comments:
    print(dt.datetime.fromtimestamp(comment.created))
