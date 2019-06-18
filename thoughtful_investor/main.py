from thoughtful_investor import __version__

import click


@click.command(help='A telegram bot holding TOMO.')
@click.version_option(version=__version__)
def entrypoint():
    """CLI entrypoint"""
    pass
