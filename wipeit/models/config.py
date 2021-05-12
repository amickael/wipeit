from dataclasses import dataclass
from typing import List


@dataclass
class AppConfig:
    scopes: List[str]
    client_id: str
    author: str
    redirect_uri: str
    app_name: str
