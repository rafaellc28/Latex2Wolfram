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
	compiler = Compiler()
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

def test35():
	check_test_num(35)

def test36():
	check_test_num(36)

def test37():
	check_test_num(37)

def test38():
	check_test_num(38)

def test39():
	check_test_num(39)

def test40():
	check_test_num(40)

def test41():
	check_test_num(41)

def test42():
	check_test_num(42)

def test43():
	check_test_num(43)

def test44():
	check_test_num(44)

def test45():
	check_test_num(45)

def test46():
	check_test_num(46)

def test47():
	check_test_num(47)

def test48():
	check_test_num(48)

def test49():
	check_test_num(49)

def test50():
	check_test_num(50)

def test51():
	check_test_num(51)

def test52():
	check_test_num(52)

def test53():
	check_test_num(53)

def test54():
	check_test_num(54)

def test55():
	check_test_num(55)

def test56():
	check_test_num(56)

def test57():
	check_test_num(57)

def test58():
	check_test_num(58)

def test59():
	check_test_num(59)

def test60():
	check_test_num(60)

def test61():
	check_test_num(61)

def test62():
	check_test_num(62)

def test63():
	check_test_num(63)

def test64():
	check_test_num(64)

def test65():
	check_test_num(65)

def test66():
	check_test_num(66)

def test67():
	check_test_num(67)

def test68():
	check_test_num(68)

def test69():
	check_test_num(69)

def test70():
	check_test_num(70)

def test71():
	check_test_num(71)

def test72():
	check_test_num(72)

def test73():
	check_test_num(73)

def test74():
	check_test_num(74)

def test75():
	check_test_num(75)

def test76():
	check_test_num(76)

def test77():
	check_test_num(77)

def test78():
	check_test_num(78)

def test79():
	check_test_num(79)

def test80():
	check_test_num(80)

def test81():
	check_test_num(81)

def test82():
	check_test_num(82)

def test83():
	check_test_num(83)

def test84():
	check_test_num(84)

def test85():
	check_test_num(85)

def test86():
	check_test_num(86)

def test87():
	check_test_num(87)

def test88():
	check_test_num(88)

def test89():
	check_test_num(89)

def test90():
	check_test_num(90)

def test91():
	check_test_num(91)

def test92():
	check_test_num(92)

def test93():
	check_test_num(93)

def test94():
	check_test_num(94)

def test95():
	check_test_num(95)

def test96():
	check_test_num(96)

def test97():
	check_test_num(97)

def test98():
	check_test_num(98)

def test99():
	check_test_num(99)

def test100():
	check_test_num(100)

def test101():
	check_test_num(101)

def test102():
	check_test_num(102)

def test103():
	check_test_num(103)

def test104():
	check_test_num(104)

def test105():
	check_test_num(105)

def test106():
	check_test_num(106)

def test107():
	check_test_num(107)

def test108():
	check_test_num(108)

def test109():
	check_test_num(109)

def test110():
	check_test_num(110)

def test111():
	check_test_num(111)

def test112():
	check_test_num(112)

def test113():
	check_test_num(113)

def test114():
	check_test_num(114)

def test115():
	check_test_num(115)

def test116():
	check_test_num(116)

def test117():
	check_test_num(117)

def test118():
	check_test_num(118)

def test119():
	check_test_num(119)

def test120():
	check_test_num(120)

def test121():
	check_test_num(121)

def test122():
	check_test_num(122)

def test123():
	check_test_num(123)

def test124():
	check_test_num(124)

def test125():
	check_test_num(125)

def test126():
	check_test_num(126)

def test127():
	check_test_num(127)

def test128():
	check_test_num(128)

def test129():
	check_test_num(129)

def test130():
	check_test_num(130)

def test131():
	check_test_num(131)

def test132():
	check_test_num(132)

def test133():
	check_test_num(133)

def test134():
	check_test_num(134)

def test135():
	check_test_num(135)

def test136():
	check_test_num(136)

def test137():
	check_test_num(137)

def test138():
	check_test_num(138)

def test139():
	check_test_num(139)

def test140():
	check_test_num(140)

def test141():
	check_test_num(141)

def test142():
	check_test_num(142)

def test143():
	check_test_num(143)

def test144():
	check_test_num(144)

def test145():
	check_test_num(145)

def test146():
	check_test_num(146)

def test147():
	check_test_num(147)

def test148():
	check_test_num(148)

def test149():
	check_test_num(149)

def test150():
	check_test_num(150)

def test151():
	check_test_num(151)

def test152():
	check_test_num(152)

def test153():
	check_test_num(153)

def test154():
	check_test_num(154)

def test155():
	check_test_num(155)

def test156():
	check_test_num(156)
