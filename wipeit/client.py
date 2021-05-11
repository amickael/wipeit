import os
import secrets
import socket
import webbrowser
from pathlib import Path
from typing import List

import praw
from praw.util.token_manager import FileTokenManager, BaseTokenManager

from wipeit import VERSION


class AuthorizedClient(praw.Reddit):
    client_id = "9thvo8KiLG6Xlw"
    redirect_uri = "http://localhost:8080"
    user_agent = f"wipeit:9thvo8KiLG6Xlw:{VERSION} (by /u/iPodAddict181)"

    @property
    def refresh_token_filename(self) -> str:
        base_path = os.path.join(Path.home(), ".wipeit")
        if not os.path.isdir(base_path):
            os.makedirs(base_path)
        return os.path.join(base_path, "refresh_token.txt")

    def __init__(self, scopes: List[str], duration: str = "permanent"):
        token_manager = self.get_token_manager()
        init_args = {
            "client_id": self.client_id,
            "client_secret": None,
            "redirect_uri": self.redirect_uri,
            "user_agent": self.user_agent,
            "token_manager": token_manager,
        }
        super().__init__(**init_args)
        if not token_manager:
            refresh_token = self.obtain_token(scopes, duration)
            if not refresh_token:
                raise ValueError("Authorization failed")
            self.__initialize_refresh_token_file(refresh_token)
            init_args["token_manager"] = self.get_token_manager()
            super().__init__(**init_args)

    def __initialize_refresh_token_file(self, refresh_token: str):
        if not os.path.isfile(self.refresh_token_filename):
            with open(self.refresh_token_filename, "w") as outfile:
                outfile.write(refresh_token)

    def get_token_manager(self) -> (BaseTokenManager, None):
        if not os.path.isfile(self.refresh_token_filename):
            return None
        return FileTokenManager(self.refresh_token_filename)

    @staticmethod
    def __receive_connection() -> socket.socket:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("localhost", 8080))
        server.listen(1)
        client = server.accept()[0]
        server.close()
        return client

    @staticmethod
    def __send_message(client: socket.socket, message: str):
        client.send(f"HTTP/1.1 200 OK\r\n\r\n{message}".encode("utf-8"))
        client.close()

    def obtain_token(
        self,
        scopes: List[str] = None,
        duration: str = "permanent",
    ) -> (str, None):
        # Set default scope, add identity if not provided
        if not scopes:
            scopes = ["identity"]
        elif "identity" not in scopes:
            scopes.append("identity")

        # Generate state and request from browser
        state = secrets.token_urlsafe()
        url = self.auth.url(scopes, state, duration)
        webbrowser.open_new(url)

        # Open connection and parse response
        client = self.__receive_connection()
        data = client.recv(1024).decode("utf-8")
        param_tokens = data.split(" ", 2)[1].split("?", 1)[1].split("&")
        params = {
            key: value for (key, value) in [token.split("=") for token in param_tokens]
        }
        if state != params["state"]:
            self.__send_message(
                client,
                f"State mismatch. Expected: {state} Received: {params['state']}",
            )
            return None
        elif "error" in params:
            self.__send_message(client, params["error"])
            return None

        # Exchange for refresh token and return
        refresh_token = self.auth.authorize(params["code"])
        self.__send_message(
            client,
            f"Successfully authenticated as /u/{self.user.me()}, you may now close this window.",
        )
        return refresh_token
