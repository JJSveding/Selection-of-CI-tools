

import click

import commands


@click.group()
def cli() -> None:
    pass

cli.add_command(commands.pr_comments.print_changed_costs)

if __name__ == "__main__":
    cli()
