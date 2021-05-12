import click

from wipeit.client import AuthorizedClient
from .const import SCOPES


@click.command()
def login(*args, **kwargs):
    try:
        client = AuthorizedClient(SCOPES)
    except ValueError:
        click.echo(
            "Authorization failed. You must allow Reddit permissions for wipeit to function."
        )
        retry = click.confirm("Retry?", default=True)
        if retry:
            try:
                client = AuthorizedClient(SCOPES)
            except ValueError:
                click.echo("Authorization failed, aborting.")
                raise click.Abort
        else:
            raise click.Abort
    click.echo(f"Successfully authenticated as /u/{client.user.me().name}")
    click.echo("")
