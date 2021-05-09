from wipeit.client import AuthorizedClient


reddit = AuthorizedClient(["identity", "edit", "history"])
for item in reddit.user.me().comments.new():
    print(item.body)
