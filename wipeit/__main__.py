import click

from wipeit import VERSION
from wipeit.commands import wipe, login, logout


@click.group()
@click.version_option(VERSION)
def cli():
    pass


cli.add_command(wipe)
cli.add_command(login)
cli.add_command(logout)


if __name__ == "__main__":
    cli()
