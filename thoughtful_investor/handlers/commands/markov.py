import random as rd

from telegram.ext.dispatcher import run_async
from telegram import ChatAction
import colorlog

from thoughtful_investor.markov import gen_sentence
from thoughtful_investor.markov import gen_sentence_with_start

log = colorlog.getLogger(__name__)

NO_RESULT_MESSAGES = [
    '🤯',
]


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
        text=message if message else rd.choice(NO_RESULT_MESSAGES),
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
        text=message if message else rd.choice(NO_RESULT_MESSAGES),
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
        text=message if message else rd.choice(NO_RESULT_MESSAGES),
    )


@run_async
def yes_or_no(bot, update):
    log.info(f'/yes_or_no from {update.message.from_user["first_name"]}')
    bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    if rd.choice([True, False]):
        message = gen_sentence_with_start('Yes')
    else:
        message = gen_sentence_with_start('No')
    bot.send_message(
        chat_id=update.message.chat_id,
        text=message if message else rd.choice(NO_RESULT_MESSAGES),
    )
