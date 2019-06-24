#!/usr/bin/python -tt

import sys
from Compiler import *

DEBUG = False

for arg in sys.argv:
	if arg == "-d":
		DEBUG = True

doc = sys.stdin.read()

compiler = Compiler(DEBUG)
result = compiler.compile(doc)
print(result)
