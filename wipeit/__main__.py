import datetime as dt
from typing import Type

import click

from wipeit import VERSION
from wipeit.client import AuthorizedClient
from wipeit.history import CommentHistory, SubmissionHistory, BaseHistory


class CLIHandler:
    def __init__(
        self,
        client: AuthorizedClient,
        start_dt: dt.datetime,
        end_dt: dt.datetime,
        overwrite: bool,
    ):
        self.client = client
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.overwrite = overwrite

    def confirm_delete(self, operation: str) -> bool:
        start_str = self.start_dt.date().isoformat()
        end_str = self.end_dt.date().isoformat()
        return click.confirm(
            f"You are about to delete all {operation} from {start_str} to {end_str}, proceed?",
        )

    def delete_content(self, handler: Type[BaseHistory], content_type: str):
        history = handler(self.client)
        confirm = self.confirm_delete(f"{content_type}s")
        if confirm:
            delete_count = 0
            for item in history.wipe(self.start_dt, self.end_dt, self.overwrite):
                delete_count += 1
                click.echo(f"* Deleted {content_type} ID {item.id}")
            suffix = "s" if delete_count != 1 else ""
            click.echo(f"Deleted {delete_count} {content_type}{suffix}.")
            click.echo("")
        else:
            click.echo(f"Skipping {content_type} deletion.")
            click.echo("")


def validate_date(ctx, param, value: str) -> dt.datetime:
    if not value:
        return dt.datetime.now()
    try:
        date = dt.datetime.fromisoformat(value)
    except Exception:
        raise click.BadParameter("Invalid date")
    else:
        return date


@click.command()
@click.version_option(VERSION)
@click.option(
    "--days",
    "-d",
    help="Number of days worth of content to delete. Defaults to 365.",
    default=365,
    type=click.IntRange(1, 365 * 5, clamp=True),
)
@click.option(
    "--from-date",
    "-f",
    help="Date relative to --days, in ISO format (YYYY-MM-DD). Defaults to today.",
    type=str,
    callback=validate_date,
)
@click.option(
    "--comments",
    "-c",
    is_flag=True,
    default=False,
    help="Delete comments.",
)
@click.option(
    "--submissions",
    "-s",
    is_flag=True,
    default=False,
    help="Delete submissions.",
)
@click.option(
    "--overwrite",
    "-o",
    is_flag=True,
    default=False,
    help="Overwrite content with random text before deletion.",
)
def cli(
    days: int,
    from_date: dt.datetime,
    comments: bool,
    submissions: bool,
    overwrite: bool,
    *args,
    **kwargs,
):
    # Initialize client and parse arguments
    scopes = ["identity", "edit", "history"]
    try:
        client = AuthorizedClient(scopes)
    except ValueError:
        click.echo(
            "Authorization failed. You must allow Reddit permissions for wipeit to function."
        )
        confirm = click.confirm("Retry?", default=True)
        if confirm:
            try:
                client = AuthorizedClient(scopes)
            except ValueError:
                click.echo("Authorization failed, aborting.")
                raise click.Abort
        else:
            raise click.Abort
    end_dt = from_date
    start_dt = end_dt - dt.timedelta(days=days)

    # Handle
    handler = CLIHandler(client, start_dt, end_dt, overwrite)
    if comments:
        handler.delete_content(CommentHistory, "comment")
    if submissions:
        handler.delete_content(SubmissionHistory, "submission")


if __name__ == "__main__":
    cli()
