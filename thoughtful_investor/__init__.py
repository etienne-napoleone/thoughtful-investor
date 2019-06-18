import colorlog

__version__ = '0.1.0'

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(yellow)s%(asctime)s%(reset)s - %(log_color)s%(levelname)s%(reset)s'
    ' - %(message)s',
    '%H:%M:%S'
))
log = colorlog.getLogger(__name__)
log.setLevel('INFO')
log.addHandler(handler)
