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

def test6():
	check_test_num(6)

def test7():
	check_test_num(7)

def test8():
	check_test_num(8)

def test9():
	check_test_num(9)

def test10():
	check_test_num(10)

def test11():
	check_test_num(11)

def test12():
	check_test_num(12)

def test13():
	check_test_num(13)

def test14():
	check_test_num(14)

def test15():
	check_test_num(15)

def test16():
	check_test_num(16)

def test17():
	check_test_num(17)

def test18():
	check_test_num(18)

def test19():
	check_test_num(19)

def test20():
	check_test_num(20)

def test21():
	check_test_num(21)

def test22():
	check_test_num(22)

def test23():
	check_test_num(23)

def test24():
	check_test_num(24)

def test25():
	check_test_num(25)

def test26():
	check_test_num(26)

def test27():
	check_test_num(27)

def test28():
	check_test_num(28)

def test29():
	check_test_num(29)

def test30():
	check_test_num(30)

def test31():
	check_test_num(31)

def test32():
	check_test_num(32)

def test33():
	check_test_num(33)

def test34():
	check_test_num(34)
