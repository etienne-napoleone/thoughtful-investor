from thoughtful_investor import __version__

import click
import colorlog

log = colorlog.getLogger(__name__)


@click.command(help='A telegram bot holding TOMO.')
@click.argument('telegram_key', envvar='TELEGRAM_KEY')
@click.option('--debug', is_flag=True, help='Set logging level to debug.')
@click.version_option(version=__version__)
def entrypoint(telegram_key, debug):
    """CLI entrypoint"""
    log.info('🤔 Starting thoughtful-investor v{}'.format(__version__))
    if debug:
        log.setLevel('DEBUG')
        log.debug('Debug enabled')
