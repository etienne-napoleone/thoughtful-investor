from os import path
import click
import colorlog

from thoughtful_investor import __version__
from thoughtful_investor import markov
from thoughtful_investor import bot

log = colorlog.getLogger(__name__)


@click.command(help='A telegram bot holding TOMO.')
@click.argument('token', envvar='TOKEN')
@click.option('--corpus', envvar='CORPUS', type=click.Path(exists=True, dir_okay=False), default='./corpus.txt', show_default=True, help='Corpus file path.')  # noqa E501
@click.option('--model', envvar='MODEL', type=click.Path(dir_okay=False), default='./model', show_default=True, help='Model base filename.')  # noqa E501
@click.option('--state-size', envvar='STATE_SIZE', multiple=True, show_default=True, help='State sizes of the markov model.')  # noqa E501
@click.option('--debug', envvar='DEBUG', is_flag=True, help='Set logging level to debug.')  # noqa E501
@click.version_option(version=__version__)
def entrypoint(token, corpus, model, state_size, debug):
    """CLI entrypoint"""
    log.info('🤔 Starting thoughtful-investor v{}'.format(__version__))
    if debug:
        log.setLevel('DEBUG')
        log.debug('Debug enabled')
    if path.isfile(model+'0'):
        log.info('At least one model found, loading now...')
        markov.load_models(model)
    else:
        log.warn('No model found, generating now...')
        markov.generate_models(corpus, str(model), state_size)
    bot.start(token)
