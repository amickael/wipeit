import os

from pkg_resources import get_distribution

import yaml

from .models.config import AppConfig

########################################################################################################################
# Get version
########################################################################################################################
VERSION = get_distribution("wipeit").version

########################################################################################################################
# Load config
########################################################################################################################
base_path = os.path.dirname(__file__)
with open(os.path.join(base_path, "config.yaml")) as stream:
    _config = yaml.safe_load(stream)


CONFIG = AppConfig(**_config)
