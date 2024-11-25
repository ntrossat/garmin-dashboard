import click

from core.datapipeline.activity import ActivityPipeline


@click.group()
def cli():
    pass


@cli.command()
def load():
    pipeline = ActivityPipeline()
    pipeline.load_raw_data()

    click.echo("Loading Garmin Activities")


@cli.command()
def process():
    click.echo("Processing Garmin Data")


if __name__ == "__main__":
    cli()
