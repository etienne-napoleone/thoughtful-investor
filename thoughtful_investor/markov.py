import json
import random
import sys
import os

import colorlog
import markovify

log = colorlog.getLogger(__name__)
models = []


def generate_model(corpus, model, state_size):
    try:
        with open(corpus) as f:
            text = f.read()
            log.debug('Imported corpus file')
    except FileNotFoundError:
        log.fatal('Could not find corpus')
        sys.exit(1)
    except Exception as e:
        log.fatal(f'Could not compute model: {e}')
        sys.exit(1)
    model_raw = markovify.NewlineText(text, state_size=state_size)
    model_json = model_raw.to_json()
    try:
        with open(model, 'w') as f:
            json.dump(model_json, f)
        log.debug(f'Model {model} created')
    except Exception as e:
        log.fatal(f'Could not write model {model}: {e}')
        sys.exit(1)


def load_models(models_repertory):
    global models
    for model in os.listdir(models_repertory):
        try:
            with open(os.path.join(models_repertory, model)) as f:
                model_json = json.load(f)
                models.append(markovify.NewlineText.from_json(model_json))
                log.debug(f'Imported model {model}')
        except Exception as e:
            log.warning(f'Ignoring {model} as it could not be imported')
            log.debug(e)
    if not len(models):
        log.fatal('No model could be imported in {models_repertory}')


def gen_sentence(tries=250):
    try:
        log.debug('Generating up to 10 sentences...')
        for i in range(10):
            sentence = random.choice(models).make_sentence(tries=tries)
            if sentence:
                log.debug('Found a valid sentence')
                return sentence
            else:
                log.debug('Found a "None" sentence, retrying...')
    except Exception as e:
        log.error(f'Could not get sentence: {e}')
    return None


def gen_sentence_with_start(start='', tries=250):
    try:
        log.debug('Generating up to 10 sentences...')
        for i in range(10):
            sentence = random.choice(models).make_sentence_with_start(
                start, tries=tries
            )
            if sentence:
                log.debug('Found a valid sentence')
                return sentence
            else:
                log.debug('Found a "None" sentence, retrying...')
    except Exception as e:
        log.error(f'Could not get sentence: {e}')
    return None
