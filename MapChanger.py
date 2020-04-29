import os
import sys
import glob
import logging
import requests
import argparse
import subprocess
import urllib.request
from pathlib import Path
from Tools import create_logger, export_json, import_json, logger

PARSER = glob.glob('Parser/*.exe')

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--replay", help="Path of the replay to convert")
    parser.add_argument("-d", "--replay-directory", help="Directory of replays to convert")
    parser.add_argument("-m", "--map", type=str, help="Resulting map on the replay")
    parser.add_argument("-v", "--verbosity", action='store_true', help="Increase output verbosity")
    return parser.parse_args()

class Parser:
    
    def __init__(self, parser_path):
        self.parser_path = parser_path
        self.release_url = 'https://api.github.com/repos/tfausak/rattletrap/releases/latest'
        self.latest_parser_info = self._get_latest_parser_info()

    def update(self):
        if self._parser_out_of_date():
            logger.info('The replay parser is out of date. Retrieving latest rattletrap release...')
            self.updated_parser_path = self._download_parser()
            self._remove_old_parser()
            return self.updated_parser_path
        else:
            logger.info('Latest parser release already downloaded')
            return self.parser_path[0]

    def _parser_out_of_date(self) -> bool:
        if not glob.glob('Parser/{}'.format(self.latest_parser_info['Name'])):
            return True
        else:
            return False

    def _download_parser(self):
        new_parser_path = 'Parser/{}'.format(self.latest_parser_info['Name'])
        urllib.request.urlretrieve(self.latest_parser_info['URL'], new_parser_path)
        return new_parser_path

    def _remove_old_parser(self):
        if self.parser_path:
            os.remove(self.parser_path[0])

    def _get_latest_parser_info(self) -> dict:
        logger.debug('Getting latest rattltrap release URL...')
        response = requests.get(self.release_url).json()
        for asset in response['assets']:
            if 'exe' in asset['browser_download_url']:
                return {'URL': asset['browser_download_url'], 'Name': asset['name']}

class Replay:
    
    def __init__(self, parser_path, replay_path, map_data):
        self.parser_path = parser_path
        self.replay_path = replay_path
        self.replay_parent = Path(replay_path).parent
        self.replay_name = Path(replay_path).stem
        self.replay_ext = Path(replay_path).suffix
        self.replay_temp = 'temp.json'
        self.map_data = map_data

    def change_map(self, map_code):
        self.replay_out = '{}/{}_converted_{}{}'.format(self.replay_parent, self.replay_name, map_code, self.replay_ext)
        self.replay_json = self._decode()
        self._update_map(map_code)
        self._encode()
        return self.replay_out

    def _decode(self) -> dict:
        logger.debug('Decoding replay file to {}...'.format(self.replay_temp))
        command = [self.parser_path, '-i', self.replay_path, '-o', self.replay_temp]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, encoding='utf-8', errors='replace')
        
        if result.returncode != 0:
            logger.error('Replay {} failed to decode. Exiting...'.format(self.replay_path))
            sys.exit(0)
        
        return import_json(self.replay_temp)

    def _encode(self) -> str:
        logger.debug('Encoding {} to replay file...'.format(self.replay_temp))
        command = [self.parser_path, '-i', self.replay_temp, '-o', self.replay_out]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, encoding='utf-8', errors='replace')
        if result.returncode != 0:
            logger.error('Replay failed to re-encode. Exiting...')
            sys.exit(0)
        else:
            logger.debug('Removing temporary JSON file...')
            os.remove(self.replay_temp)

    def _update_map(self, map_code):
        map_code_old = self.replay_json['header']['body']['properties']['value']['MapName']['value']['name']
        self.replay_json['header']['body']['properties']['value']['MapName']['value']['name'] = map_code

        logger.debug('Changing map from {} to {}'.format(self.map_data[map_code_old.lower()], self.map_data[map_code.lower()]))
        export_json(self.replay_json, self.replay_temp)        

class Converter:

    def __init__(self, parser, map_code):
        self.parser = parser
        self.map_code = map_code
        self.map_data = import_json('Resources/Maps.json')
    
    def single(self, replay_path):
        logger.info('Converting replay...')
        replay_out_path = Replay(self.parser, replay_path, self.map_data).change_map(self.map_code)
        logger.info('Replay converted! Resulting file is located at {}'.format(replay_out_path))

    def directory(self, directory_path):
        replays = glob.glob('{}/*.replay'.format(Path(directory_path)))
        replays = [replay for replay in replays if 'converted' not in replay.lower()]
        
        logger.info('Converting directory...')

        for replay in tqdm(replays):
            Replay(self.parser, replay, self.map_data).change_map(self.map_code)

        logger.info('Directory converted!')

def main():
    args = get_args()
    parser = Parser(PARSER).update()

    if args.verbosity:
        logger.setLevel(logging.DEBUG)

    if args.replay:
        Converter(parser, args.map).single(args.replay)
    elif args.replay_directory:
        Converter(parser, args.map).directory(args.replay_directory)

if __name__ == '__main__':
    main()
