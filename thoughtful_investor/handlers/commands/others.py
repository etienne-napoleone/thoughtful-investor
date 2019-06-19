from telegram import ChatAction
import colorlog

log = colorlog.getLogger(__name__)


def donate(bot, update):
    log.info(f'/donate from {update.message.from_user["first_name"]}')
    bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    text = "0x5539e0E7B54b55f81Be0a8E0Db33bD8bAC1C7e4B"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )
