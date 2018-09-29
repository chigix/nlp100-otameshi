# coding: UTF-8

import os

CONST_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(CONST_PATH)
FIXTURES_DIR = os.path.normpath(os.path.join(BASE_DIR, '../../../fixtures'))
JAWIKI_COUNTRY_JSON_FILE = os.path.normpath(os.path.join(FIXTURES_DIR, 'jawiki-country.json.gz'))
