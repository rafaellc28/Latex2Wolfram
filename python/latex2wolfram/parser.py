#!/usr/bin/python -tt

from lexer import tokens

from Main import *
from Expression import *
from Integral import *
from Identifier import *
from ID import *
from SyntaxException import *

import objects as obj

precedence = (
    ('left', 'ID'),
    ('left', 'NUMBER', 'INFINITY'),
    ('left', 'INTEGRAL', 'DIFFERENTIAL'),
    ('right', 'COMMA'),
    ('right', 'PIPE'),
    ('right', 'LPAREN', 'RPAREN'),
    ('right', 'LBRACE', 'RBRACE', 'FRAC'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD', 'QUOTIENT'),
    ('right', 'CARET'),
    ('left', 'LFLOOR', 'RFLOOR', 'LCEIL', 'RCEIL', 'SIN', 'COS', 'TAN', 'ATAN', 'SQRT', 'LN', 'LOG', 'EXP')
)

def p_Main(t):
  '''MAIN : Expression'''
  t[0] = Main(t[1])

def p_Factor(t):
  '''Factor : NUMBER
            | Identifier
            | INFINITY
            | LPAREN Expression RPAREN'''

  if len(t) > 2:
    t[0] = ExpressionBetweenParenthesis(t[2])
    
  else:
    t[0] = ValuedExpression(t[1])

def p_Term(t):
  '''Term : Term TIMES Factor
          | Term DIVIDE Factor
          | Term MOD Factor
          | Term QUOTIENT Factor
          | Term CARET LBRACE Factor RBRACE
          | Factor'''

  if len(t) == 2:
      t[0] = t[1]

  else:
    _type = t.slice[2].type
    if _type == "TIMES":
        op = ExpressionWithArithmeticOperation.TIMES

    elif _type == "QUOTIENT":
        op = ExpressionWithArithmeticOperation.QUOT

    elif _type == "DIVIDE":
        op = ExpressionWithArithmeticOperation.DIV

    elif _type == "MOD":
        op = ExpressionWithArithmeticOperation.MOD

    elif _type == "CARET":
        op = ExpressionWithArithmeticOperation.POW

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
          op = ExpressionWithArithmeticOperation.PLUS

      elif _type == "MINUS":
          op = ExpressionWithArithmeticOperation.MINUS

      t[0] = ExpressionWithArithmeticOperation(op, t[1], t[3])

def p_FractionalExpression(t):
    '''Expression : FRAC LBRACE Expression RBRACE LBRACE Expression RBRACE'''

    t[0] = FractionalExpression(t[3], t[6])

def p_FunctionExpression(t):
    '''Factor : SQRT LBRACE Expression RBRACE
                         
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

              | Identifier LPAREN ExpressionList RPAREN

              | Identifier LPAREN RPAREN'''

    _type = t.slice[1].type
    if _type == "SQRT":
        op = ExpressionWithFunction.SQRT

    elif _type == "LFLOOR":
        op = ExpressionWithFunction.FLOOR

    elif _type == "LCEIL":
        op = ExpressionWithFunction.CEIL

    elif _type == "PIPE":
        op = ExpressionWithFunction.ABS

    elif _type == "SIN":
        op = ExpressionWithFunction.SIN

    elif _type == "COS":
        op = ExpressionWithFunction.COS

    elif _type == "LOG":
        op = ExpressionWithFunction.LOG

    elif _type == "LN":
        op = ExpressionWithFunction.LN

    elif _type == "EXP":
        op = ExpressionWithFunction.EXP

    elif _type == "TAN":
        op = ExpressionWithFunction.TAN

    elif _type == "ATAN":
        op = ExpressionWithFunction.ATAN

    else:
      op = t[1]

    if len(t) > 5:
        t[0] = ExpressionWithFunction(op, t[3], t[5])

    elif len(t) > 4:
        t[0] = ExpressionWithFunction(op, t[3])
        
    else:
        if t.slice[2].type == "LPAREN":
          t[0] = ExpressionWithFunction(op)
        else:
          t[0] = ExpressionWithFunction(op, t[2])

def p_Integral(t):
    '''Factor : INTEGRAL UNDERLINE LBRACE Expression RBRACE CARET LBRACE Expression RBRACE Expression DIFFERENTIAL'''
    t[0] = Integral(t[4], t[8], t[10], t[11][1:])

def p_Identifier(t):
    '''Identifier : ID'''
    t[0] = Identifier(ID(t[1]))

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
