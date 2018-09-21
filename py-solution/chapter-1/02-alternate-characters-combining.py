# coding: UTF-8

from pprint import pprint
import unittest

str1 = 'パトカー'
str2 = 'タクシー'

class TestSuite(unittest.TestCase):

  def testCase(self):
    zipped = zip(str1, str2)
    self.assertEqual(
      [('パ', 'タ'), ('ト', 'ク'), ('カ', 'シ'), ('ー', 'ー')],
      list(zipped))
    self.assertEqual(''.join(map(lambda arr: arr[0] + arr[1], zip(str1,str2))),
      'パタトクカシーー')
    # pprint(''.join(map(lambda arr: arr[0] + arr[1], zip(str1,str2))))

unittest.main()
