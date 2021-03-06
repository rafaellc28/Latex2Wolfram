#!/usr/bin/python -tt

from lexer import tokens

from Main import *
from IndexingExpression import *
from Expression import *
from Integral import *
from Derivative import *
from DifferentialVariable import *
from ChooseExpression import *
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
    ('left', 'BEGIN_CASE', 'END_CASE', 'BEGIN_BMATRIX', 'END_BMATRIX', 'BEGIN_PMATRIX', 'END_PMATRIX', 'BACKSLASHES'),
    ('left', 'INTEGRAL', 'DIFFERENTIAL', 'D', 'I', 'E', 'PARTIAL', 'LIMIT', 'TO'),
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
    ('left', 'TIMES', 'DIVIDE', 'MOD', 'CHOOSE', 'DOT'),
    ('left', 'UPLUS', 'UMINUS'),
    ('right', 'CARET'),
    ('left', 'LFLOOR', 'RFLOOR', 'LCEIL', 'RCEIL', 'SINH', 'ASINH', 'SIN', 'ASIN', 'COSH', 'ACOSH', 'COS', 'ACOS', 'TANH', 'ATANH', 'TAN', 'ATAN',
      'SEC', 'ASEC', 'CSC', 'ACSC', 'COTH', 'ACOTH', 'COT', 'ACOT', 'SQRT', 'LN', 'LOG', 'EXP', 'GCD', 'DEG', 'GRADIENT', 'DETERMINANT', 
      'CROSS')
)

def p_Main(t):
  '''MAIN : Expression
          | Constraint
          | ConstraintSystem'''
  t[0] = Main(t[1])

def p_Factor(t):
  '''Factor : NUMBER
            | ImaginaryNumber
            | NapierNumber
            | ID
            | INFINITY
            | Symbol
            | IteratedExpression
            | DivisorFunction
            | Derivative
            | Integral
            | Limit
            | DifferentialVariable
            | ChooseExpression
            | Matrix
            | Determinant
            | Norm
            | FractionalExpression
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
          | Term DOT Factor
          | Term CROSS Factor
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

    elif _type == "DOT":
        op = BinaryOperator(BinaryOperator.DOT)

    elif _type == "CROSS":
        op = BinaryOperator(BinaryOperator.CROSS)

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
    '''Factor : PLUS Expression %prec UPLUS
              | MINUS Expression %prec UMINUS'''

    if t.slice[1].type == "PLUS":
      op = UnaryOperator.PLUS
    else:
      op = UnaryOperator.MINUS

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
    '''FractionalExpression : FRAC LBRACE Expression RBRACE LBRACE Expression RBRACE'''

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

              | GCD LPAREN ExpressionList RPAREN

              | GCD ID

              | GCD NUMBER

              | DEG LPAREN ExpressionList RPAREN

              | DEG ID

              | DEG NUMBER

              | GRADIENT LPAREN ExpressionList RPAREN

              | GRADIENT ID

              | GRADIENT NUMBER

              | GRADIENT DOT LPAREN ExpressionList RPAREN

              | GRADIENT DOT ID

              | GRADIENT DOT NUMBER

              | GRADIENT CROSS LPAREN ExpressionList RPAREN
              
              | GRADIENT CROSS ID
              
              | GRADIENT CROSS NUMBER
              
              | LAPLACIAN LPAREN Expression RPAREN
              
              | LAPLACIAN NUMBER
              
              | LAPLACIAN ID
              
              | DETERMINANT LPAREN Matrix RPAREN
              
              | DETERMINANT Matrix

              | Symbol LPAREN ExpressionList RPAREN
              
              | ID LPAREN ExpressionList RPAREN
              
              | ID LPAREN RPAREN'''

    _type = t.slice[1].type

    if _type == "Symbol":
        function = t[1]

    elif _type == "SQRT":
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

    elif _type == "GCD":
        function = FunctionName(FunctionName.GCD)

    elif _type == "DEG":
        function = FunctionName(FunctionName.DEG)

    elif _type == "GRADIENT":
        if t.slice[2].type == "DOT":
          function = FunctionName(FunctionName.DIV)
        elif t.slice[2].type == "CROSS":
          function = FunctionName(FunctionName.CURL)
        else:
          function = FunctionName(FunctionName.GRAD)

    elif _type == "LAPLACIAN":
        function = FunctionName(FunctionName.LAPL)

    elif _type == "DETERMINANT":
        function = FunctionName(FunctionName.DET)

    else:
      function = FunctionName(Identifier(ID(t[1])))

    if len(t) > 5:

      if _type == "GRADIENT":
        t[0] = ExpressionWithFunction(function, t[4])

      elif _type == "LOG":
        t[0] = ExpressionWithFunction(function, t[7], t[4])

      elif _type == "SQRT":
        t[0] = ExpressionWithFunction(function, t[6], t[3])
        
      else:
        t[0] = ExpressionWithFunction(function, t[3], t[5])

    elif len(t) > 4:
      t[0] = ExpressionWithFunction(function, t[3])
        
    else:
      if _type == "GRADIENT":
        if t.slice[3].type == "ID":
          t[3] = Identifier(ID(t[3]))

        t[0] = ExpressionWithFunction(function, t[3])

      elif t.slice[2].type == "LPAREN":
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
      t[0] = Derivative(t[11], t[17], t[6])

    else:
      t[0] = Derivative(t[7], t[9])

