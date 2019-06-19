import click
import colorlog

from thoughtful_investor import __version__
from thoughtful_investor import markov
from thoughtful_investor import bot

log = colorlog.getLogger(__name__)


@click.group(help='A telegram bot holding TOMO.')
@click.option('--debug', envvar='DEBUG', is_flag=True, help='Set logging level to debug.')  # noqa E501
@click.version_option(version=__version__)
def entrypoint(debug):
    """CLI entrypoint"""
    if debug:
        log.setLevel('DEBUG')
        log.debug('Debug enabled')


@entrypoint.command()
@click.option('--corpus', envvar='CORPUS', type=click.Path(exists=True, dir_okay=False), default='./corpus.txt', show_default=True, help='Corpus file path.')  # noqa E501
@click.option('--model', envvar='MODEL', type=click.Path(dir_okay=False), default='./models/model.json', show_default=True, help='Model file path.')  # noqa E501
@click.option('--state-size', envvar='STATE_SIZE', default=4, show_default=True, help='State sizes of the markov model.')  # noqa E501
def generate_model(corpus, model, state_size):
    """Generate data models"""
    log.info(f'Generating a new model at {model}...')
    markov.generate_model(corpus, model, state_size)


@entrypoint.command()
@click.argument('token', envvar='TOKEN')
@click.option('--model_repertory', envvar='MODEL', type=click.Path(exists=True), default='./models', show_default=True, help='Models repertory path.')  # noqa E501
def start(token, model_repertory):
    """Start the bot"""
    log.info('🤔 Starting thoughtful-investor v{}'.format(__version__))
    markov.load_models(model_repertory)
    bot.start(token)
