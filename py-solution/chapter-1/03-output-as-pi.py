# coding: UTF-8

from pprint import pprint
import unittest

target_str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

class TestSuite(unittest.TestCase):

  def testCase(self):
    print(target_str.split())
    self.assertEqual(
      [len(stng.strip(',. ')) for stng in target_str.split()],
      [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    )

unittest.main()