def p_Derivative4(t):
    '''Derivative : FRAC LBRACE PARTIAL Expression RBRACE LBRACE PARTIAL ID RBRACE
                  | FRAC LBRACE PARTIAL CARET LBRACE NUMBER RBRACE Expression RBRACE LBRACE PARTIAL ID CARET LBRACE NUMBER RBRACE RBRACE'''

    if len(t) > 10:
      t[0] = Derivative(t[12][:1], t[8], t[6])

    else:
      t[0] = Derivative(t[8][:1], t[4])

def p_DivisorFunction(t):
  '''DivisorFunction : SIGMA_LOWER UNDERLINE LBRACE NUMBER RBRACE LPAREN ExpressionList RPAREN'''
  t[0] = ExpressionWithFunction(Symbol(Symbol.SIGMA_LOWER), t[7], t[4])


def p_ImaginaryNumber(t):
    '''ImaginaryNumber : I
                       | NUMBER I'''
    if len(t) > 2:
      t[0] = ImaginaryNumber(t[1])
    else:
      t[0] = ImaginaryNumber()

def p_NapierNumber(t):
    '''NapierNumber : E
                    | NUMBER E'''
    if len(t) > 2:
      t[0] = NapierNumber(t[1])
    else:
      t[0] = NapierNumber()

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

def p_Choose(t):
  '''ChooseExpression : LBRACE Expression CHOOSE Expression RBRACE'''
  t[0] = ChooseExpression(t[2], t[4])

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

def p_ConstraintSystem(t):
  '''ConstraintSystem : BEGIN_CASE Constraints END_CASE
                      | BEGIN_CASE Constraints BACKSLASHES END_CASE'''
  t[0] = t[2]

def p_Constraints(t):
  '''Constraints : Constraints BACKSLASHES Constraint
                 | Constraint'''

  if len(t) == 2:
    t[0] = Constraints([t[1]])

  else:
    t[1].add(t[3])
    t[0] = t[1]

def p_Determinant(t):
  '''Determinant : BEGIN_VMATRIX ExpressionsRows END_VMATRIX
                 | BEGIN_VMATRIX ExpressionsRows BACKSLASHES END_VMATRIX'''

  t[0] = ExpressionWithFunction(FunctionName.DET, t[2])

def p_Norm(t):
  '''Norm : BEGIN_NMATRIX ExpressionsRows END_NMATRIX
          | BEGIN_NMATRIX ExpressionsRows BACKSLASHES END_NMATRIX'''

  t[0] = ExpressionWithFunction(FunctionName.NORM, t[2])

