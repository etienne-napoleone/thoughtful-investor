import random

from telegram import ChatAction
import colorlog

log = colorlog.getLogger(__name__)


def command(bot, update):
    bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    messages = [
        'Sorry, what?',
        'Can you repeat please?',
        'I don\'t understand...',
        'What do you want from me?!',
        'No way.',
        'Please stop.',
        '😤',
        '🙅‍♂️',
    ]
    bot.send_message(
        chat_id=update.message.chat_id,
        text=random.choice(messages),
    )
    log.debug('Received unhandled message')
