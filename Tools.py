import json
import logging
from tqdm import tqdm

class TqdmLoggingHandler(logging.Handler):
    def __init__(self, level=logging.NOTSET):
        super().__init__(level)

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.write(msg)
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

def create_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s] %(name)s: %(message)s')
    tqdm_stream_handler = TqdmLoggingHandler()
    tqdm_stream_handler.setFormatter(formatter)
    logger.addHandler(tqdm_stream_handler)
    return logger

def import_json(file_path):
    logger.debug('Importing JSON from {}'.format(file_path))
    with open(file_path) as file:
        data = json.load(file)
    return data

def export_json(replay_config, output_path):
    logger.debug('Exporting replay JSON to {}'.format(output_path))
    with open(output_path, 'w', encoding='utf8') as file:
        file.write(json.dumps(replay_config))

logger = create_logger(__name__)