from telegram.error import BadRequest
from telegram.error import ChatMigrated
from telegram.error import NetworkError
from telegram.error import TelegramError
from telegram.error import TimedOut
from telegram.error import Unauthorized
import colorlog

log = colorlog.getLogger(__name__)


def error(bot, update, error):
    try:
        raise error
    except (
        TelegramError,
        Unauthorized,
        BadRequest,
        TimedOut,
        ChatMigrated,
        NetworkError
    ) as e:
        log.error(f'Error while processing: {e}')
    # except Unauthorized:
    #     # remove update.message.chat_id from conversation list
    # except BadRequest:
    #     # handle malformed requests - read more below!
    # except TimedOut:
    #     # handle slow connection problems
    # except NetworkError:
    #     # handle other connection problems
    # except ChatMigrated as e:
    #     # the chat_id of a group has changed, use e.new_chat_id instead
    # except TelegramError:
    #     # handle all other telegram related errors