def p_Matrix(t):
  '''Matrix : BEGIN_BMATRIX ExpressionsRows END_BMATRIX
            | BEGIN_BMATRIX ExpressionsRows BACKSLASHES END_BMATRIX

            | BEGIN_PMATRIX ExpressionsRows END_PMATRIX
            | BEGIN_PMATRIX ExpressionsRows BACKSLASHES END_PMATRIX'''

  t[0] = t[2]

def p_ExpressionsRow(t):
  '''ExpressionsRow : ExpressionsRow AMPERSAND Expression
                    | Expression'''

  if len(t) == 2:
    t[0] = ExpressionsRow([t[1]])

  else:
    t[1].add(t[3])
    t[0] = t[1]

def p_ExpressionsRows(t):
  '''ExpressionsRows : ExpressionsRows BACKSLASHES ExpressionsRow
                     | ExpressionsRow'''

  if len(t) == 2:
    t[0] = ExpressionsRow([t[1]])

  else:
    t[1].add(t[3])
    t[0] = t[1]

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
  '''Symbol : PI
            | XI_LOWER
            | CHI_LOWER
            | PHI_LOWER
            | PSI_LOWER
            | SIGMA_LOWER
            | ZETA_LOWER
            | ETA_LOWER
            | DELTA_LOWER
            | THETA_LOWER
            | LAMBDA_LOWER
            | EPSILON_LOWER
            | TAU_LOWER
            | KAPPA_LOWER
            | OMEGA_LOWER
            | ALPHA_LOWER
            | NU_LOWER
            | RHO_LOWER
            | OMICRON_LOWER
            | UPSILON_LOWER
            | IOTA_LOWER
            | BETA_LOWER
            | GAMMA_LOWER
            | MU_LOWER
            | PI_UPPER
            | BETA
            | GAMMA
            | KAPPA
            | OMICRON
            | OMEGA
            | LAMBDA
            | IOTA
            | PSI
            | MU
            | PHI
            | SIGMA
            | ETA
            | ZETA
            | THETA
            | EPSILON
            | TAU
            | ALPHA
            | XI
            | CHI
            | NU
            | RHO
            | UPSILON'''

  if t.slice[1].type == "PI":
    t[0] = Symbol(Symbol.PI)

  elif t.slice[1].type == "PI_UPPER":
    t[0] = Symbol(Symbol.PI_UPPER)

  elif t.slice[1].type == "ALPHA_LOWER":
    t[0] = Symbol(Symbol.ALPHA_LOWER)

  elif t.slice[1].type == "CHI_LOWER":
    t[0] = Symbol(Symbol.CHI_LOWER)

  elif t.slice[1].type == "XI_LOWER":
    t[0] = Symbol(Symbol.XI_LOWER)

  elif t.slice[1].type == "PHI_LOWER":
    t[0] = Symbol(Symbol.PHI_LOWER)

  elif t.slice[1].type == "PSI_LOWER":
    t[0] = Symbol(Symbol.PSI_LOWER)

  elif t.slice[1].type == "SIGMA_LOWER":
    t[0] = Symbol(Symbol.SIGMA_LOWER)

  elif t.slice[1].type == "ZETA_LOWER":
    t[0] = Symbol(Symbol.ZETA_LOWER)

  elif t.slice[1].type == "ETA_LOWER":
    t[0] = Symbol(Symbol.ETA_LOWER)

  elif t.slice[1].type == "DELTA_LOWER":
    t[0] = Symbol(Symbol.DELTA_LOWER)

  elif t.slice[1].type == "THETA_LOWER":
    t[0] = Symbol(Symbol.THETA_LOWER)

  elif t.slice[1].type == "LAMBDA_LOWER":
    t[0] = Symbol(Symbol.LAMBDA_LOWER)

  elif t.slice[1].type == "EPSILON_LOWER":
    t[0] = Symbol(Symbol.EPSILON_LOWER)

  elif t.slice[1].type == "TAU_LOWER":
    t[0] = Symbol(Symbol.TAU_LOWER)

  elif t.slice[1].type == "KAPPA_LOWER":
    t[0] = Symbol(Symbol.KAPPA_LOWER)

  elif t.slice[1].type == "OMEGA_LOWER":
    t[0] = Symbol(Symbol.OMEGA_LOWER)

  elif t.slice[1].type == "NU_LOWER":
    t[0] = Symbol(Symbol.NU_LOWER)

  elif t.slice[1].type == "RHO_LOWER":
    t[0] = Symbol(Symbol.RHO_LOWER)

  elif t.slice[1].type == "OMICRON_LOWER":
    t[0] = Symbol(Symbol.OMICRON_LOWER)

  elif t.slice[1].type == "UPSILON_LOWER":
    t[0] = Symbol(Symbol.UPSILON_LOWER)

  elif t.slice[1].type == "IOTA_LOWER":
    t[0] = Symbol(Symbol.IOTA_LOWER)

  elif t.slice[1].type == "BETA_LOWER":
    t[0] = Symbol(Symbol.BETA_LOWER)

  elif t.slice[1].type == "GAMMA_LOWER":
    t[0] = Symbol(Symbol.GAMMA_LOWER)

  elif t.slice[1].type == "BETA":
    t[0] = Symbol(Symbol.BETA)

  elif t.slice[1].type == "GAMMA":
    t[0] = Symbol(Symbol.GAMMA)

  elif t.slice[1].type == "MU":
    t[0] = Symbol(Symbol.MU)

  elif t.slice[1].type == "KAPPA":
    t[0] = Symbol(Symbol.KAPPA)

  elif t.slice[1].type == "OMICRON":
    t[0] = Symbol(Symbol.OMICRON)

  elif t.slice[1].type == "OMEGA":
    t[0] = Symbol(Symbol.OMEGA)

  elif t.slice[1].type == "LAMBDA":
    t[0] = Symbol(Symbol.LAMBDA)

  elif t.slice[1].type == "IOTA":
    t[0] = Symbol(Symbol.IOTA)

  elif t.slice[1].type == "PSI":
    t[0] = Symbol(Symbol.PSI)

  elif t.slice[1].type == "PHI":
    t[0] = Symbol(Symbol.PHI)
  
  elif t.slice[1].type == "SIGMA":
    t[0] = Symbol(Symbol.SIGMA)
  
  elif t.slice[1].type == "ETA":
    t[0] = Symbol(Symbol.ETA)
  
  elif t.slice[1].type == "ZETA":
    t[0] = Symbol(Symbol.ZETA)
  
  elif t.slice[1].type == "THETA":
    t[0] = Symbol(Symbol.THETA)
  
  elif t.slice[1].type == "EPSILON":
    t[0] = Symbol(Symbol.EPSILON)
  
  elif t.slice[1].type == "TAU":
    t[0] = Symbol(Symbol.TAU)
  
  elif t.slice[1].type == "ALPHA":
    t[0] = Symbol(Symbol.ALPHA)
  
  elif t.slice[1].type == "XI":
    t[0] = Symbol(Symbol.XI)
  
  elif t.slice[1].type == "CHI":
    t[0] = Symbol(Symbol.CHI)
  
  elif t.slice[1].type == "NU":
    t[0] = Symbol(Symbol.NU)
  
  elif t.slice[1].type == "RHO":
    t[0] = Symbol(Symbol.RHO)
  
  elif t.slice[1].type == "UPSILON":
    t[0] = Symbol(Symbol.UPSILON)
  
  else:
    t[0] = Symbol(Symbol.MU_LOWER)

def p_error(t):
  if t:
    raise SyntaxException(t.lineno, t.lexpos, t.value, t)
  else:
    raise SyntaxException("EOF")
