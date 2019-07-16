#!/usr/bin/python -tt

from lexer import tokens

from Main import *
from Expression import *
from Integral import *
from Derivative import *
from Identifier import *
from FunctionName import *
from BinaryOperator import *
from ID import *
from SyntaxException import *

import objects as obj

precedence = (
    ('left', 'ID'),
    ('left', 'NUMBER', 'INFINITY'),
    ('left', 'INTEGRAL', 'DIFFERENTIAL', 'D', 'PARTIAL'),
    ('right', 'COMMA'),
    ('right', 'PIPE'),
    ('right', 'LPAREN', 'RPAREN'),
    ('right', 'LBRACE', 'RBRACE', 'FRAC'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'CARET'),
    ('left', 'LFLOOR', 'RFLOOR', 'LCEIL', 'RCEIL', 'SIN', 'COS', 'TAN', 'ATAN', 'SQRT', 'LN', 'LOG', 'EXP')
)

def p_Main(t):
  '''MAIN : Expression'''
  t[0] = Main(t[1])

def p_Factor(t):
  '''Factor : NUMBER
            | ID
            | INFINITY
            | Derivative
            | Integral
            | LPAREN Expression RPAREN'''

  if len(t) > 2:
    t[0] = ExpressionBetweenParenthesis(t[2])
    
  else:
    if t.slice[1].type == "ID":
      t[1] = Identifier(ID(t[1]))

    t[0] = t[1]

def p_Term(t):
  '''Term : Term TIMES Factor
          | Term DIVIDE Factor
          | Term MOD Factor
          | Term CARET LBRACE Expression RBRACE
          | Factor'''

  if len(t) == 2:
      t[0] = t[1]

  else:
    _type = t.slice[2].type
    if _type == "TIMES":
        op = BinaryOperator(BinaryOperator.TIMES)

    elif _type == "DIVIDE":
        op = BinaryOperator(BinaryOperator.DIV)

    elif _type == "MOD":
        op = BinaryOperator(BinaryOperator.MOD)

    elif _type == "CARET":
        op = BinaryOperator(BinaryOperator.POW)

    if _type == "CARET":
      t[0] = ExpressionWithArithmeticOperation(op, t[1], t[4])
    else:
      t[0] = ExpressionWithArithmeticOperation(op, t[1], t[3])


def p_Expression_binop(t):
    '''Expression : Expression PLUS Term
                  | Expression MINUS Term
                  | Term'''

    if len(t) == 2:
      t[0] = t[1]

    else:
      _type = t.slice[2].type
      if _type == "PLUS":
          op = BinaryOperator(BinaryOperator.PLUS)

      elif _type == "MINUS":
          op = BinaryOperator(BinaryOperator.MINUS)

      t[0] = ExpressionWithArithmeticOperation(op, t[1], t[3])

def p_FractionalExpression(t):
    '''Factor : FRAC LBRACE Expression RBRACE LBRACE Expression RBRACE'''

    t[0] = FractionalExpression(t[3], t[6])

def p_FunctionExpression(t):
    '''Factor : SQRT LBRACE Expression RBRACE

              | SQRT LBRACKET NUMBER RBRACKET LBRACE Expression RBRACE
                         
              | LFLOOR Expression RFLOOR
                         
              | LCEIL Expression RCEIL
                         
              | PIPE Expression PIPE
                         
              | SIN LPAREN Expression RPAREN
                         
              | COS LPAREN Expression RPAREN

              | TAN LPAREN Expression RPAREN
                         
              | ATAN LPAREN Expression COMMA Expression RPAREN
              | ATAN LPAREN Expression RPAREN
                         
              | LOG LPAREN Expression RPAREN
                         
              | LN LPAREN Expression RPAREN
                         
              | EXP LPAREN Expression RPAREN

              | ID LPAREN ExpressionList RPAREN

              | ID LPAREN RPAREN'''

    _type = t.slice[1].type
    if _type == "SQRT":
        function = FunctionName(FunctionName.SQRT)

    elif _type == "LFLOOR":
        function = FunctionName(FunctionName.FLOOR)

    elif _type == "LCEIL":
        function = FunctionName(FunctionName.CEIL)

    elif _type == "PIPE":
        function = FunctionName(FunctionName.ABS)

    elif _type == "SIN":
        function = FunctionName(FunctionName.SIN)

    elif _type == "COS":
        function = FunctionName(FunctionName.COS)

    elif _type == "LOG":
        function = FunctionName(FunctionName.LOG)

    elif _type == "LN":
        function = FunctionName(FunctionName.LN)

    elif _type == "EXP":
        function = FunctionName(FunctionName.EXP)

    elif _type == "TAN":
        function = FunctionName(FunctionName.TAN)

    elif _type == "ATAN":
        function = FunctionName(FunctionName.ATAN)

    else:
      function = FunctionName(Identifier(ID(t[1])))

    if len(t) > 5:

      if _type == "SQRT":
        t[0] = ExpressionWithFunction(function, t[6], t[3])
      else:
        t[0] = ExpressionWithFunction(function, t[3], t[5])

    elif len(t) > 4:
      t[0] = ExpressionWithFunction(function, t[3])
        
    else:
      if t.slice[2].type == "LPAREN":
        t[0] = ExpressionWithFunction(function)
      else:
        t[0] = ExpressionWithFunction(function, t[2])

