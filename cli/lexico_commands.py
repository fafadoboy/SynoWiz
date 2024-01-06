import click

@click.group()
def lexico_group():
    """Commands related to the lexico service."""
    pass

@lexico_group.command()
def some_lexico_command():
    """A Lexico-specific command."""
    click.echo("Lexico command executed.")
