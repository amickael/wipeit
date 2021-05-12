import click

from wipeit import CONFIG
from wipeit.app import AppClient


@click.command()
def login(*args, **kwargs):
    """Authorize wipeit with a Reddit account, will open a browser window to authenticate."""
    try:
        client = AppClient(CONFIG.scopes)
    except ValueError:
        click.echo(
            "Authorization failed. You must allow Reddit permissions for wipeit to function."
        )
        retry = click.confirm("Retry?", default=True)
        if retry:
            try:
                client = AppClient(CONFIG.scopes)
            except ValueError:
                click.echo("Authorization failed, aborting.")
                raise click.Abort
        else:
            raise click.Abort
    click.echo(f"Successfully authenticated as /u/{client.user.me().name}")
    click.echo("")
