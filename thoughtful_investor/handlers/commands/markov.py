from telegram.ext.dispatcher import run_async
from telegram import ChatAction
import colorlog

from thoughtful_investor.markov import gen_sentence
from thoughtful_investor.markov import gen_sentence_with_start

log = colorlog.getLogger(__name__)


@run_async
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


@run_async
def yes(bot, update):
    log.info(f'/yes from {update.message.from_user["first_name"]}')
    bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    message = gen_sentence_with_start('Yes')
    bot.send_message(
        chat_id=update.message.chat_id,
        text=message,
    )


@run_async
def no(bot, update):
    log.info(f'/no from {update.message.from_user["first_name"]}')
    bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    message = gen_sentence_with_start('No')
    bot.send_message(
        chat_id=update.message.chat_id,
        text=message,
    )
