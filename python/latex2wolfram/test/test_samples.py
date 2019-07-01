import difflib
from latex2wolfram.Compiler import *

compiler = None

def setup_module(module):
	module.compiler = Compiler()


def check_test(name1, name2):
	f1 = open(name1, 'r')
	f2 = open(name2, 'r')

	expected = f2.read()
	expected = expected[:-1] # remove last \n

	doc = f1.read()
	#compiler = Compiler()
	actual = compiler.compile(doc)

	expected=expected.splitlines(True)
	actual=actual.splitlines(True)

	diff = difflib.unified_diff(expected, actual)
	diff = list(diff)

	f1.close()
	f2.close()

	if len(diff) != 0:
		print(''.join(diff))

	assert len(diff) == 0

def check_test_num(num, with_declarations = False):
	name1 = 'latex2wolfram/test/samples/test'+str(num)+'.tex'
	name2 = 'latex2wolfram/test/samples/output/test'+str(num)+'.out'

	check_test(name1, name2)

def test1():
	check_test_num(1)

def test2():
	check_test_num(2)

def test3():
	check_test_num(3)

def test4():
	check_test_num(4)

def test5():
	check_test_num(5)
