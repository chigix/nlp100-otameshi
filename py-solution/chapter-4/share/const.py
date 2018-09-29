# coding: UTF-8

import os

CONST_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(CONST_PATH)
FIXTURES_DIR = os.path.normpath(os.path.join(BASE_DIR, '../../../fixtures'))
OUTPUT_DIR = os.path.normpath(os.path.join(BASE_DIR, '../../../.out'))
NEKO_TXT_FILE = os.path.normpath(os.path.join(FIXTURES_DIR, 'neko.txt'))
NEKO_MECAB_OUT = os.path.normpath(os.path.join(OUTPUT_DIR, 'neko.txt.mecab'))
