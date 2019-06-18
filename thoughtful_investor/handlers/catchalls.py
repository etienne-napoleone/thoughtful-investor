import colorlog

log = colorlog.getLogger(__name__)


def command(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Sorry, I didn\'t understand that',
    )
    log.debug('Received unhandled message')
