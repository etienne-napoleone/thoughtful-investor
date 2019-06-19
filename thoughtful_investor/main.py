from os import path
import sys

from telegram.error import InvalidToken
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
import click
import colorlog

from thoughtful_investor import __version__
from thoughtful_investor import handlers
from thoughtful_investor import markov

log = colorlog.getLogger(__name__)


@click.command(help='A telegram bot holding TOMO.')
@click.argument('token', envvar='TOKEN')
@click.option('--corpus', envvar='CORPUS', type=click.Path(exists=True, dir_okay=False), default='./corpus.txt', show_default=True, help='Corpus file path.')  # noqa E501
@click.option('--model', envvar='MODEL', type=click.Path(dir_okay=False), default='./model.json', show_default=True, help='Model file path.')  # noqa E501
@click.option('--state-size', envvar='STATE_SIZE', type=int, default=5, show_default=True, help='State size of the markov model.')  # noqa E501
@click.option('--debug', envvar='DEBUG', is_flag=True, help='Set logging level to debug.')  # noqa E501
@click.version_option(version=__version__)
def entrypoint(token, corpus, model, state_size, debug):
    """CLI entrypoint"""
    log.info('🤔 Starting thoughtful-investor v{}'.format(__version__))
    if debug:
        log.setLevel('DEBUG')
        log.debug('Debug enabled')
    if path.isfile(model):
        log.info('Model found, loading now...')
        markov.load_model(model)
    else:
        log.warn('Model not found, generating now...')
        markov.generate_model(corpus, str(model), state_size)
    start_bot(token)


def start_bot(token):
    try:
        updater = Updater(token=token)
        updater.logger = log
        log.debug('Created updater')
        dispatcher = updater.dispatcher
        dispatcher.logger = log
        # error handlers
        dispatcher.add_error_handler(handlers.error)
        log.debug(f'Added error handler')
        # command handlers
        dispatcher.add_handler(
            CommandHandler('random', handlers.commands.random)
        )
        log.debug('Added command /random')
        dispatcher.add_handler(
            CommandHandler('yes', handlers.commands.yes)
        )
        log.debug('Added command /yes')
        dispatcher.add_handler(
            CommandHandler('no', handlers.commands.no)
        )
        log.debug('Added command /no')
        dispatcher.add_handler(
            CommandHandler('support', handlers.commands.support)
        )
        log.debug('Added command /support')
        # catchall handlers
        dispatcher.add_handler(
            MessageHandler(Filters.command, handlers.catchalls.command)
        )
        log.debug('Added catchall handler')
        log.info('🤖 Starting bot')
        updater.start_polling(timeout=60)
        updater.idle()
    except InvalidToken:
        log.fatal('Invalid token')
        sys.exit(1)
