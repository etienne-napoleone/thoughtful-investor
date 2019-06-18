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

log = colorlog.getLogger(__name__)


@click.command(help='A telegram bot holding TOMO.')
@click.argument('telegram_token', envvar='TELEGRAM_TOKEN')
@click.option('--debug', is_flag=True, help='Set logging level to debug.')
@click.version_option(version=__version__)
def entrypoint(telegram_token, debug):
    """CLI entrypoint"""
    log.info('🤔 Starting thoughtful-investor v{}'.format(__version__))
    if debug:
        log.setLevel('DEBUG')
        log.debug('Debug enabled')
    poll(telegram_token)


def poll(token):
    try:
        updater = Updater(token=token)
        log.debug('Created updater')
        dispatcher = updater.dispatcher
        # error handler
        dispatcher.add_error_handler(handlers.error)
        log.debug(f'Added error handler')
        # commands handler
        dispatcher.add_handler(
            CommandHandler('say', handlers.commands.say)
        )
        log.debug('Added command /say')
        dispatcher.add_handler(
            CommandHandler('donate', handlers.commands.donate)
        )
        log.debug('Added command /donate')
        # catchall command handler handler
        dispatcher.add_handler(
            MessageHandler(Filters.command, handlers.catchalls.command)
        )
        log.debug('Added catchall handler')
        updater.start_polling(timeout=60)
        updater.idle()
    except InvalidToken:
        log.fatal('Invalid token')
        sys.exit(1)
