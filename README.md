# Wipeit!
A small CLI to purge your Reddit history.

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
