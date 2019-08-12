#!/usr/bin/python -tt

# List of token names.   This is always required

from Number import *
from Infinity import *

import sys
import re
from SyntaxException import *

reserved = {
}

tokens = [
   'FRAC',
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'LBRACKET',
   'RBRACKET',
   'LBRACE',
   'RBRACE',
   'LFLOOR',
   'RFLOOR',
   'LCEIL',
   'RCEIL',
   'ASINH',
   'SINH',
   'ASIN',
   'SIN',
   'ACOSH',
   'COSH',
   'ACOS',
   'COS',
   'ATANH',
   'TANH',
   'ATAN',
   'TAN',
   'ASEC',
   'SEC',
   'ACSC',
   'CSC',
   'ACOTH',
   'COTH',
   'ACOT',
   'COT',
   'SQRT',
   'LOG',
   'LN',
   'EXP',
   'MOD',
   'CARET',
   'COMMA',
   'ID',
   'PIPE',
   'INFINITY',
   'UNDERLINE',
   'INTEGRAL',
   'DIFFERENTIAL',
   'D', 
   'PARTIAL',
   'SUM',
   'PROD', 
   'IN', 
   'DOTS',
   'EQ',
   'NEQ',
   'LT',
   'LE',
   'GT',
   'GE',
   'FACTORIAL',
   'PERCENT',
   'PI',
   'LIMIT',
   'TO'
] + list(reserved.values())

# Define a rule so we can track line numbers
def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\r'

t_UNDERLINE = r'_'

def t_LIMIT(t):
   r'\\lim'
   return t

def t_TO(t):
   r'\\to'
   return t

t_PI = r'\\pi'

t_EQ = r'='
t_NEQ = r'\\neq'
t_LE = r'\\leq'
t_LT = r'<'
t_GE = r'\\geq'
t_GT = r'>'

t_SUM = r'\\sum'
t_PROD = r'\\prod'
t_IN = r'\\in'
t_FACTORIAL = r'!'

def t_PERCENT(t):
   r'\\text\{\s*\%\s*\}'
   return t

def t_MOD(t):
   r'\\mod|\\bmod'
   return t

def t_DOTS(t):
   r'\\cdots|\\ldots|\\dots|\.\.\.'
   return t

def t_INFINITY(t):
   r'\\infty'
   t.value = Infinity()
   return t

def t_COMMENT(t):
    r'\%[^\n]*'
    pass

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'

def t_TIMES(t):
   r'\*|\\cdot|\\ast'
   return t

def t_DIVIDE(t):
   r'/|\\div'
   return t

def t_FRAC(t):
   r'\\frac'
   return t

t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_LBRACKET(t):
   r'\['
   return t

def t_RBRACKET(t):
   r'\]'
   return t

def t_LBRACE(t):
   r'\{'
   return t

def t_RBRACE(t):
   r'\}'
   return t

t_CARET = r'\^'
t_LFLOOR = r'\\lfloor'
t_RFLOOR = r'\\rfloor'
t_LCEIL = r'\\lceil'
t_RCEIL = r'\\rceil'
t_ASINH = r'\\sinh\^\{-1\}'
t_ASIN  = r'\\sin\^\{-1\}|\\arcsin'
t_SINH  = r'\\sinh'
t_SIN   = r'\\sin'
t_ACOSH = r'\\cosh\^\{-1\}'
t_ACOS  = r'\\cos\^\{-1\}|\\arccos'
t_COSH  = r'\\cosh'
t_COS   = r'\\cos'
t_ATANH = r'\\tanh\^\{-1\}'
t_ATAN  = r'\\tan\^\{-1\}|\\arctan'
t_TANH  = r'\\tanh'
t_TAN   = r'\\tan'
t_ASEC  = r'\\sec\^\{-1\}'
t_SEC   = r'\\sec'
t_ACSC  = r'\\csc\^\{-1\}'
t_CSC   = r'\\csc'
t_ACOTH = r'\\coth\^\{-1\}'
t_ACOT  = r'\\cot\^\{-1\}'
t_COTH  = r'\\coth'
t_COT   = r'\\cot'
t_SQRT  = r'\\sqrt'
t_LOG   = r'\\log'
t_LN    = r'\\ln'
t_EXP   = r'\\exp'

def t_INTEGRAL(t):
   r'\\int'
   return t

def t_D(t):
   r'd(?!\\_|[a-zA-Z0-9])'
   return t

def t_DIFFERENTIAL(t):
   r'd[a-zA-Z](?!\\_|[a-zA-Z0-9])'
   return t

def t_PARTIAL(t):
   r'\\partial'
   return t

def t_PIPE(t):
   r'\\mid|\\vert|\|'
   return t

def t_ignore_LIMITS(t):
   r'\\limits'
   pass

def t_ignore_BEGIN(t):
   r'\\begin\{[a-zA-Z][a-zA-Z0-9]*[\*]?\}[\{\[][a-zA-Z0-9][a-zA-Z0-9]*[\*]?[\}\]]|\\begin\{[a-zA-Z][a-zA-Z0-9]*[\*]?\}'
   pass

def t_ignore_END(t):
   r'\\end\{[a-zA-Z][a-zA-Z0-9]*[\*]?\}[\{\[][a-zA-Z0-9][a-zA-Z0-9]*[\*]?[\}\]]|\\end\{[a-zA-Z][a-zA-Z0-9]*[\*]?\}'
   pass

def t_ignore_BEGIN_EQUATION(t):
   r'\\begin\{equation\}'
   pass

def t_ignore_END_EQUATION(t):
   r'\\end\{equation\}'
   pass

def t_ignore_BEGIN_SPLIT(t):
   r'\\begin\{split\}'
   pass

def t_ignore_END_SPLIT(t):
   r'\\end\{split\}'
   pass

def t_ignore_DISPLAYSTYLE(t):
   r'\\displaystyle'
   pass

def t_ignore_QUAD(t):
   r'\\quad'
   pass

def t_ignore_MATHCLAP(t):
   r'\\mathclap'
   pass

def t_ignored_LEFT(t):
   r'\\left'
   pass

def t_ignored_RIGHT(t):
   r'\\right'
   pass

t_COMMA = r','

def t_ignore_BACKSLASHES(t):
   r'\\\\'
   pass

def t_ID(t):
   r'\\text\{\s*(\\_)*[a-zA-Z]((\\_)*[a-zA-Z0-9]*)*\s*\}|(\\_)*[a-zA-Z]((\\_)*[a-zA-Z0-9]*)*'
   t.type = reserved.get(t.value, 'ID') # Check for reserved words

   m = re.search(r"\\text\{\s*(.+)\s*\}", t.value)

   if m:
      t.value = m.groups(0)[0]

   t.value = t.value.replace("\\", "").strip()

   return t

# A regular expression rule with some action code
def t_NUMBER(t):
   r'[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
   t.value = Number(t.value)
   return t

def t_ignore_TEXT(t):
    r'\\text\{\s*\}|\\text'
    pass

# Error handling rule
def t_error(t):
   sys.stderr.write( "Illegal character '%s'" % t.value[0] )
   t.lexer.skip(1)
