import pytest
from click.testing import CliRunner
from cli.synowiz import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_lexico_lookup(runner):
    result = runner.invoke(cli, ["lexico", "lookup", "apple"])
    assert result.exit_code == 0
    assert "Looking up the word: apple" in result.output


def test_practice_create_set(runner):
    input = ["practice", "create-set", "Fruits", "apple", "banana"]
    result = runner.invoke(cli, input)
    assert result.exit_code == 0
    assert "Creating a practice set: Fruits with words: apple, banana" in result.output


# Add more tests for other commands and scenarios
