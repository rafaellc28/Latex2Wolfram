#!/usr/bin/python -tt

from lexer import tokens

from Main import *
from IndexingExpression import *
from Expression import *
from Integral import *
from Derivative import *
from DifferentialVariable import *
from Limit import *
from Identifier import *
from FunctionName import *
from UnaryOperator import *
from BinaryOperator import *
from IteratedOperator import *
from Constraint import *
from ConstraintOperator import *
from Symbol import *
from ID import *
from SyntaxException import *

precedence = (
    ('left', 'ID'),
    ('left', 'NUMBER', 'INFINITY'),
    ('left', 'INTEGRAL', 'DIFFERENTIAL', 'D', 'PARTIAL', 'LIMIT', 'TO'),
    ('right', 'COMMA'),
    ('right', 'PIPE'),
    ('right', 'LPAREN', 'RPAREN'),
    ('right', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'FRAC'),
    ('left', 'PI', 'PRIME'),
    ('right', 'LE', 'GE', 'LT', 'GT', 'EQ', 'NEQ'),
    ('left', 'IN'),
    ('right', 'DOTS'),
    ('left', 'SUM', 'PROD'),
    ('left', 'FACTORIAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('left', 'UPLUS', 'UMINUS'),
    ('right', 'CARET'),
    ('left', 'LFLOOR', 'RFLOOR', 'LCEIL', 'RCEIL', 'SINH', 'ASINH', 'SIN', 'ASIN', 'COSH', 'ACOSH', 'COS', 'ACOS', 'TANH', 'ATANH', 'TAN', 'ATAN'
      , 'SEC', 'ASEC', 'CSC', 'ACSC', 'COTH', 'ACOTH', 'COT', 'ACOT', 'SQRT', 'LN', 'LOG', 'EXP')
)

def p_Main(t):
  '''MAIN : Expression
          | Constraint'''
  t[0] = Main(t[1])

def p_Factor(t):
  '''Factor : NUMBER
            | ID
            | INFINITY
            | IteratedExpression
            | Derivative
            | Integral
            | Limit
            | DifferentialVariable
            | ID CARET LBRACE Expression RBRACE
            | LPAREN Expression RPAREN'''

  if len(t) > 4:
    t[1] = Identifier(ID(t[1]))
    t[0] = ExpressionWithBinaryOperation(BinaryOperator(BinaryOperator.POW), t[1], t[4])

  elif len(t) > 2:
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
      t[0] = ExpressionWithBinaryOperation(op, t[1], t[4])
    else:
      t[0] = ExpressionWithBinaryOperation(op, t[1], t[3])


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

      t[0] = ExpressionWithBinaryOperation(op, t[1], t[3])

def p_UnaryExpressionOperatorBefore(t):
    '''Factor : PLUS ID %prec UPLUS
              | PLUS NUMBER %prec UPLUS
              | PLUS LPAREN Expression RPAREN %prec UPLUS
              | MINUS ID %prec UMINUS
              | MINUS NUMBER %prec UMINUS
              | MINUS LPAREN Expression RPAREN %prec UMINUS'''

    if t.slice[1].type == "PLUS":
      op = UnaryOperator.PLUS
    else:
      op = UnaryOperator.MINUS

    if len(t) > 3:
      t[0] = ExpressionWithUnaryOperation(UnaryOperator(op), ExpressionBetweenParenthesis(t[3]))

    else:
      if t.slice[2].type == "ID":
        t[2] = Identifier(ID(t[2]))

      t[0] = ExpressionWithUnaryOperation(UnaryOperator(op), t[2])

def p_UnaryExpressionOperatorAfter(t):
    '''Factor : NUMBER FACTORIAL
              | ID FACTORIAL
              | LPAREN Expression RPAREN FACTORIAL
              | NUMBER PERCENT
              | ID PERCENT
              | LPAREN Expression RPAREN PERCENT'''

    if t.slice[1].type == "ID":
      t[1] = Identifier(ID(t[1]))

    if len(t) > 3:
      if t.slice[4].type == "FACTORIAL":
        op = UnaryOperator.FACTORIAL
      else:
        op = UnaryOperator.PERCENT

      t[0] = ExpressionWithUnaryOperation(UnaryOperator(op), ExpressionBetweenParenthesis(t[2]), True)
    else:
      if t.slice[2].type == "FACTORIAL":
        op = UnaryOperator.FACTORIAL
      else:
        op = UnaryOperator.PERCENT

      t[0] = ExpressionWithUnaryOperation(UnaryOperator(op), t[1], True)

def p_FractionalExpression(t):
    '''Factor : FRAC LBRACE Expression RBRACE LBRACE Expression RBRACE'''

    t[0] = FractionalExpression(t[3], t[6])

def p_FunctionExpression(t):
    '''Factor : SQRT LBRACE Expression RBRACE

              | SQRT LBRACKET NUMBER RBRACKET LBRACE Expression RBRACE
                         
              | LFLOOR Expression RFLOOR
                         
              | LCEIL Expression RCEIL
                         
              | PIPE Expression PIPE

              | ASINH LPAREN Expression RPAREN
              
              | ASINH ID

              | ASINH NUMBER

              | SINH LPAREN Expression RPAREN
              
              | SINH ID

              | SINH NUMBER
              
              | ASIN LPAREN Expression RPAREN

              | ASIN ID

              | ASIN NUMBER

              | SIN LPAREN Expression RPAREN
              
              | SIN ID

              | SIN NUMBER

              | ACOSH LPAREN Expression RPAREN

              | ACOSH ID

              | ACOSH NUMBER

              | COSH LPAREN Expression RPAREN

              | COSH ID

              | COSH NUMBER

              | ACOS LPAREN Expression RPAREN

              | ACOS ID

              | ACOS NUMBER

              | COS LPAREN Expression RPAREN

              | COS ID

              | COS NUMBER

              | ATANH LPAREN Expression RPAREN

              | ATANH ID

              | ATANH NUMBER

              | TANH LPAREN Expression RPAREN

              | TANH ID

              | TANH NUMBER

              | ATAN LPAREN Expression COMMA Expression RPAREN
              | ATAN LPAREN Expression RPAREN
  
              | ATAN ID

              | ATAN NUMBER

              | TAN LPAREN Expression RPAREN

              | TAN ID

              | TAN NUMBER

              | ASEC LPAREN Expression RPAREN

              | ASEC ID

              | ASEC NUMBER

              | SEC LPAREN Expression RPAREN
              
              | SEC ID

              | SEC NUMBER

              | ACSC LPAREN Expression RPAREN

              | ACSC ID

              | ACSC NUMBER

              | CSC LPAREN Expression RPAREN

              | CSC ID

              | CSC NUMBER

              | ACOTH LPAREN Expression RPAREN

              | ACOTH ID

              | ACOTH NUMBER

              | COTH LPAREN Expression RPAREN

              | COTH ID

              | COTH NUMBER

              | ACOT LPAREN Expression RPAREN

              | ACOT ID

              | ACOT NUMBER

              | COT LPAREN Expression RPAREN

              | COT ID

              | COT NUMBER
                         
              | LOG LPAREN Expression RPAREN

              | LOG ID

              | LOG NUMBER

              | LOG UNDERLINE LBRACE NUMBER RBRACE LPAREN Expression RPAREN
                         
              | LN LPAREN Expression RPAREN

              | LN ID

              | LN NUMBER
                         
              | EXP LPAREN Expression RPAREN

              | EXP ID

              | EXP NUMBER

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

    elif _type == "ASINH":
        function = FunctionName(FunctionName.ASINH)

    elif _type == "SINH":
        function = FunctionName(FunctionName.SINH)

    elif _type == "ASIN":
        function = FunctionName(FunctionName.ASIN)

    elif _type == "SIN":
        function = FunctionName(FunctionName.SIN)

    elif _type == "ACOSH":
        function = FunctionName(FunctionName.ACOSH)

    elif _type == "COSH":
        function = FunctionName(FunctionName.COSH)

    elif _type == "ACOS":
        function = FunctionName(FunctionName.ACOS)

    elif _type == "COS":
        function = FunctionName(FunctionName.COS)

    elif _type == "ATANH":
        function = FunctionName(FunctionName.ATANH)

    elif _type == "TANH":
        function = FunctionName(FunctionName.TANH)

    elif _type == "ATAN":
        function = FunctionName(FunctionName.ATAN)

    elif _type == "TAN":
        function = FunctionName(FunctionName.TAN)

    elif _type == "ASEC":
        function = FunctionName(FunctionName.ASEC)

    elif _type == "SEC":
        function = FunctionName(FunctionName.SEC)

    elif _type == "ACSC":
        function = FunctionName(FunctionName.ACSC)

    elif _type == "CSC":
        function = FunctionName(FunctionName.CSC)

    elif _type == "ACOTH":
        function = FunctionName(FunctionName.ACOTH)

    elif _type == "COTH":
        function = FunctionName(FunctionName.COTH)

    elif _type == "ACOT":
        function = FunctionName(FunctionName.ACOT)

    elif _type == "COT":
        function = FunctionName(FunctionName.COT)

    elif _type == "LOG":
        function = FunctionName(FunctionName.LOG)

    elif _type == "LN":
        function = FunctionName(FunctionName.LN)

    elif _type == "EXP":
        function = FunctionName(FunctionName.EXP)

    else:
      function = FunctionName(Identifier(ID(t[1])))

    if len(t) > 5:

      if _type == "LOG":
        t[0] = ExpressionWithFunction(function, t[7], t[4])

      elif _type == "SQRT":
        t[0] = ExpressionWithFunction(function, t[6], t[3])
        
      else:
        t[0] = ExpressionWithFunction(function, t[3], t[5])

    elif len(t) > 4:
      t[0] = ExpressionWithFunction(function, t[3])
        
    else:

      if t.slice[2].type == "LPAREN":
        t[0] = ExpressionWithFunction(function)

      else:
        if t.slice[2].type == "ID":
          t[2] = Identifier(ID(t[2]))

        t[0] = ExpressionWithFunction(function, t[2])

def p_Range(t):
    '''Range : Expression DOTS Expression'''
    t[0] = Range(t[1], t[3])

def p_IndexingExpression(t):
    '''IndexingExpression : ID IN Range'''
    t[0] = IndexingExpression(Identifier(ID(t[1])), t[3])

def p_IteratedExpression(t):
    '''IteratedExpression : SUM UNDERLINE LBRACE IndexingExpression RBRACE Expression
                          | SUM UNDERLINE LBRACE ID EQ Expression RBRACE CARET LBRACE Expression RBRACE Expression
                          | PROD UNDERLINE LBRACE IndexingExpression RBRACE Expression
                          | PROD UNDERLINE LBRACE ID EQ Expression RBRACE CARET LBRACE Expression RBRACE Expression'''

    _type = t.slice[1].type
    if _type == "SUM":
      op = IteratedOperator(IteratedOperator.SUM)
    else:
      op = IteratedOperator(IteratedOperator.PROD)

    if len(t) > 7:
      _range = Range(t[6], t[10])
      indexingExpression = IndexingExpression(Identifier(ID(t[4])), _range)

      t[0] = IteratedExpression(op, t[12], indexingExpression)
    else:
      t[0] = IteratedExpression(op, t[6], t[4])

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

def p_DifferentialVariable1(t):
  '''DifferentialVariable : ID PrimeList LPAREN ExpressionList RPAREN
                          | ID PrimeList'''

  if len(t) > 3:
    t[0] = DifferentialVariable(Identifier(ID(t[1])), t[2], t[4])

  else:
    t[0] = DifferentialVariable(Identifier(ID(t[1])), t[2])

def p_DifferentialVariable2(t):
  '''DifferentialVariable : ID CARET LBRACE LPAREN NUMBER RPAREN RBRACE LPAREN ExpressionList RPAREN
                          | ID CARET LBRACE LPAREN NUMBER RPAREN RBRACE'''

  isOrder = False

  try:
    order = int(t[5].getNumber())
    isOrder = True
  except Exception as msg:
    order = t[5]

  if isOrder:

    if order > 0:
      primeList = [Symbol(Symbol.PRIME)]*int(order)
    else:
      primeList = []

    if len(t) > 8:
      t[0] = DifferentialVariable(Identifier(ID(t[1])), primeList, t[9])

    else:
      t[0] = DifferentialVariable(Identifier(ID(t[1])), primeList)

  else:
    if len(t) > 8:
      raise SyntaxException(t.slice[5].lineno, t.slice[5].lexpos, t.slice[5].value, t.slice[5])

    else:
      t[0] = ExpressionWithBinaryOperation(BinaryOperator(BinaryOperator.POW), Identifier(ID(t[1])), t[5])


def p_LIMIT(t):
    '''Limit : LIMIT UNDERLINE LBRACE ID TO Expression RBRACE Expression
             | LIMIT UNDERLINE LBRACE ID TO Expression PLUS RBRACE Expression
             | LIMIT UNDERLINE LBRACE ID TO Expression MINUS RBRACE Expression
             | LIMIT UNDERLINE LBRACE ID TO Expression CARET LBRACE PLUS RBRACE RBRACE Expression
             | LIMIT UNDERLINE LBRACE ID TO Expression CARET LBRACE MINUS RBRACE RBRACE Expression
             | LIMIT UNDERLINE LBRACE ID TO Term CARET LBRACE PLUS RBRACE RBRACE Expression
             | LIMIT UNDERLINE LBRACE ID TO Term CARET LBRACE MINUS RBRACE RBRACE Expression'''

    if len(t) > 10:

      if t.slice[9].type == "PLUS":
        approachesFrom = Limit.FROM_RIGHT

      else:
        approachesFrom = Limit.FROM_LEFT

      t[0] = Limit(Identifier(ID(t[4])), t[6], t[12], approachesFrom)

    elif len(t) > 9:

      if t.slice[7].type == "PLUS":
        approachesFrom = Limit.FROM_RIGHT

      else:
        approachesFrom = Limit.FROM_LEFT

      t[0] = Limit(Identifier(ID(t[4])), t[6], t[9], approachesFrom)

    else:
      t[0] = Limit(Identifier(ID(t[4])), t[6], t[8])

def p_ExpessionList(t):
  '''ExpressionList : ExpressionList COMMA Expression
                    | Expression'''

  if len(t) == 2:
    t[0] = ExpressionList([t[1]])

  else:
    t[1].add(t[3])
    t[0] = t[1]

def p_PrimeList(t):
  '''PrimeList : PrimeList PRIME
               | PRIME'''

  if len(t) == 2:
    t[0] = [Symbol(Symbol.PRIME)]

  else:
    t[0] = t[1] + [Symbol(Symbol.PRIME)]

def p_Constraint(t):
  '''Constraint : Expression EQ Expression
                | Expression NEQ Expression
                | Expression LT Expression
                | Expression LE Expression
                | Expression GT Expression
                | Expression GE Expression'''

  _type = t.slice[2].type

  if _type == "EQ":
    op = ConstraintOperator(ConstraintOperator.EQ)

  elif _type == "NEQ":
    op = ConstraintOperator(ConstraintOperator.NEQ)

  elif _type == "LT":
    op = ConstraintOperator(ConstraintOperator.LT)

  elif _type == "LE":
    op = ConstraintOperator(ConstraintOperator.LE)

  elif _type == "GT":
    op = ConstraintOperator(ConstraintOperator.GT)

  elif _type == "GE":
    op = ConstraintOperator(ConstraintOperator.GE)
  
  t[0] = Constraint(op, t[1], t[3])

def p_Symbol(t):
  '''Factor : PI'''
  t[0] = Symbol(Symbol.PI)

def p_error(t):
  if t:
    raise SyntaxException(t.lineno, t.lexpos, t.value, t)
  else:
    raise SyntaxException("EOF")
