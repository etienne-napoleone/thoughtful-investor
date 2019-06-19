from telegram import ChatAction
import colorlog

from thoughtful_investor.markov import gen_sentence

log = colorlog.getLogger(__name__)


def random(bot, update):
    log.info(f'/random from {update.message.from_user["first_name"]}')
    bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    message = gen_sentence()
    bot.send_message(
        chat_id=update.message.chat_id,
        text=message,
    )
