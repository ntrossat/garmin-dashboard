import click

from core.cli.datapipeline import DataPipeline

@click.group()
def cli():
    pass

@cli.command()
def fetch():
    garmin = DataPipeline('user','password')
    garmin.fetch_raw_data()
    click.echo('Fetching Garmin Raw Data')

@cli.command()
def update():
    click.echo('Updating Garmin')


if __name__ == "__main__":
    cli()
