import colorlog

log = colorlog.getLogger(__name__)


def sigint_handler(signum, frame):
    log.info('👋 Got SIGINT, cya')
