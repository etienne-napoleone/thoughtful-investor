import json
import sys

import colorlog
import markovify

log = colorlog.getLogger(__name__)
model = None


def generate_model(corpus_path, model_path, state_size):
    global model
    try:
        with open(corpus_path) as f:
            text = f.read()
            log.debug('Imported corpus file')
    except FileNotFoundError:
        log.fatal('Could not find corpus')
        sys.exit(1)
    except Exception as e:
        log.fatal(f'Could not compute model: {e}')
        sys.exit(1)
    model = markovify.NewlineText(text, state_size=state_size)
    model_json = model.to_json()
    try:
        with open(model_path, 'w') as f:
            json.dump(model_json, f)
        log.debug('Model created')
    except Exception as e:
        log.warning(f'Could not write model: {e}')


def load_model(model_path):
    global model
    try:
        with open(model_path) as f:
            model_json = json.load(f)
            log.debug('Imported existing model')
    except Exception as e:
        log.fatal(f'Could not import model from json: {e}')
        sys.exit(1)
    model = markovify.NewlineText.from_json(model_json)  # noqa F841


def gen_sentence(tries=400):
    try:
        log.debug('Generating up to 10 sentences...')
        for i in range(10):
            sentence = model.make_sentence(tries=tries)
            if sentence:
                log.debug('Found a valid sentence')
                return sentence
            else:
                log.debug('Found a "None" sentence, retrying...')
    except Exception as e:
        log.error(f'Could not get sentence: {e}')
    return None


def gen_sentence_with_start(start='', tries=400):
    try:
        log.debug('Generating up to 10 sentences...')
        for i in range(10):
            sentence = model.make_sentence_with_start(start, tries=tries)
            if sentence:
                log.debug('Found a valid sentence')
                return sentence
            else:
                log.debug('Found a "None" sentence, retrying...')
    except Exception as e:
        log.error(f'Could not get sentence: {e}')
    return None
