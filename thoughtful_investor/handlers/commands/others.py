from telegram import ChatAction
from telegram import ParseMode
import colorlog

log = colorlog.getLogger(__name__)


def support(bot, update):
    log.info(f'/support from {update.message.from_user["first_name"]}')
    bot.send_chat_action(
        chat_id=update.message.chat_id,
        action=ChatAction.TYPING
    )
    text = (
        '🔗☕️\nThis bot was made using [makov chains]'
        '(https://en.wikipedia.org/wiki/Markov_chain#Applications) '
        'and some coffees.'
        '\nIf you enjoy this bot and want to help me '
        '[build](https://github.com/etienne-napoleone) more stuff, '
        'I\'ll be thankful if you send me some some TOMO for a coffee :)\n'
        '`0x5539e0E7B54b55f81Be0a8E0Db33bD8bAC1C7e4B`'
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
        parse_mode=ParseMode.MARKDOWN,
    )
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open('./assets/account_qr.png', 'rb'),
    )
