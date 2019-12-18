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
   'I', 
   'E',
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
   'ETA_LOWER',
   'ZETA_LOWER',
   'PHI_LOWER',
   'PSI_LOWER',
   'SIGMA_LOWER',
   'DELTA_LOWER',
   'THETA_LOWER',
   'LAMBDA_LOWER',
   'EPSILON_LOWER',
   'TAU_LOWER',
   'KAPPA_LOWER',
   'OMEGA_LOWER',
   'ALPHA_LOWER',
   'XI_LOWER',
   'CHI_LOWER',
   'NU_LOWER',
   'RHO_LOWER',
   'OMICRON_LOWER',
   'UPSILON_LOWER',
   'IOTA_LOWER',
   'BETA_LOWER',
   'GAMMA_LOWER',
   'MU_LOWER',
   'PI_UPPER',
   'PI',
   'BETA',
   'GAMMA',
   'LIMIT',
   'TO',
   'PRIME',
   'GCD',
   'DEG',
   'CHOOSE',
   'GRADIENT',
   'LAPLACIAN',
   'BEGIN_CASE',
   'END_CASE',
   'BACKSLASHES',
   'BEGIN_BMATRIX',
   'END_BMATRIX',
   'BEGIN_PMATRIX',
   'END_PMATRIX',
   'BEGIN_VMATRIX',
   'END_VMATRIX',
   'BEGIN_NMATRIX',
   'END_NMATRIX',
   'AMPERSAND',
   'DETERMINANT',
   'CROSS',
   'DOT'
] + list(reserved.values())

# Define a rule so we can track line numbers
def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\r'

t_UNDERLINE = r'_'

def t_PRIME(t):
   r'\\prime|\''
   return t

def t_LIMIT(t):
   r'\\lim'
   return t

def t_TO(t):
   r'\\to'
   return t

t_PHI_LOWER = r'\\phi'
t_SIGMA_LOWER = r'\\sigma'
t_ETA_LOWER = r'\\eta'
t_ZETA_LOWER = r'\\zeta'
t_PSI_LOWER = r'\\psi'
t_DELTA_LOWER = r'\\delta'
t_THETA_LOWER = r'\\theta'
t_LAMBDA_LOWER = r'\\lambda'
t_EPSILON_LOWER = r'\\epsilon'
t_TAU_LOWER = r'\\tau'
t_KAPPA_LOWER = r'\\kappa'
t_OMEGA_LOWER = r'\\omega'
t_ALPHA_LOWER = r'\\alpha'
t_XI_LOWER = r'\\xi'
t_CHI_LOWER = r'\\chi'
t_NU_LOWER = r'\\nu'
t_RHO_LOWER = r'\\rho'
t_OMICRON_LOWER = r'\\omicron'
t_UPSILON_LOWER = r'\\upsilon'
t_IOTA_LOWER = r'\\iota'
t_BETA_LOWER = r'\\beta'
t_GAMMA_LOWER = r'\\gamma'
t_MU_LOWER = r'\\mu'
t_BETA = r'\\Beta'
t_GAMMA = r'\\Gamma'
t_PI = r'\\pi'
t_PI_UPPER = r'\\Pi'

t_EQ = r'='
t_NEQ = r'\\neq'
t_LE = r'\\leq'
t_LT = r'<'
t_GE = r'\\geq'
t_GT = r'>'

t_CROSS = r'\\times'
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
   r'\*|\\ast'
   return t

def t_DOT(t):
   r'\\cdot'
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

t_CARET  = r'\^'
t_LFLOOR = r'\\lfloor'
t_RFLOOR = r'\\rfloor'
t_LCEIL  = r'\\lceil'
t_RCEIL  = r'\\rceil'
t_ASINH  = r'\\sinh\^\{-1\}'
t_ASIN   = r'\\sin\^\{-1\}|\\arcsin'
t_SINH   = r'\\sinh'
t_SIN    = r'\\sin'
t_ACOSH  = r'\\cosh\^\{-1\}'
t_ACOS   = r'\\cos\^\{-1\}|\\arccos'
t_COSH   = r'\\cosh'
t_COS    = r'\\cos'
t_ATANH  = r'\\tanh\^\{-1\}'
t_ATAN   = r'\\tan\^\{-1\}|\\arctan'
t_TANH   = r'\\tanh'
t_TAN    = r'\\tan'
t_ASEC   = r'\\sec\^\{-1\}'
t_SEC    = r'\\sec'
t_ACSC   = r'\\csc\^\{-1\}'
t_CSC    = r'\\csc'
t_ACOTH  = r'\\coth\^\{-1\}'
t_ACOT   = r'\\cot\^\{-1\}'
t_COTH   = r'\\coth'
t_COT    = r'\\cot'
t_SQRT   = r'\\sqrt'
t_LOG    = r'\\log'
t_LN     = r'\\ln'
t_EXP    = r'\\exp'
t_GCD    = r'\\gcd'
t_DEG    = r'\\deg'
t_CHOOSE = r'\\choose'
t_GRADIENT = r'\\nabla'
t_LAPLACIAN = r'\\Delta'
t_AMPERSAND = r'&'
t_DETERMINANT = r'\\det'

def t_BEGIN_CASE(t):
   r'\\begin\{cases\}'
   return t

def t_END_CASE(t):
   r'\\end\{cases\}'
   return t

def t_BEGIN_BMATRIX(t):
   r'\\begin\{bmatrix\}'
   return t

def t_END_BMATRIX(t):
   r'\\end\{bmatrix\}'
   return t

def t_BEGIN_PMATRIX(t):
   r'\\begin\{pmatrix\}'
   return t

def t_END_PMATRIX(t):
   r'\\end\{pmatrix\}'
   return t

def t_BEGIN_VMATRIX(t):
   r'\\begin\{vmatrix\}'
   return t

def t_END_VMATRIX(t):
   r'\\end\{vmatrix\}'
   return t

def t_BEGIN_NMATRIX(t):
   r'\\begin\{Vmatrix\}'
   return t

def t_END_NMATRIX(t):
   r'\\end\{Vmatrix\}'
   return t

def t_BACKSLASHES(t):
   r'\\\\'
   return t

def t_INTEGRAL(t):
   r'\\int'
   return t

def t_D(t):
   r'd(?!\\_|[a-zA-Z0-9])'
   return t

def t_I(t):
   r'i(?!\\_|[a-zA-Z0-9])'
   return t

def t_E(t):
   r'e(?!\\_|[a-zA-Z0-9])'
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
