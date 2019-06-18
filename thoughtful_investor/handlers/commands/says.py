import telegram

import colorlog

log = colorlog.getLogger(__name__)


def say(bot, update):
    bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=telegram.ChatAction.TYPING
    )
    text = "I'm a bot, please talk to me!"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )
    log.info(f'/say from {update.message.from_user["first_name"]}')
