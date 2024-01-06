import click

# Import the auto-generated client for practice service
from clients.practice_client.swagger_client import api_client, apis, models

# Configure the API client (you can also configure this in a config file or environment variables)
configuration = api_client.Configuration(
    host="http://localhost:8000"  # Replace with the actual host of the practice server
)
configuration.api_key["api_key"] = "YOUR_API_KEY"  # If API key is required
client = api_client.ApiClient(configuration)

# Instantiate the API class using the client
practice_api_instance = apis.DefaultApi(client)


@click.group()
def practice_group():
    """Commands related to the practice service."""
    pass


@practice_group.command()
@click.argument("set_id")
def get_practice_set(set_id):
    """Get a practice set by its ID."""
    try:
        # Use the API instance to call your practice service
        api_response = practice_api_instance.get_practice_set_by_id(set_id)
        click.echo(f"Practice Set: {api_response}")
    except api_client.ApiException as e:
        click.echo(f"Exception when calling get_practice_set_by_id: {e}")


@practice_group.command()
@click.argument("set_id")
@click.argument("score")
@click.argument("retries")
def record_execution(set_id, score, retries):
    """Record a new practice execution."""
    execution = models.PracticeExecution(
        practice_set_id=set_id, score=score, retries=retries
    )
    try:
        # Record a new practice execution
        api_response = practice_api_instance.add_practice_execution(execution)
        click.echo(f"Practice Execution Recorded: {api_response}")
    except api_client.ApiException as e:
        click.echo(f"Exception when calling add_practice_execution: {e}")


# Add more commands as needed
