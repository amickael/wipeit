# Wipeit!
A small CLI to purge your Reddit history.

[![Release](https://github.com/amickael/wipeit/actions/workflows/python-publish.yml/badge.svg)](https://github.com/amickael/wipeit/actions/workflows/python-publish.yml)
[![PyPI](https://img.shields.io/pypi/v/wipeit?color=blue)](https://pypi.org/project/wipeit/)
[![Code style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)


![wipeit](https://repository-images.githubusercontent.com/365859955/17783580-b1d0-11eb-9738-6d2bc92644e6)

## 👶 Dependencies
* [Python 3.6 or higher](https://www.python.org/downloads/)

## 🛠️ Installation
Install from PyPI using `pip`, you may need to use `pip3` depending on your installation:
```sh
pip install wipeit
```

## 🚀 Usage
**wipeit** is a command-line program to purge your Reddit history. It requires a Python interpreter version 3.6+.

The following command will purge the last 30 days of comment and submission history, and will additionally overwrite the content with a random string before deletion:
```sh
wipeit -d 30 -sco
```


## ⚙️ Options
```
--version                 Show the version and exit.
-d, --days INTEGER RANGE  Number of days worth of content to delete.
                          Defaults to 365.

-f, --from TEXT           Date relative to --days, in ISO format (YYYY-MM-
                          DD). Defaults to today.

-c, --comments            Delete comments.
-s, --submissions         Delete submissions.
-o, --overwrite           Overwrite content with random text before
                          deletion.

--help                    Show help message and exit.
```

## ⚖️ License
[MIT © 2021 Andrew Mickael](https://github.com/amickael/wipeit/blob/master/LICENSE)
