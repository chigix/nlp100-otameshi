# coding: UTF-8

import sys
import os
import lib.const as const
import gzip
import json
import unittest

class TestSuite(unittest.TestCase):

  def testCase(self):
    with gzip.open(const.JAWIKI_COUNTRY_JSON_FILE, 'rb') as f:
      json_lines = [json.loads(line.decode('utf-8')) for line in f]
      ite = filter(lambda jo: jo['title'] == 'イギリス', json_lines)
      record_en = next(ite)
      self.assertEqual(record_en['title'], 'イギリス')
      self.assertRaises(StopIteration, lambda : next(ite))
      print(record_en['text'])

unittest.main()

