# coding: UTF-8

import sys
import os

file=os.path.normpath(
  os.path.join(os.getcwd(), sys.argv[1])
)

print(sum(1 for x in open(file)))