def p_Integral(t):
    '''Integral : INTEGRAL UNDERLINE LBRACE Expression RBRACE CARET LBRACE Expression RBRACE Expression DIFFERENTIAL
                | INTEGRAL UNDERLINE LBRACE Expression RBRACE Expression DIFFERENTIAL
                | INTEGRAL CARET LBRACE Expression RBRACE Expression DIFFERENTIAL
                | INTEGRAL Expression DIFFERENTIAL'''

    if len(t) > 8:
      t[0] = Integral(t[10], t[11][1:], t[4], t[8])

    elif len(t) > 4:

      if t.slice[2].type == "UNDERLINE":
        t[0] = Integral(t[6], t[7][1:], t[4])

      else:
        t[0] = Integral(t[6], t[7][1:], None, t[4])

    else:
      t[0] = Integral(t[2], t[3][1:])

def p_Derivative1(t):
    '''Derivative : FRAC LBRACE D RBRACE LBRACE DIFFERENTIAL RBRACE Expression
                  | FRAC LBRACE D CARET LBRACE NUMBER RBRACE RBRACE LBRACE DIFFERENTIAL CARET LBRACE NUMBER RBRACE RBRACE Expression'''

    if len(t) > 9:
      t[0] = Derivative(t[10][1:], t[16], t[6])

    else:
      t[0] = Derivative(t[6][1:], t[8])

def p_Derivative2(t):
    '''Derivative : FRAC LBRACE D Expression RBRACE LBRACE DIFFERENTIAL RBRACE
                  | FRAC LBRACE D CARET LBRACE NUMBER RBRACE Expression RBRACE LBRACE DIFFERENTIAL CARET LBRACE NUMBER RBRACE RBRACE'''

    if len(t) > 9:
      t[0] = Derivative(t[11][1:], t[8], t[6])

    else:
      t[0] = Derivative(t[7][1:], t[4])

def p_Derivative3(t):
    '''Derivative : FRAC LBRACE PARTIAL RBRACE LBRACE PARTIAL ID RBRACE Expression
                  | FRAC LBRACE PARTIAL CARET LBRACE NUMBER RBRACE RBRACE LBRACE PARTIAL ID CARET LBRACE NUMBER RBRACE RBRACE Expression'''

    if len(t) > 10:
      t[0] = Derivative(t[11][:1], t[17], t[6])

    else:
      t[0] = Derivative(t[7][:1], t[9])

def p_Derivative4(t):
    '''Derivative : FRAC LBRACE PARTIAL Expression RBRACE LBRACE PARTIAL ID RBRACE
                  | FRAC LBRACE PARTIAL CARET LBRACE NUMBER RBRACE Expression RBRACE LBRACE PARTIAL ID CARET LBRACE NUMBER RBRACE RBRACE'''

    if len(t) > 10:
      t[0] = Derivative(t[12][:1], t[8], t[6])

    else:
      t[0] = Derivative(t[8][:1], t[4])


def p_ExpessionList(t):
  '''ExpressionList : ExpressionList COMMA Expression
                    | Expression'''

  if len(t) == 2:
    t[0] = ExpressionList([t[1]])

  else:
    t[1].add(t[3])
    t[0] = t[1]

def p_error(t):
  if t:
    raise SyntaxException(t.lineno, t.lexpos, t.value, t)
  else:
    raise SyntaxException("EOF")
