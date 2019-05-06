"""CLI Applicaiton for connecting to a time server."""
import requests
import click
import time
import os


@click.command()
@click.option(
    '--hostname',
    default=os.getenv('HOSTNAME') or 'localhost')
@click.option(
    '--repeat',
    default=5)
def get_time(hostname, repeat):
    """Get the current time from server."""
    for _ in range(0, repeat):
        click.echo(
            requests.get('http://{}:5001'.format(hostname)).json())
        time.sleep(2)


if __name__ == '__main__':
    get_time()  # pragma: no cover
