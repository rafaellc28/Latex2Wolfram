#!/usr/bin/python -tt

import re
import logging

import ply.lex as lex
import ply.yacc as yacc
import lexer as lexer_mod
import parser as parser_mod

from SyntaxException import *
from CodeGenerator import *
from Identifier import *

class Compiler:

	def __init__(self, DEBUG = False):
		self.DEBUG = DEBUG

		# Set up a logging object
		logging.basicConfig(
		    level = logging.DEBUG,
		    filename = "parselog.txt",
		    filemode = "w",
		    format = "%(filename)10s:%(lineno)4d:%(message)s"
		)
		self.log = logging.getLogger()

		self.lexer = lex.lex(module=lexer_mod, debug=False, optimize=False)
		self.parser = yacc.yacc(module=parser_mod, debug=True, optimize=False)
		self.parser.defaulted_states = {}

	def compile(self, doc):

		res = ""
		lines = doc.split("\n")
		result = None
		parsing = True
		msg = None
		new_comma = []

		try:
			result = self.parser.parse(doc, debug=self.log)

			if not self.DEBUG:
				try:
					codeGenerator = CodeGenerator()
					response = result.generateCode(codeGenerator)
					res += response

				except:
					res += "Error while generating MathProg code. Please, check your Latex code!"

			else:
				if self.DEBUG:
					res += str(result)

				codeGenerator = CodeGenerator()
				response = result.generateCode(codeGenerator)
				res += response

		except SyntaxException as msg:

			if msg[0] == "EOF":
				res += "Syntax error at EOF."
			else:
				
				lineNum = msg[0]-1
				print("lineNum", lineNum, msg)
				line = lines[lineNum]

				totalCharLinesAbove = 0
				lineNum -= 1
				while lineNum >= 0:
					totalCharLinesAbove += len(lines[lineNum])+1
					lineNum -= 1
				
				# If a COMMA was inserted after an Identifier (see above), 
				# then the real position of the character that caused the error must be discounted by this COMMA
				# (the original document has not this automatically inserted COMMA)
				pos_aux = msg[1]
				pos = pos_aux-totalCharLinesAbove
				if totalCharLinesAbove > 0:
					pos += 1

				res += "Syntax error at line %d, position %d: '%s'.\nContext: %s." % (msg[0], pos, msg[2], line)

		return res
