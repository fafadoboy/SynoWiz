# from pyspell.practice import practice_session
# from pyspell.sets import practice_set
# from pyspell.utils import *
# from pyspell.sets.utils import *
# from tabulate import tabulate

import uuid
from pathlib import Path
import re

import click

@click.group()
def cli():
    """Spelling Master"""
    
if __name__ == "__main__":
    cli()