import colorlog
import sys

from telegram.error import InvalidToken
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from thoughtful_investor import handlers

log = colorlog.getLogger(__name__)


def start(token):
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
            CommandHandler('yes_or_no', handlers.commands.yes_or_no)
        )
        log.debug('Added command /yes_or_no')
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
