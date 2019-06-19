import json
import random
import sys

import colorlog
import markovify

log = colorlog.getLogger(__name__)
models = []


def generate_models(corpus_path, model_filename, state_sizes):
    global models
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
    for state_size in state_sizes:
        models.append(markovify.NewlineText(text, state_size=state_size))
    for index, model in enumerate(models):
        model_json = model.to_json()
        try:
            with open(model_filename + str(index), 'w') as f:
                json.dump(model_json, f)
            log.debug(f'Model {index} created')
        except Exception as e:
            log.warning(f'Could not write model {index}: {e}')


def load_models(model_filename):
    global models
    for index in range(0, 20):
        try:
            with open(model_filename + str(index)) as f:
                model_json = json.load(f)
                log.debug(f'Imported existing model {index}')
        except FileNotFoundError:
            log.debug('No more model found')
            break
        except Exception as e:
            log.fatal(f'Could not import model {index} from json: {e}')
            sys.exit(1)
        models.append(markovify.NewlineText.from_json(model_json))


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
            sentence = random.choice(models).make_sentence_with_start(start, tries=tries)
            if sentence:
                log.debug('Found a valid sentence')
                return sentence
            else:
                log.debug('Found a "None" sentence, retrying...')
    except Exception as e:
        log.error(f'Could not get sentence: {e}')
    return None
