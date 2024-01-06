import uuid
from pathlib import Path
import re

import click
from rich import box
from rich.console import Console
from rich.prompt import Confirm
from rich.prompt import Prompt
from rich.rule import Rule
from rich.table import Table

from cli.lexico_commands import lexico_group
from cli.practice_commands import practice_group

@click.group()
def synowiz():
    """SynoWiz CLI tool that includes subcommands for lexico and practice services."""
    pass

synowiz.add_command(lexico_group, name="lexico")
synowiz.add_command(practice_group, name="practice")

if __name__ == "__main__":
    synowiz()
