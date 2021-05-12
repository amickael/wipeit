import click

from wipeit.command import wipe, login, logout


@click.group()
def cli():
    pass


cli.add_command(wipe)
cli.add_command(login)
cli.add_command(logout)


if __name__ == "__main__":
    cli()
