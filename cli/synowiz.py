# import uuid
# from pathlib import Path


# from rich import box
# from rich.console import Console
# from rich.prompt import Confirm
# from rich.prompt import Prompt
# from rich.rule import Rule
# from rich.table import Table

# from cli.lexico_commands import lexico_group
# from cli.practice_commands import practice_group

import click

# Import the client functions from the lexico and practice modules
# from clients.lexico_client import ...
# from clients.practice_client import ...


# Define the main CLI group
@click.group()
def cli():
    """
    SynoWiz: A unified interface for Lexico and Practice functionalities.
    """
    pass


# Lexico Commands
@cli.group(name="lexico")
def lexico():
    """Lexico Service Commands"""
    pass


@lexico.command(name="lookup")
@click.argument("word")
def lookup_word(word):
    """Look up a word in the Lexico service."""
    # Call the lexico client method to look up the word
    click.echo(f"Looking up the word: {word}")
    # result = lexico_client.lookup_word(word)
    # click.echo(result)


@lexico.command(name="add")
@click.argument("word")
@click.argument("details")
def add_word(word, details):
    """Add a new word to the Lexico service."""
    # Call the lexico client method to add the word
    click.echo(f"Adding the word: {word} with details: {details}")
    # result = lexico_client.add_word(word, details)
    # click.echo(result)


# Practice Commands
@cli.group(name="practice")
def practice():
    """Practice Service Commands"""
    pass


@practice.command(name="create-set")
@click.argument("set_name")
@click.argument("words", nargs=-1)
def create_practice_set(set_name, words):
    """Create a new practice set."""
    # Call the practice client method to create a new set
    click.echo(f"Creating a practice set: {set_name} with words: {', '.join(words)}")
    # result = practice_client.create_set(set_name, words)
    # click.echo(result)


@practice.command(name="start-session")
@click.argument("set_id")
def start_practice_session(set_id):
    """Start a practice session with the given set."""
    # Call the practice client method to start a session
    click.echo(f"Starting a practice session with set ID: {set_id}")
    # result = practice_client.start_session(set_id)
    # click.echo(result)


if __name__ == "__main__":
    cli()
