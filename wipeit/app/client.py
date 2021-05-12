from wipeit import CONFIG, VERSION
from wipeit.models import AuthorizedClient


class AppClient(AuthorizedClient):
    client_id = CONFIG.client_id
    redirect_uri = CONFIG.redirect_uri
    user_agent = f"wipeit:{client_id}:{VERSION} (by /u/{CONFIG.author})"
