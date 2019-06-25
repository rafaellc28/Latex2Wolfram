#!/usr/bin/python -tt

import sys
import re

from lexer import tokens
import ply.yacc as yacc

from Main import *
from LinearProgram import *
from LinearEquations import *
from Objectives import *
from Constraints import *
from ConstraintExpression import *
from LinearExpression import *
from NumericExpression import *
from SymbolicExpression import *
from IndexingExpression import *
from EntryIndexingExpression import *
from LogicalExpression import *
from EntryLogicalExpression import *
from SetExpression import *
from ValueList import *
from TupleList import *
from Tuple import *
from Range import *
from Value import *
from Identifier import *
from ID import *
from SyntaxException import *
from Declarations import *
from DeclarationExpression import *

precedence = (
    ('left', 'ID'),
    ('left', 'COMMA', 'DOTS', 'FOR', 'WHERE'),
    ('left', 'NUMBER'),
    ('left', 'OR', 'AND', 'NOT'),
    ('left', 'FORALL', 'EXISTS', 'NEXISTS'),
    ('right', 'LE', 'GE', 'LT', 'GT', 'EQ', 'NEQ', 'COLON', 'DEFAULT', 'DIMEN', 'SETOF'),
    ('left', 'DIFF', 'SYMDIFF', 'UNION', 'INTER', 'CROSS', 'BY'),
    ('left', 'UNDERLINE', 'CARET'),
    ('left', 'SUM', 'PROD', 'MAX', 'MIN'),
    ('left', 'PIPE', 'LFLOOR', 'RFLOOR', 'LCEIL', 'RCEIL', 'SIN', 'COS', 'ARCTAN', 'SQRT', 'LN', 'LOG', 'EXP'),
    ('right', 'LPAREN', 'RPAREN'),
    ('right', 'IN', 'NOTIN', 'SUBSET', 'NOTSUBSET'),
    ('right', 'LBRACE', 'RBRACE', 'LLBRACE', 'RRBRACE', 'LBRACKET', 'RBRACKET'),
    ('right', 'PLUS', 'MINUS'),
    ('right', 'TIMES', 'DIVIDE', 'MOD', 'QUOTIENT', 'LESS'),
    ('right', 'UPLUS', 'UMINUS'),
    ('right', 'AMPERSAND'),
    ('left', 'INTEGERSET', 'INTEGERSETPOSITIVE', 'INTEGERSETNEGATIVE', 'INTEGERSETWITHONELIMIT', 
      'REALSET', 'REALSETPOSITIVE', 'REALSETNEGATIVE', 'REALSETWITHONELIMIT', 'NATURALSET', 'BINARYSET', 'SYMBOLIC', 'LOGICAL')
)

def p_Main(t):
  '''MAIN : LinearProgram 
          | LinearEquations'''
  t[0] = Main(t[1])

def p_LinearEquations(t):
    '''LinearEquations : ConstraintList'''
    t[0] = LinearEquations(Constraints(t[1]))

def p_LinearProgram(t):
    '''LinearProgram : Objectives
                     | Objectives Constraints'''

    if isinstance(t[1], LinearProgram):
      t[1].setDeclarations(t[2])
      t[0] = t[1]

    else:
      if len(t) > 3:
          t[0] = LinearProgram(t[1], t[3])
      elif len(t) > 2:
          t[0] = LinearProgram(t[1], t[2])
      else:
          t[0] = LinearProgram(t[1], None)

def p_Objectives(t):
    '''Objectives : Objectives Objective
                  | Objective'''

    if not isinstance(t[1], Objectives):
        t[0] = Objectives([t[1]])
    elif len(t) > 2:
        t[0] = t[1].addObjective(t[2])
    else:
        t[0] = t[1]

def p_Objective(t):
    '''Objective : MAXIMIZE LinearExpression
                 | MAXIMIZE SymbolicExpression
                 | MAXIMIZE NumericExpression
                 | MAXIMIZE Identifier
                 | MINIMIZE LinearExpression
                 | MINIMIZE SymbolicExpression
                 | MINIMIZE NumericExpression
                 | MINIMIZE Identifier
                 | MAXIMIZE LinearExpression FOR IndexingExpression
                 | MAXIMIZE SymbolicExpression FOR IndexingExpression
                 | MAXIMIZE NumericExpression FOR IndexingExpression
                 | MAXIMIZE Identifier FOR IndexingExpression
                 | MINIMIZE LinearExpression FOR IndexingExpression
                 | MINIMIZE SymbolicExpression FOR IndexingExpression
                 | MINIMIZE NumericExpression FOR IndexingExpression
                 | MINIMIZE Identifier FOR IndexingExpression
                 | MAXIMIZE LinearExpression WHERE IndexingExpression
                 | MAXIMIZE SymbolicExpression WHERE IndexingExpression
                 | MAXIMIZE NumericExpression WHERE IndexingExpression
                 | MAXIMIZE Identifier WHERE IndexingExpression
                 | MINIMIZE LinearExpression WHERE IndexingExpression
                 | MINIMIZE SymbolicExpression WHERE IndexingExpression
                 | MINIMIZE NumericExpression WHERE IndexingExpression
                 | MINIMIZE Identifier WHERE IndexingExpression
                 | MAXIMIZE LinearExpression COLON IndexingExpression
                 | MAXIMIZE SymbolicExpression COLON IndexingExpression
                 | MAXIMIZE NumericExpression COLON IndexingExpression
                 | MAXIMIZE Identifier COLON IndexingExpression
                 | MINIMIZE LinearExpression COLON IndexingExpression
                 | MINIMIZE SymbolicExpression COLON IndexingExpression
                 | MINIMIZE NumericExpression COLON IndexingExpression
                 | MINIMIZE Identifier COLON IndexingExpression'''

    if len(t) > 3:
        t[4].setStmtIndexing(True)

        obj = Objective.MINIMIZE
        if re.search(r"\\text\{\s*maximize\s*\}|maximize|\\text\{\s*maximize:\s*\}|maximize:", t[1]):
            obj = Objective.MAXIMIZE

        t[0] = Objective(t[2], obj, t[4])
    else:
        if re.search(r"\\text\{\s*minimize\s*\}|minimize|\\text\{\s*minimize:\s*\}|minimize:", t[1]):
            t[0] = Objective(t[2])
        else:
            t[0] = Objective(t[2], Objective.MAXIMIZE)

def p_Constraints(t):
    '''Constraints : SUBJECTTO ConstraintList'''
    t[0] = Constraints(t[2])

def p_ConstraintList(t):
    '''ConstraintList : ConstraintList Constraint
                      | ConstraintList Declarations
                      | Declarations
                      | Constraint'''
    if len(t) > 2:
      if isinstance(t[2], Declarations):
        t[0] = t[1] + t[2].declarations
      else:
        t[0] = t[1] + [t[2]]

    elif isinstance(t[1], Declarations):
        t[0] = t[1].declarations
    #elif len(t) > 2:
    #    t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_Constraint(t):
    '''Constraint : ConstraintExpression FOR IndexingExpression
                  | ConstraintExpression WHERE IndexingExpression
                  | ConstraintExpression COLON IndexingExpression
                  | ConstraintExpression'''
    
    if len(t) > 3:
        t[3].setStmtIndexing(True)
        t[0] = Constraint(t[1], t[3])
    else:
        t[0] = Constraint(t[1])

def p_ConstraintExpression(t):
    '''ConstraintExpression : LinearExpression EQ LinearExpression
                            | SymbolicExpression EQ SymbolicExpression
                            | NumericExpression EQ LinearExpression
                            | NumericExpression EQ SymbolicExpression
                            | Identifier EQ LinearExpression
                            | Identifier EQ SymbolicExpression
                            | LinearExpression EQ NumericExpression
                            | SymbolicExpression EQ NumericExpression
                            | LinearExpression EQ Identifier
                            | SymbolicExpression EQ Identifier
                            | NumericExpression EQ NumericExpression
                            | NumericExpression EQ Identifier
                            | Identifier EQ NumericExpression
                            | Identifier EQ Identifier
                            | LinearExpression LE LinearExpression
                            | SymbolicExpression LE SymbolicExpression
                            | NumericExpression LE LinearExpression
                            | NumericExpression LE SymbolicExpression
                            | Identifier LE LinearExpression
                            | Identifier LE SymbolicExpression
                            | LinearExpression LE NumericExpression
                            | SymbolicExpression LE NumericExpression
                            | LinearExpression LE Identifier
                            | SymbolicExpression LE Identifier
                            | NumericExpression LE NumericExpression
                            | NumericExpression LE Identifier
                            | Identifier LE NumericExpression
                            | Identifier LE Identifier
                            | LinearExpression GE LinearExpression
                            | SymbolicExpression GE SymbolicExpression
                            | NumericExpression GE LinearExpression
                            | NumericExpression GE SymbolicExpression
                            | Identifier GE LinearExpression
                            | Identifier GE SymbolicExpression
                            | LinearExpression GE NumericExpression
                            | SymbolicExpression GE NumericExpression
                            | LinearExpression GE Identifier
                            | SymbolicExpression GE Identifier
                            | NumericExpression GE NumericExpression
                            | NumericExpression GE Identifier
                            | Identifier GE NumericExpression
                            | Identifier GE Identifier
                            | LinearExpression LE LinearExpression LE LinearExpression
                            | SymbolicExpression LE SymbolicExpression LE SymbolicExpression
                            | LinearExpression LE LinearExpression LE NumericExpression
                            | SymbolicExpression LE SymbolicExpression LE NumericExpression
                            | LinearExpression LE LinearExpression LE Identifier
                            | SymbolicExpression LE SymbolicExpression LE Identifier
                            | LinearExpression LE NumericExpression LE LinearExpression
                            | SymbolicExpression LE NumericExpression LE SymbolicExpression
                            | LinearExpression LE Identifier LE LinearExpression
                            | SymbolicExpression LE Identifier LE SymbolicExpression
                            | LinearExpression LE NumericExpression LE NumericExpression
                            | SymbolicExpression LE NumericExpression LE NumericExpression
                            | LinearExpression LE NumericExpression LE Identifier
                            | SymbolicExpression LE NumericExpression LE Identifier
                            | LinearExpression LE Identifier LE NumericExpression
                            | SymbolicExpression LE Identifier LE NumericExpression
                            | LinearExpression LE Identifier LE Identifier
                            | SymbolicExpression LE Identifier LE Identifier
                            | NumericExpression LE LinearExpression LE LinearExpression
                            | NumericExpression LE SymbolicExpression LE SymbolicExpression
                            | Identifier LE LinearExpression LE LinearExpression
                            | Identifier LE SymbolicExpression LE SymbolicExpression
                            | NumericExpression LE LinearExpression LE NumericExpression
                            | NumericExpression LE SymbolicExpression LE NumericExpression
                            | NumericExpression LE LinearExpression LE Identifier
                            | NumericExpression LE SymbolicExpression LE Identifier
                            | Identifier LE LinearExpression LE NumericExpression
                            | Identifier LE SymbolicExpression LE NumericExpression
                            | Identifier LE LinearExpression LE Identifier
                            | Identifier LE SymbolicExpression LE Identifier
                            | NumericExpression LE NumericExpression LE LinearExpression
                            | NumericExpression LE NumericExpression LE SymbolicExpression
                            | NumericExpression LE Identifier LE LinearExpression
                            | NumericExpression LE Identifier LE SymbolicExpression
                            | Identifier LE NumericExpression LE LinearExpression
                            | Identifier LE NumericExpression LE SymbolicExpression
                            | Identifier LE Identifier LE LinearExpression
                            | Identifier LE Identifier LE SymbolicExpression
                            | NumericExpression LE NumericExpression LE NumericExpression
                            | NumericExpression LE NumericExpression LE Identifier
                            | NumericExpression LE Identifier LE NumericExpression
                            | Identifier LE NumericExpression LE NumericExpression
                            | Identifier LE NumericExpression LE Identifier
                            | Identifier LE Identifier LE NumericExpression
                            | Identifier LE Identifier LE Identifier
                            | LinearExpression GE LinearExpression GE LinearExpression
                            | SymbolicExpression GE SymbolicExpression GE SymbolicExpression
                            | LinearExpression GE LinearExpression GE NumericExpression
                            | SymbolicExpression GE SymbolicExpression GE NumericExpression
                            | LinearExpression GE LinearExpression GE Identifier
                            | SymbolicExpression GE SymbolicExpression GE Identifier
                            | LinearExpression GE NumericExpression GE LinearExpression
                            | SymbolicExpression GE NumericExpression GE SymbolicExpression
                            | LinearExpression GE Identifier GE LinearExpression
                            | SymbolicExpression GE Identifier GE SymbolicExpression
                            | LinearExpression GE NumericExpression GE NumericExpression
                            | SymbolicExpression GE NumericExpression GE NumericExpression
                            | LinearExpression GE NumericExpression GE Identifier
                            | SymbolicExpression GE NumericExpression GE Identifier
                            | LinearExpression GE Identifier GE NumericExpression
                            | SymbolicExpression GE Identifier GE NumericExpression
                            | LinearExpression GE Identifier GE Identifier
                            | SymbolicExpression GE Identifier GE Identifier
                            | NumericExpression GE LinearExpression GE LinearExpression
                            | NumericExpression GE SymbolicExpression GE SymbolicExpression
                            | Identifier GE LinearExpression GE LinearExpression
                            | Identifier GE SymbolicExpression GE SymbolicExpression
                            | NumericExpression GE LinearExpression GE NumericExpression
                            | NumericExpression GE SymbolicExpression GE NumericExpression
                            | NumericExpression GE LinearExpression GE Identifier
                            | NumericExpression GE SymbolicExpression GE Identifier
                            | Identifier GE LinearExpression GE NumericExpression
                            | Identifier GE SymbolicExpression GE NumericExpression
                            | Identifier GE LinearExpression GE Identifier
                            | Identifier GE SymbolicExpression GE Identifier
                            | NumericExpression GE NumericExpression GE LinearExpression
                            | NumericExpression GE NumericExpression GE SymbolicExpression
                            | NumericExpression GE Identifier GE LinearExpression
                            | NumericExpression GE Identifier GE SymbolicExpression
                            | Identifier GE NumericExpression GE LinearExpression
                            | Identifier GE NumericExpression GE SymbolicExpression
                            | Identifier GE Identifier GE LinearExpression
                            | Identifier GE Identifier GE SymbolicExpression
                            | NumericExpression GE NumericExpression GE NumericExpression
                            | NumericExpression GE NumericExpression GE Identifier
                            | NumericExpression GE Identifier GE NumericExpression
                            | NumericExpression GE Identifier GE Identifier
                            | Identifier GE NumericExpression GE NumericExpression
                            | Identifier GE NumericExpression GE Identifier
                            | Identifier GE Identifier GE NumericExpression
                            | Identifier GE Identifier GE Identifier'''
    
    if len(t) > 4:
        if t[4] == "\\leq":
            t[0] = ConstraintExpression3(t[3], t[1], t[5], ConstraintExpression.LE)
        elif t[4] == "\\geq":
            t[0] = ConstraintExpression3(t[3], t[1], t[5], ConstraintExpression.GE)
    elif t[2] == "=":
        t[0] = ConstraintExpression2(t[1], t[3], ConstraintExpression.EQ)
    elif t[2] == "\\leq":
        t[0] = ConstraintExpression2(t[1], t[3], ConstraintExpression.LE)
    elif t[2] == "\\geq":
        t[0] = ConstraintExpression2(t[1], t[3], ConstraintExpression.GE)

def p_Declarations(t):
  '''Declarations : DeclarationList'''

  i = 1
  length = len(t[1])
  lastDecl = t[1][length-i]
  while (not lastDecl or lastDecl.indexingExpression == None) and i < length:
    i += 1
    lastDecl = t[1][length-i]
  
  if lastDecl and lastDecl.indexingExpression != None:
    for i in range(length-i):
      decl = t[1][i]
      if decl.indexingExpression == None:
        decl.setIndexingExpression(lastDecl.indexingExpression)

  t[0] = Declarations(t[1])

def p_DeclarationList(t):
    '''DeclarationList : Declaration
                       | DeclarationList SEMICOLON Declaration'''
    if len(t) > 4:
      t[0] = t[1] + [t[4]]
    elif len(t) > 3:
      if isinstance(t[3], Declaration):
        t[0] = t[1] + [t[3]]
      else:
        t[0] = t[1]
    elif len(t) > 2:
      t[0] = t[1]
    else:
      t[0] = [t[1]]

def p_Declaration(t):
    '''Declaration : DeclarationExpression FOR IndexingExpression
                   | DeclarationExpression WHERE IndexingExpression
                   | DeclarationExpression COLON IndexingExpression
                   | ValueList FOR IndexingExpression
                   | NumericExpression FOR IndexingExpression
                   | Identifier FOR IndexingExpression
                   | SymbolicExpression FOR IndexingExpression
                   | ValueList WHERE IndexingExpression
                   | NumericExpression WHERE IndexingExpression
                   | Identifier WHERE IndexingExpression
                   | SymbolicExpression WHERE IndexingExpression
                   | ValueList COLON IndexingExpression
                   | NumericExpression COLON IndexingExpression
                   | Identifier COLON IndexingExpression
                   | SymbolicExpression COLON IndexingExpression
                   | DeclarationExpression'''

    #if len(t) > 4:
    #    t[4].setStmtIndexing(True)
    #    if isinstance(t[1], ValueList):
    #      t[1] = DeclarationExpression(t[1], [])
    #    elif isinstance(t[1], NumericExpression) or isinstance(t[1], SymbolicExpression) or isinstance(t[1], Identifier):
    #      t[1] = DeclarationExpression(ValueList([t[1]]), [])
    #
    #    t[0] = Declaration(t[1], t[4])

    if len(t) > 3:
        t[3].setStmtIndexing(True)
        if isinstance(t[1], ValueList):
          t[1] = DeclarationExpression(t[1], [])
        elif isinstance(t[1], NumericExpression) or isinstance(t[1], SymbolicExpression) or isinstance(t[1], Identifier):
          t[1] = DeclarationExpression(ValueList([t[1]]), [])

        t[0] = Declaration(t[1], t[3])
    else:
        t[0] = Declaration(t[1])

def p_DeclarationExpression(t):
    '''DeclarationExpression : ValueList IN SetExpression
                             | ValueList IN Range
                             | NumericExpression IN SetExpression
                             | NumericExpression IN Range
                             | Identifier IN SetExpression
                             | Identifier IN Range
                             | SymbolicExpression IN SetExpression
                             | SymbolicExpression IN Range
                             | ValueList IN Identifier
                             | NumericExpression IN Identifier
                             | Identifier IN Identifier
                             | SymbolicExpression IN Identifier
                             | ValueList SUBSET SetExpression
                             | ValueList SUBSET Range
                             | NumericExpression SUBSET SetExpression
                             | NumericExpression SUBSET Range
                             | Identifier SUBSET SetExpression
                             | Identifier SUBSET Range
                             | SymbolicExpression SUBSET SetExpression
                             | SymbolicExpression SUBSET Range
                             | ValueList SUBSET Identifier
                             | NumericExpression SUBSET Identifier
                             | Identifier SUBSET Identifier
                             | SymbolicExpression SUBSET Identifier
                             | ValueList DEFAULT NumericExpression
                             | ValueList DEFAULT Identifier
                             | NumericExpression DEFAULT NumericExpression
                             | NumericExpression DEFAULT Identifier
                             | Identifier DEFAULT NumericExpression
                             | Identifier DEFAULT Identifier
                             | SymbolicExpression DEFAULT NumericExpression
                             | SymbolicExpression DEFAULT Identifier
                             | ValueList DEFAULT SymbolicExpression
                             | NumericExpression DEFAULT SymbolicExpression
                             | Identifier DEFAULT SymbolicExpression
                             | SymbolicExpression DEFAULT SymbolicExpression
                             | ValueList DEFAULT SetExpression
                             | ValueList DEFAULT Range
                             | NumericExpression DEFAULT SetExpression
                             | NumericExpression DEFAULT Range
                             | Identifier DEFAULT SetExpression
                             | Identifier DEFAULT Range
                             | SymbolicExpression DEFAULT SetExpression
                             | SymbolicExpression DEFAULT Range
                             | ValueList DIMEN NumericExpression
                             | ValueList DIMEN Identifier
                             | NumericExpression DIMEN NumericExpression
                             | NumericExpression DIMEN Identifier
                             | Identifier DIMEN NumericExpression
                             | Identifier DIMEN Identifier
                             | SymbolicExpression DIMEN NumericExpression
                             | SymbolicExpression DIMEN Identifier
                             | ValueList DIMEN SymbolicExpression
                             | NumericExpression DIMEN SymbolicExpression
                             | Identifier DIMEN SymbolicExpression
                             | SymbolicExpression DIMEN SymbolicExpression
                             | ValueList COLON EQ NumericExpression
                             | ValueList COLON EQ Identifier
                             | NumericExpression COLON EQ NumericExpression
                             | NumericExpression COLON EQ Identifier
                             | Identifier COLON EQ NumericExpression
                             | Identifier COLON EQ Identifier
                             | SymbolicExpression COLON EQ NumericExpression
                             | SymbolicExpression COLON EQ Identifier
                             | ValueList COLON EQ SymbolicExpression
                             | NumericExpression COLON EQ SymbolicExpression
                             | Identifier COLON EQ SymbolicExpression
                             | SymbolicExpression COLON EQ SymbolicExpression
                             | ValueList COLON EQ SetExpression
                             | ValueList COLON EQ Range
                             | NumericExpression COLON EQ SetExpression
                             | NumericExpression COLON EQ Range
                             | Identifier COLON EQ SetExpression
                             | Identifier COLON EQ Range
                             | SymbolicExpression COLON EQ SetExpression
                             | SymbolicExpression COLON EQ Range
                             | ValueList LT NumericExpression
                             | ValueList LT Identifier
                             | NumericExpression LT NumericExpression
                             | NumericExpression LT Identifier
                             | Identifier LT NumericExpression
                             | Identifier LT Identifier
                             | SymbolicExpression LT NumericExpression
                             | SymbolicExpression LT Identifier
                             | ValueList LT SymbolicExpression
                             | NumericExpression LT SymbolicExpression
                             | Identifier LT SymbolicExpression
                             | SymbolicExpression LT SymbolicExpression
                             | ValueList GT NumericExpression
                             | ValueList GT Identifier
                             | NumericExpression GT NumericExpression
                             | NumericExpression GT Identifier
                             | Identifier GT NumericExpression
                             | Identifier GT Identifier
                             | SymbolicExpression GT NumericExpression
                             | SymbolicExpression GT Identifier
                             | ValueList GT SymbolicExpression
                             | NumericExpression GT SymbolicExpression
                             | Identifier GT SymbolicExpression
                             | SymbolicExpression GT SymbolicExpression
                             | ValueList NEQ NumericExpression
                             | ValueList NEQ Identifier
                             | NumericExpression NEQ NumericExpression
                             | NumericExpression NEQ Identifier
                             | Identifier NEQ NumericExpression
                             | Identifier NEQ Identifier
                             | SymbolicExpression NEQ NumericExpression
                             | SymbolicExpression NEQ Identifier
                             | ValueList NEQ SymbolicExpression
                             | NumericExpression NEQ SymbolicExpression
                             | Identifier NEQ SymbolicExpression
                             | SymbolicExpression NEQ SymbolicExpression
                             | ValueList COMMA DeclarationAttributeList
                             | NumericExpression COMMA DeclarationAttributeList
                             | Identifier COMMA DeclarationAttributeList
                             | SymbolicExpression COMMA DeclarationAttributeList
                             | DeclarationExpression COMMA DeclarationAttributeList'''

    if len(t) > 3 and isinstance(t[3], Identifier):
      t[3] = SetExpressionWithValue(t[3])    

    if isinstance(t[1], DeclarationExpression):
      if t[2] == ",":
        t[1].addAttribute(t[3])
      else:
        t[1].addAttribute(t[2])

      t[0] = t[1]

    else:
      attr = None
      if t[2] == ",":
        attr = t[3]
      elif t[2] == "\\in":
        attr = DeclarationAttribute(t[3], DeclarationAttribute.IN)
      elif re.search(r"\\subseteq|\\subset", t[2]):
        attr = DeclarationAttribute(t[3], DeclarationAttribute.WT)
      elif re.search(r"\\text\{\s*default\s*\}", t[2]):
        attr = DeclarationAttribute(t[3], DeclarationAttribute.DF)
      elif re.search(r"\\text\{\s*dimen\s*\}", t[2]):
        attr = DeclarationAttribute(t[3], DeclarationAttribute.DM)
      elif t[2] == ":":
        attr = DeclarationAttribute(t[4], DeclarationAttribute.ST)
      elif t[2] == "<":
        attr = DeclarationAttribute(t[3], DeclarationAttribute.LT)
      elif t[2] == "\\leq":
        attr = DeclarationAttribute(t[3], DeclarationAttribute.LE)
      elif t[2] == ">":
        attr = DeclarationAttribute(t[3], DeclarationAttribute.GT)
      elif t[2] == "\\geq":
        attr = DeclarationAttribute(t[3], DeclarationAttribute.GE)
      elif t[2] == "\\neq":
        attr = DeclarationAttribute(t[3], DeclarationAttribute.NEQ)

      if isinstance(t[1], NumericExpression) or isinstance(t[1], SymbolicExpression) or isinstance(t[1], Identifier):
        t[1] = ValueList([t[1]])

      t[0] = DeclarationExpression(t[1])
      t[0].addAttribute(attr)

def p_DeclarationAttributeList(t):
  '''DeclarationAttributeList : DeclarationAttribute
                              | DeclarationAttributeList COMMA DeclarationAttribute'''
  if len(t) > 3:
    t[0] = t[1] + [t[3]]
  else:
    t[0] = [t[1]]

def p_DeclarationAttribute(t):
  '''DeclarationAttribute : IN SetExpression
                          | IN Range
                          | IN Identifier
                          | SUBSET SetExpression
                          | SUBSET Range
                          | SUBSET Identifier
                          | DEFAULT NumericExpression
                          | DEFAULT Identifier
                          | DEFAULT SymbolicExpression
                          | DEFAULT SetExpression
                          | DEFAULT Range
                          | DIMEN NumericExpression
                          | DIMEN Identifier
                          | DIMEN SymbolicExpression
                          | COLON EQ NumericExpression
                          | COLON EQ Identifier
                          | COLON EQ SymbolicExpression
                          | COLON EQ SetExpression
                          | COLON EQ Range
                          | LT NumericExpression
                          | LT Identifier
                          | LT SymbolicExpression
                          | LE NumericExpression
                          | LE Identifier
                          | LE SymbolicExpression
                          | EQ NumericExpression
                          | EQ Identifier
                          | EQ SymbolicExpression
                          | GT NumericExpression
                          | GT Identifier
                          | GT SymbolicExpression
                          | GE NumericExpression
                          | GE Identifier
                          | GE SymbolicExpression
                          | NEQ NumericExpression
                          | NEQ Identifier
                          | NEQ SymbolicExpression'''
  if isinstance(t[2], Identifier):
    t[2] = SetExpressionWithValue(t[2])    

  if t[1] == "\\in":
    t[0] = DeclarationAttribute(t[2], DeclarationAttribute.IN)
  elif re.search(r"\\subseteq|\\subset", t[1]):
    t[0] = DeclarationAttribute(t[2], DeclarationAttribute.WT)
  elif re.search(r"\\text\{\s*default\s*\}", t[1]):
    t[0] = DeclarationAttribute(t[2], DeclarationAttribute.DF)
  elif re.search(r"\\text\{\s*dimen\s*\}", t[1]):
    t[0] = DeclarationAttribute(t[2], DeclarationAttribute.DM)
  elif t[1] == ":":
    t[0] = DeclarationAttribute(t[3], DeclarationAttribute.ST)
  elif t[1] == "<":
    t[0] = DeclarationAttribute(t[2], DeclarationAttribute.LT)
  elif t[1] == "\\leq":
    t[0] = DeclarationAttribute(t[2], DeclarationAttribute.LE)
  elif t[1] == ">":
    t[0] = DeclarationAttribute(t[2], DeclarationAttribute.GT)
  elif t[1] == "\\geq":
    t[0] = DeclarationAttribute(t[2], DeclarationAttribute.GE)
  elif t[1] == "\\neq":
    t[0] = DeclarationAttribute(t[2], DeclarationAttribute.NEQ)

def p_LinearExpression(t):
    '''LinearExpression : LPAREN LinearExpression RPAREN
                        | ConditionalLinearExpression'''

    if len(t) > 3:
        t[0] = LinearExpressionBetweenParenthesis(t[2])
    elif isinstance(t[1], ConditionalLinearExpression):
        t[0] = t[1]
    else:
        t[0] = ValuedLinearExpression(t[1])

def p_LinearExpression_binop(t):
    '''LinearExpression : LinearExpression PLUS LinearExpression
                        | SymbolicExpression PLUS SymbolicExpression
                        | LinearExpression PLUS NumericExpression
                        | SymbolicExpression PLUS NumericExpression
                        | LinearExpression PLUS Identifier
                        | SymbolicExpression PLUS Identifier
                        | NumericExpression PLUS LinearExpression
                        | NumericExpression PLUS SymbolicExpression
                        | Identifier PLUS LinearExpression
                        | Identifier PLUS SymbolicExpression
                        | LinearExpression MINUS LinearExpression
                        | SymbolicExpression MINUS SymbolicExpression
                        | LinearExpression MINUS NumericExpression
                        | SymbolicExpression MINUS NumericExpression
                        | LinearExpression MINUS Identifier
                        | SymbolicExpression MINUS Identifier
                        | NumericExpression MINUS LinearExpression
                        | NumericExpression MINUS SymbolicExpression
                        | Identifier MINUS LinearExpression
                        | Identifier MINUS SymbolicExpression
                        | LinearExpression TIMES NumericExpression
                        | SymbolicExpression TIMES NumericExpression
                        | LinearExpression TIMES Identifier
                        | SymbolicExpression TIMES Identifier
                        | LinearExpression DIVIDE NumericExpression
                        | SymbolicExpression DIVIDE NumericExpression
                        | LinearExpression DIVIDE Identifier
                        | SymbolicExpression DIVIDE Identifier'''

    if t[2] == "+":
        op = LinearExpressionWithArithmeticOperation.PLUS
    elif t[2] == "-":
        op = LinearExpressionWithArithmeticOperation.MINUS
    elif re.search(r"\*|\\cdot|\\ast", t[2]):
        op = LinearExpressionWithArithmeticOperation.TIMES
    elif re.search(r"/|\\div", t[2]):
        op = LinearExpressionWithArithmeticOperation.DIV

    t[0] = LinearExpressionWithArithmeticOperation(op, t[1], t[3])

def p_IteratedLinearExpression(t):
    '''LinearExpression : SUM UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE NumericExpression RBRACE LinearExpression
                        | SUM UNDERLINE LBRACE IndexingExpression RBRACE LinearExpression
                        | SUM UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE NumericExpression RBRACE SymbolicExpression
                        | SUM UNDERLINE LBRACE IndexingExpression RBRACE SymbolicExpression'''
    if len(t) > 7:
        t[0] = IteratedLinearExpression(t[10], t[4], t[8])
    else:
        t[0] = IteratedLinearExpression(t[6], t[4])

def p_ConditionalLinearExpression(t):
    '''ConditionalLinearExpression : LPAREN Identifier RPAREN QUESTION_MARK LinearExpression COLON LinearExpression
                                   | LPAREN Identifier RPAREN QUESTION_MARK SymbolicExpression COLON SymbolicExpression
                                   | LPAREN Identifier RPAREN QUESTION_MARK LinearExpression COLON NumericExpression
                                   | LPAREN Identifier RPAREN QUESTION_MARK SymbolicExpression COLON NumericExpression
                                   | LPAREN Identifier RPAREN QUESTION_MARK LinearExpression COLON Identifier
                                   | LPAREN Identifier RPAREN QUESTION_MARK SymbolicExpression COLON Identifier
                                   | LPAREN Identifier RPAREN QUESTION_MARK NumericExpression COLON LinearExpression
                                   | LPAREN Identifier RPAREN QUESTION_MARK NumericExpression COLON SymbolicExpression
                                   | LPAREN Identifier RPAREN QUESTION_MARK Identifier COLON LinearExpression
                                   | LPAREN Identifier RPAREN QUESTION_MARK Identifier COLON SymbolicExpression
                                   | LPAREN NumericExpression RPAREN QUESTION_MARK LinearExpression COLON LinearExpression
                                   | LPAREN NumericExpression RPAREN QUESTION_MARK SymbolicExpression COLON SymbolicExpression
                                   | LPAREN NumericExpression RPAREN QUESTION_MARK LinearExpression COLON NumericExpression
                                   | LPAREN NumericExpression RPAREN QUESTION_MARK SymbolicExpression COLON NumericExpression
                                   | LPAREN NumericExpression RPAREN QUESTION_MARK LinearExpression COLON Identifier
                                   | LPAREN NumericExpression RPAREN QUESTION_MARK SymbolicExpression COLON Identifier
                                   | LPAREN NumericExpression RPAREN QUESTION_MARK NumericExpression COLON LinearExpression
                                   | LPAREN NumericExpression RPAREN QUESTION_MARK NumericExpression COLON SymbolicExpression
                                   | LPAREN NumericExpression RPAREN QUESTION_MARK Identifier COLON LinearExpression
                                   | LPAREN NumericExpression RPAREN QUESTION_MARK Identifier COLON SymbolicExpression
                                   | LPAREN LogicalExpression RPAREN QUESTION_MARK LinearExpression COLON LinearExpression
                                   | LPAREN LogicalExpression RPAREN QUESTION_MARK SymbolicExpression COLON SymbolicExpression
                                   | LPAREN LogicalExpression RPAREN QUESTION_MARK LinearExpression COLON NumericExpression
                                   | LPAREN LogicalExpression RPAREN QUESTION_MARK SymbolicExpression COLON NumericExpression
                                   | LPAREN LogicalExpression RPAREN QUESTION_MARK LinearExpression COLON Identifier
                                   | LPAREN LogicalExpression RPAREN QUESTION_MARK SymbolicExpression COLON Identifier
                                   | LPAREN LogicalExpression RPAREN QUESTION_MARK NumericExpression COLON LinearExpression
                                   | LPAREN LogicalExpression RPAREN QUESTION_MARK NumericExpression COLON SymbolicExpression
                                   | LPAREN LogicalExpression RPAREN QUESTION_MARK Identifier COLON LinearExpression
                                   | LPAREN LogicalExpression RPAREN QUESTION_MARK Identifier COLON SymbolicExpression'''
    if not isinstance(t[2], LogicalExpression):
      t[2] = LogicalExpression([EntryLogicalExpressionNumericOrSymbolic(t[2])])

    t[0] = ConditionalLinearExpression(t[2], t[5])
    t[0].addElseExpression(t[7])

def p_LogicalExpression(t):
    '''LogicalExpression : EntryLogicalExpression
                         | LogicalExpression OR EntryLogicalExpression
                         | LogicalExpression OR NumericExpression
                         | LogicalExpression OR Identifier
                         | LogicalExpression AND EntryLogicalExpression
                         | LogicalExpression AND NumericExpression
                         | LogicalExpression AND Identifier'''

    if len(t) > 3:
      if isinstance(t[3], NumericExpression) or isinstance(t[3], Identifier):
        t[3] = EntryLogicalExpressionNumericOrSymbolic(t[3])

      if re.search(r"\\wedge|\\text\{\s*and\s*\}", t[2]):
        t[0] = t[1].addAnd(t[3])
      else:
        t[0] = t[1].addOr(t[3])
    else:
        t[0] = LogicalExpression([t[1]])

def p_EntryLogicalExpression(t):
    '''EntryLogicalExpression : NOT EntryLogicalExpression
                              | NOT NumericExpression
                              | NOT Identifier
                              | LPAREN LogicalExpression RPAREN'''
    if isinstance(t[2], NumericExpression) or isinstance(t[2], Identifier):
      t[2] = EntryLogicalExpressionNumericOrSymbolic(t[2])

    if isinstance(t[1], str) and re.search(r"!|\\text\{\s*not\s*}", t[1]):
      t[0] = EntryLogicalExpressionNot(t[2])
    elif t[1] == "(":
      t[0] = EntryLogicalExpressionBetweenParenthesis(t[2])
    else:
      t[0] = t[2]

def p_EntryRelationalLogicalExpression(t):
    '''EntryLogicalExpression : NumericExpression LT NumericExpression
                              | NumericExpression LT Identifier
                              | Identifier LT NumericExpression
                              | Identifier LT Identifier
                              | NumericExpression LT SymbolicExpression
                              | Identifier LT SymbolicExpression
                              | SymbolicExpression LT NumericExpression
                              | SymbolicExpression LT Identifier
                              | SymbolicExpression LT SymbolicExpression
                              | NumericExpression LE NumericExpression
                              | NumericExpression LE Identifier
                              | Identifier LE NumericExpression
                              | Identifier LE Identifier
                              | NumericExpression LE SymbolicExpression
                              | Identifier LE SymbolicExpression
                              | SymbolicExpression LE NumericExpression
                              | SymbolicExpression LE Identifier
                              | SymbolicExpression LE SymbolicExpression
                              | NumericExpression EQ NumericExpression
                              | NumericExpression EQ Identifier
                              | Identifier EQ NumericExpression
                              | Identifier EQ Identifier
                              | NumericExpression EQ SymbolicExpression
                              | Identifier EQ SymbolicExpression
                              | SymbolicExpression EQ NumericExpression
                              | SymbolicExpression EQ Identifier
                              | SymbolicExpression EQ SymbolicExpression
                              | NumericExpression GT NumericExpression
                              | NumericExpression GT Identifier
                              | Identifier GT NumericExpression
                              | Identifier GT Identifier
                              | NumericExpression GT SymbolicExpression
                              | Identifier GT SymbolicExpression
                              | SymbolicExpression GT NumericExpression
                              | SymbolicExpression GT Identifier
                              | SymbolicExpression GT SymbolicExpression
                              | NumericExpression GE NumericExpression
                              | NumericExpression GE Identifier
                              | Identifier GE NumericExpression
                              | Identifier GE Identifier
                              | NumericExpression GE SymbolicExpression
                              | Identifier GE SymbolicExpression
                              | SymbolicExpression GE NumericExpression
                              | SymbolicExpression GE Identifier
                              | SymbolicExpression GE SymbolicExpression
                              | NumericExpression NEQ NumericExpression
                              | NumericExpression NEQ Identifier
                              | Identifier NEQ NumericExpression
                              | Identifier NEQ Identifier
                              | NumericExpression NEQ SymbolicExpression
                              | Identifier NEQ SymbolicExpression
                              | SymbolicExpression NEQ NumericExpression
                              | SymbolicExpression NEQ Identifier
                              | SymbolicExpression NEQ SymbolicExpression'''

    if t[2] == "<":
        t[0] = EntryLogicalExpressionRelational(EntryLogicalExpressionRelational.LT, t[1], t[3])
    elif t[2] == "\\leq":
        t[0] = EntryLogicalExpressionRelational(EntryLogicalExpressionRelational.LE, t[1], t[3])
    elif t[2] == "=":
        t[0] = EntryLogicalExpressionRelational(EntryLogicalExpressionRelational.EQ, t[1], t[3])
    elif t[2] == ">":
        t[0] = EntryLogicalExpressionRelational(EntryLogicalExpressionRelational.GT, t[1], t[3])
    elif t[2] == "\\geq":
        t[0] = EntryLogicalExpressionRelational(EntryLogicalExpressionRelational.GE, t[1], t[3])
    elif t[2] == "\\neq":
        t[0] = EntryLogicalExpressionRelational(EntryLogicalExpressionRelational.NEQ, t[1], t[3])

def p_EntryLogicalExpressionWithSet(t):
    '''EntryLogicalExpression : ValueList IN SetExpression
                              | ValueList IN Range
                              | NumericExpression IN SetExpression
                              | NumericExpression IN Range
                              | Identifier IN SetExpression
                              | Identifier IN Range
                              | SymbolicExpression IN SetExpression
                              | SymbolicExpression IN Range
                              | ValueList IN Identifier
                              | NumericExpression IN Identifier
                              | Identifier IN Identifier
                              | SymbolicExpression IN Identifier
                              | Tuple IN SetExpression
                              | Tuple IN Range
                              | Tuple IN Identifier
                              | ValueList NOTIN SetExpression
                              | ValueList NOTIN Range
                              | NumericExpression NOTIN SetExpression
                              | NumericExpression NOTIN Range
                              | Identifier NOTIN SetExpression
                              | Identifier NOTIN Range
                              | SymbolicExpression NOTIN SetExpression
                              | SymbolicExpression NOTIN Range
                              | ValueList NOTIN Identifier
                              | NumericExpression NOTIN Identifier
                              | Identifier NOTIN Identifier
                              | SymbolicExpression NOTIN Identifier
                              | Tuple NOTIN SetExpression
                              | Tuple NOTIN Range
                              | Tuple NOTIN Identifier
                              | SetExpression SUBSET SetExpression
                              | Range SUBSET Range
                              | Identifier SUBSET SetExpression
                              | Identifier SUBSET Range
                              | SetExpression SUBSET Identifier
                              | Range SUBSET Identifier
                              | SetExpression NOTSUBSET SetExpression
                              | Range NOTSUBSET Range
                              | Identifier NOTSUBSET SetExpression
                              | Identifier NOTSUBSET Range
                              | SetExpression NOTSUBSET Identifier
                              | Range NOTSUBSET Identifier'''
    if not isinstance(t[3], SetExpression):
      t[3] = SetExpressionWithValue(t[3])

    if isinstance(t[1], ValueList):
      t[1] = ValueList([t[1]])

    if t[2] == "\\in":
        t[0] = EntryLogicalExpressionWithSet(EntryLogicalExpressionWithSet.IN, t[1], t[3])
    elif t[2] == "\\notin":
        t[0] = EntryLogicalExpressionWithSet(EntryLogicalExpressionWithSet.NOTIN, t[1], t[3])
    elif re.search(r"\\subseteq|\\subset", t[2]):
        t[0] = EntryLogicalExpressionWithSetOperation(EntryLogicalExpressionWithSetOperation.SUBSET, t[1], t[3])
    elif re.search(r"\\not\\subseteq|\\not\\subset", t[2]):
        t[0] = EntryLogicalExpressionWithSetOperation(EntryLogicalExpressionWithSetOperation.NOTSUBSET, t[1], t[3])

def p_EntryIteratedLogicalExpression(t):
    '''EntryLogicalExpression : FORALL LLBRACE IndexingExpression RRBRACE LogicalExpression
                              | FORALL LLBRACE IndexingExpression RRBRACE NumericExpression
                              | FORALL LLBRACE IndexingExpression RRBRACE Identifier
                              | NFORALL LLBRACE IndexingExpression RRBRACE LogicalExpression
                              | NFORALL LLBRACE IndexingExpression RRBRACE NumericExpression
                              | NFORALL LLBRACE IndexingExpression RRBRACE Identifier
                              | EXISTS LLBRACE IndexingExpression RRBRACE LogicalExpression
                              | EXISTS LLBRACE IndexingExpression RRBRACE NumericExpression
                              | EXISTS LLBRACE IndexingExpression RRBRACE Identifier
                              | NEXISTS LLBRACE IndexingExpression RRBRACE LogicalExpression
                              | NEXISTS LLBRACE IndexingExpression RRBRACE NumericExpression
                              | NEXISTS LLBRACE IndexingExpression RRBRACE Identifier'''
    if not isinstance(t[5], LogicalExpression):
      t[5] = LogicalExpression([EntryLogicalExpressionNumericOrSymbolic(t[5])])

    if t[1] == "\\forall":
        t[0] = EntryLogicalExpressionIterated(EntryLogicalExpressionIterated.FORALL, t[3], t[5])
    elif t[1] == "\\not\\forall":
        t[0] = EntryLogicalExpressionIterated(EntryLogicalExpressionIterated.NFORALL, t[3], t[5])
    elif t[1] == "\\exists":
        t[0] = EntryLogicalExpressionIterated(EntryLogicalExpressionIterated.EXISTS, t[3], t[5])
    elif t[1] == "\\nexists" or t[1] == "\\not\\exists":
        t[0] = EntryLogicalExpressionIterated(EntryLogicalExpressionIterated.NEXISTS, t[3], t[5])

def p_SetExpressionWithOperation(t):
    '''SetExpression : Identifier DIFF Identifier
                     | SetExpression DIFF SetExpression
                     | Range DIFF Range
                     | Identifier DIFF SetExpression
                     | Identifier DIFF Range
                     | SetExpression DIFF Identifier
                     | Range DIFF Identifier
                     | SetExpression SYMDIFF SetExpression
                     | Range SYMDIFF Range
                     | Identifier SYMDIFF Identifier
                     | Identifier SYMDIFF SetExpression
                     | Identifier SYMDIFF Range
                     | SetExpression SYMDIFF Identifier
                     | Range SYMDIFF Identifier
                     | SetExpression UNION SetExpression
                     | Range UNION Range
                     | Identifier UNION Identifier
                     | Identifier UNION SetExpression
                     | Identifier UNION Range
                     | SetExpression UNION Identifier
                     | Range UNION Identifier
                     | SetExpression INTER SetExpression
                     | Range INTER Range
                     | Identifier INTER Identifier
                     | Identifier INTER SetExpression
                     | Identifier INTER Range
                     | SetExpression INTER Identifier
                     | Range INTER Identifier
                     | SetExpression CROSS SetExpression
                     | Range CROSS Range
                     | Identifier CROSS Identifier
                     | Identifier CROSS SetExpression
                     | Identifier CROSS Range
                     | SetExpression CROSS Identifier
                     | Range CROSS Identifier'''

    if re.search(r"\\setminus", t[2]):
        op = SetExpressionWithOperation.DIFF
    elif re.search(r"\\triangle|\\ominus", t[2]):
        op = SetExpressionWithOperation.SYMDIFF
    elif re.search(r"\\cup", t[2]):
        op = SetExpressionWithOperation.UNION
    elif re.search(r"\\cap", t[2]):
        op = SetExpressionWithOperation.INTER
    elif re.search(r"\\times", t[2]):
        op = SetExpressionWithOperation.CROSS

    if not isinstance(t[1], SetExpression):
      t[1] = SetExpressionWithValue(t[1])

    if not isinstance(t[3], SetExpression):
      t[3] = SetExpressionWithValue(t[3])

    t[0] = SetExpressionWithOperation(op, t[1], t[3])

def p_SetExpressionWithValue(t):
    '''SetExpression : LLBRACE ValueList RRBRACE
                     | LLBRACE NumericExpression RRBRACE
                     | LLBRACE Identifier RRBRACE
                     | LLBRACE SymbolicExpression RRBRACE
                     | LLBRACE Range RRBRACE
                     | LLBRACE SetExpression RRBRACE
                     | LLBRACE TupleList RRBRACE
                     | LLBRACE IndexingExpression RRBRACE
                     | LLBRACE RRBRACE
                     | LPAREN SetExpression RPAREN
                     | LPAREN Range RPAREN
                     | NATURALSET
                     | INTEGERSET
                     | INTEGERSETPOSITIVE
                     | INTEGERSETNEGATIVE
                     | INTEGERSETWITHONELIMIT
                     | INTEGERSETWITHTWOLIMITS
                     | REALSET
                     | REALSETPOSITIVE
                     | REALSETNEGATIVE
                     | REALSETWITHONELIMIT
                     | REALSETWITHTWOLIMITS
                     | BINARYSET
                     | SYMBOLIC
                     | LOGICAL
                     | PARAMETERS
                     | SETS
                     | VARIABLES'''

    if len(t) > 2:
        if isinstance(t[1], str) and re.search(r"\\\{", t[1]):
          if not (isinstance(t[2], str) and re.search(r"\\\}", t[2])):
            if isinstance(t[2], NumericExpression) or isinstance(t[2], SymbolicExpression) or isinstance(t[2], Identifier):
              t[2] = ValueList([t[2]])

            t[0] = SetExpressionBetweenBraces(SetExpressionWithValue(t[2]))
          else:
            t[0] = SetExpressionBetweenBraces(None)
        elif t[1] == "(":
          t[0] = SetExpressionBetweenParenthesis(t[2])
        else:
          if not isinstance(t[2], SetExpression):
            t[2] = SetExpressionWithValue(t[2])

          t[0] = SetExpressionWithValue(t[2])
    else:
        value = t[1]
        if hasattr(t.slice[1], 'value2'):
          value = t.slice[1].value2
        
        t[0] = SetExpressionWithValue(value)

def p_SetExpressionWithIndices(t):
    '''SetExpression : Identifier LPAREN ValueList RPAREN
                     | Identifier LPAREN NumericExpression RPAREN
                     | Identifier LPAREN Identifier RPAREN
                     | Identifier LPAREN SymbolicExpression RPAREN
                     | Identifier LBRACKET ValueList RBRACKET
                     | Identifier LBRACKET NumericExpression RBRACKET
                     | Identifier LBRACKET Identifier RBRACKET
                     | Identifier LBRACKET SymbolicExpression RBRACKET'''
    if isinstance(t[3], NumericExpression) or isinstance(t[3], SymbolicExpression) or isinstance(t[3], Identifier):
      t[3] = ValueList([t[3]])

    t[0] = SetExpressionWithIndices(t[1], t[3])

def p_IteratedSetExpression(t):
    '''SetExpression : SETOF LLBRACE IndexingExpression RRBRACE ValueList
                     | SETOF LLBRACE IndexingExpression RRBRACE NumericExpression
                     | SETOF LLBRACE IndexingExpression RRBRACE Identifier
                     | SETOF LLBRACE IndexingExpression RRBRACE SymbolicExpression
                     | SETOF LLBRACE IndexingExpression RRBRACE LPAREN ValueList RPAREN'''
    
    if t[5] == "(":
      t[0] = IteratedSetExpression(t[3], t[6])
    else:
      if isinstance(t[5], NumericExpression) or isinstance(t[5], SymbolicExpression) or isinstance(t[5], Identifier):
        t[5] = ValueList([t[5]])

      t[0] = IteratedSetExpression(t[3], [t[5]])

def p_IndexingExpression(t):
    '''IndexingExpression : EntryIndexingExpression
                          | IndexingExpression PIPE LogicalExpression
                          | IndexingExpression PIPE NumericExpression
                          | IndexingExpression PIPE Identifier
                          | IndexingExpression COMMA EntryIndexingExpression'''

    #if len(t) > 4:
    #    t[0] = t[1].add(t[4])
    if len(t) > 3:
        if re.search(r"\\mid|\\vert|\|", t[2]):
            if isinstance(t[3], NumericExpression) or isinstance(t[3], Identifier):
              t[3] = LogicalExpression([EntryLogicalExpressionNumericOrSymbolic(t[3])])

            t[0] = t[1].setLogicalExpression(t[3])
        else:
            t[0] = t[1].add(t[3])
    else:
        t[0] = IndexingExpression([t[1]])

def p_EntryIndexingExpressionWithSet(t):
    '''EntryIndexingExpression : ValueList IN SetExpression
                               | ValueList IN Range
                               | NumericExpression IN SetExpression
                               | NumericExpression IN Range
                               | Identifier IN SetExpression
                               | Identifier IN Range
                               | SymbolicExpression IN SetExpression
                               | SymbolicExpression IN Range
                               | ValueList IN Identifier
                               | NumericExpression IN Identifier
                               | Identifier IN Identifier
                               | SymbolicExpression IN Identifier
                               | Tuple IN SetExpression
                               | Tuple IN Range
                               | Tuple IN Identifier'''

    if not isinstance(t[3], SetExpression):
      t[3] = SetExpressionWithValue(t[3])

    if isinstance(t[1], NumericExpression) or isinstance(t[1], SymbolicExpression) or isinstance(t[1], Identifier):
      t[1] = ValueList([t[1]])

    t[0] = EntryIndexingExpressionWithSet(t[1], t[3])

def p_EntryIndexingExpressionEq(t):
    '''EntryIndexingExpression : Identifier EQ NumericExpression
                               | Identifier EQ Identifier
                               | Identifier EQ Range
                               | Identifier NEQ NumericExpression
                               | Identifier NEQ Identifier
                               | Identifier LE NumericExpression
                               | Identifier LE Identifier
                               | Identifier GE NumericExpression
                               | Identifier GE Identifier
                               | Identifier LT NumericExpression
                               | Identifier LT Identifier
                               | Identifier GT NumericExpression
                               | Identifier GT Identifier'''
    if t[2] == "=":
        t[0] = EntryIndexingExpressionEq(EntryIndexingExpressionEq.EQ, t[1], t[3])
    elif t[2] == "\\neq":
        t[0] = EntryIndexingExpressionEq(EntryIndexingExpressionEq.NEQ, t[1], t[3])
    elif t[2] == "\\leq":
        t[0] = EntryIndexingExpressionCmp(EntryIndexingExpressionCmp.LE, t[1], t[3])
    elif t[2] == "\\geq":
        t[0] = EntryIndexingExpressionCmp(EntryIndexingExpressionCmp.GE, t[1], t[3])
    elif t[2] == "<":
        t[0] = EntryIndexingExpressionCmp(EntryIndexingExpressionCmp.LT, t[1], t[3])
    elif t[2] == ">":
        t[0] = EntryIndexingExpressionCmp(EntryIndexingExpressionCmp.GT, t[1], t[3])

def p_StringSymbolicExpression(t):
    '''SymbolicExpression : LPAREN SymbolicExpression RPAREN
                          | STRING'''

    if len(t) > 2:
        t[0] = SymbolicExpressionBetweenParenthesis(t[2])
    else:
        t[0] = StringSymbolicExpression(t[1])

def p_SymbolicExpression_binop(t):
    '''SymbolicExpression : NumericExpression AMPERSAND NumericExpression
                          | NumericExpression AMPERSAND Identifier
                          | Identifier AMPERSAND NumericExpression
                          | Identifier AMPERSAND Identifier
                          | NumericExpression AMPERSAND SymbolicExpression
                          | Identifier AMPERSAND SymbolicExpression
                          | SymbolicExpression AMPERSAND NumericExpression
                          | SymbolicExpression AMPERSAND Identifier
                          | SymbolicExpression AMPERSAND SymbolicExpression'''
    if re.search(r"\\&", t[2]):
        op = SymbolicExpressionWithOperation.CONCAT

    t[0] = SymbolicExpressionWithOperation(op, t[1], t[3])

def p_FunctionSymbolicExpression(t):
    '''SymbolicExpression : SUBSTR LPAREN NumericExpression COMMA NumericExpression COMMA NumericExpression RPAREN
                          | SUBSTR LPAREN NumericExpression COMMA NumericExpression COMMA Identifier RPAREN
                          | SUBSTR LPAREN NumericExpression COMMA Identifier COMMA NumericExpression RPAREN
                          | SUBSTR LPAREN NumericExpression COMMA Identifier COMMA Identifier RPAREN
                          | SUBSTR LPAREN Identifier COMMA NumericExpression COMMA NumericExpression RPAREN
                          | SUBSTR LPAREN Identifier COMMA NumericExpression COMMA Identifier RPAREN
                          | SUBSTR LPAREN Identifier COMMA Identifier COMMA NumericExpression RPAREN
                          | SUBSTR LPAREN Identifier COMMA Identifier COMMA Identifier RPAREN
                          | SUBSTR LPAREN SymbolicExpression COMMA NumericExpression COMMA NumericExpression RPAREN
                          | SUBSTR LPAREN SymbolicExpression COMMA NumericExpression COMMA Identifier RPAREN
                          | SUBSTR LPAREN SymbolicExpression COMMA Identifier COMMA NumericExpression RPAREN
                          | SUBSTR LPAREN SymbolicExpression COMMA Identifier COMMA Identifier RPAREN
                          | SUBSTR LPAREN NumericExpression COMMA NumericExpression RPAREN
                          | SUBSTR LPAREN NumericExpression COMMA Identifier RPAREN
                          | SUBSTR LPAREN Identifier COMMA NumericExpression RPAREN
                          | SUBSTR LPAREN Identifier COMMA Identifier RPAREN
                          | SUBSTR LPAREN SymbolicExpression COMMA NumericExpression RPAREN
                          | SUBSTR LPAREN SymbolicExpression COMMA Identifier RPAREN
                          | TIME2STR LPAREN NumericExpression COMMA NumericExpression RPAREN
                          | TIME2STR LPAREN NumericExpression COMMA Identifier RPAREN
                          | TIME2STR LPAREN Identifier COMMA NumericExpression RPAREN
                          | TIME2STR LPAREN Identifier COMMA Identifier RPAREN
                          | TIME2STR LPAREN NumericExpression COMMA SymbolicExpression RPAREN
                          | TIME2STR LPAREN Identifier COMMA SymbolicExpression RPAREN'''

    if t[1] == "substr":
        op = SymbolicExpressionWithFunction.SUBSTR
    elif t[1] == "time2str":
        op = SymbolicExpressionWithFunction.TIME2STR

    if len(t) > 7:
        t[0] = SymbolicExpressionWithFunction(op, t[3], t[5], t[7])
    else:
        if t[1] == "substr":
            t[0] = SymbolicExpressionWithFunction(op, t[3], t[5])
        else:
            t[0] = SymbolicExpressionWithFunction(op, t[5], t[3])

def p_NumericExpression_binop(t):
    '''NumericExpression : NumericExpression PLUS NumericExpression
                         | NumericExpression PLUS Identifier
                         | Identifier PLUS NumericExpression
                         | Identifier PLUS Identifier
                         | NumericExpression MINUS NumericExpression
                         | NumericExpression MINUS Identifier
                         | Identifier MINUS NumericExpression
                         | Identifier MINUS Identifier
                         | NumericExpression TIMES NumericExpression
                         | NumericExpression TIMES Identifier
                         | Identifier TIMES NumericExpression
                         | Identifier TIMES Identifier
                         | NumericExpression DIVIDE NumericExpression
                         | NumericExpression DIVIDE Identifier
                         | Identifier DIVIDE NumericExpression
                         | Identifier DIVIDE Identifier
                         | NumericExpression MOD NumericExpression
                         | NumericExpression MOD Identifier
                         | Identifier MOD NumericExpression
                         | Identifier MOD Identifier
                         | NumericExpression QUOTIENT NumericExpression
                         | NumericExpression QUOTIENT Identifier
                         | Identifier QUOTIENT NumericExpression
                         | Identifier QUOTIENT Identifier
                         | NumericExpression LESS NumericExpression
                         | NumericExpression LESS Identifier
                         | Identifier LESS NumericExpression
                         | Identifier LESS Identifier
                         | NumericExpression CARET LBRACE NumericExpression RBRACE
                         | NumericExpression CARET LBRACE Identifier RBRACE
                         | Identifier CARET LBRACE NumericExpression RBRACE
                         | Identifier CARET LBRACE Identifier RBRACE'''

    if t[2] == "+":
        op = NumericExpressionWithArithmeticOperation.PLUS
    elif t[2] == "-":
        op = NumericExpressionWithArithmeticOperation.MINUS
    elif re.search(r"\*|\\cdot|\\ast", t[2]):
        op = NumericExpressionWithArithmeticOperation.TIMES
    elif re.search(r"/|\\div", t[2]):
        op = NumericExpressionWithArithmeticOperation.DIV
    elif re.search(r"\\text\{\s*\%\s*\}|\\mod|\\bmod", t[2]):
        op = NumericExpressionWithArithmeticOperation.MOD
    elif t[2] == "^":
        op = NumericExpressionWithArithmeticOperation.POW
    elif re.search(r"\\big/|\\text\{\s*div\s*\}", t[2]):
        op = NumericExpressionWithArithmeticOperation.QUOT
    elif re.search(r"\\text\{\s*less\s*\}", t[2]):
        op = NumericExpressionWithArithmeticOperation.LESS

    if len(t) > 4 and isinstance(t[4], Identifier):
      t[4] = ValuedNumericExpression(t[4])
    elif len(t) > 3 and isinstance(t[3], Identifier):
      t[3] = ValuedNumericExpression(t[3])
    elif isinstance(t[1], Identifier):
      t[1] = ValuedNumericExpression(t[1])

    if t[2] == "^":
      t[0] = NumericExpressionWithArithmeticOperation(op, t[1], t[4])
    else:
      t[0] = NumericExpressionWithArithmeticOperation(op, t[1], t[3])

def p_IteratedNumericExpression(t):
    '''NumericExpression : SUM UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE NumericExpression RBRACE NumericExpression
                         | SUM UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE NumericExpression RBRACE Identifier
                         | SUM UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE Identifier RBRACE NumericExpression
                         | SUM UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE Identifier RBRACE Identifier
                         | SUM UNDERLINE LBRACE IndexingExpression RBRACE NumericExpression
                         | SUM UNDERLINE LBRACE IndexingExpression RBRACE Identifier
                         | PROD UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE NumericExpression RBRACE NumericExpression
                         | PROD UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE NumericExpression RBRACE Identifier
                         | PROD UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE Identifier RBRACE NumericExpression
                         | PROD UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE Identifier RBRACE Identifier
                         | PROD UNDERLINE LBRACE IndexingExpression RBRACE NumericExpression
                         | PROD UNDERLINE LBRACE IndexingExpression RBRACE Identifier
                         | MAX UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE NumericExpression RBRACE NumericExpression
                         | MAX UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE NumericExpression RBRACE Identifier
                         | MAX UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE Identifier RBRACE NumericExpression
                         | MAX UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE Identifier RBRACE Identifier
                         | MAX UNDERLINE LBRACE IndexingExpression RBRACE NumericExpression
                         | MAX UNDERLINE LBRACE IndexingExpression RBRACE Identifier
                         | MIN UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE NumericExpression RBRACE NumericExpression
                         | MIN UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE NumericExpression RBRACE Identifier
                         | MIN UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE Identifier RBRACE NumericExpression
                         | MIN UNDERLINE LBRACE IndexingExpression RBRACE CARET LBRACE Identifier RBRACE Identifier
                         | MIN UNDERLINE LBRACE IndexingExpression RBRACE NumericExpression
                         | MIN UNDERLINE LBRACE IndexingExpression RBRACE Identifier'''

    if t[1] == "\\sum":
        op = IteratedNumericExpression.SUM
    elif t[1] == "\\prod":
        op = IteratedNumericExpression.PROD
    elif t[1] == "\\max":
        op = IteratedNumericExpression.MAX
    elif t[1] == "\\min":
        op = IteratedNumericExpression.MIN

    if len(t) > 7:
        if isinstance(t[8], Identifier):
          t[8] = ValuedNumericExpression(t[8])

        if isinstance(t[10], Identifier):
          t[10] = ValuedNumericExpression(t[10])

        t[0] = IteratedNumericExpression(op, t[10], t[4], t[8])
    else:
        if isinstance(t[6], Identifier):
          t[6] = ValuedNumericExpression(t[6])

        t[0] = IteratedNumericExpression(op, t[6], t[4])

def p_NumericExpression(t):
    '''NumericExpression : MINUS NumericExpression %prec UMINUS
                         | MINUS Identifier %prec UMINUS
                         | PLUS NumericExpression %prec UPLUS
                         | PLUS Identifier %prec UPLUS
                         | LPAREN NumericExpression RPAREN
                         | LPAREN Identifier RPAREN
                         | ConditionalNumericExpression
                         | NUMBER'''

    if len(t) > 2 and isinstance(t[2], Identifier):
      t[2] = ValuedNumericExpression(t[2])

    if len(t) > 3:
      t[0] = NumericExpressionBetweenParenthesis(t[2])
    elif t[1] == "+":
      t[0] = t[2]
    elif t[1] == "-":
      t[0] = MinusNumericExpression(t[2])
    elif isinstance(t[1], ConditionalNumericExpression):
      t[0] = t[1]
    else:
      t[0] = ValuedNumericExpression(t[1])

def p_FunctionNumericExpression(t):
    '''NumericExpression : SQRT LBRACE NumericExpression RBRACE
                         | SQRT LBRACE Identifier RBRACE
                         | LFLOOR NumericExpression RFLOOR
                         | LFLOOR Identifier RFLOOR
                         | LCEIL NumericExpression RCEIL
                         | LCEIL Identifier RCEIL
                         | PIPE NumericExpression PIPE
                         | PIPE Identifier PIPE
                         | MAX LPAREN ValueList RPAREN
                         | MAX LPAREN NumericExpression RPAREN
                         | MAX LPAREN Identifier RPAREN
                         | MAX LPAREN SymbolicExpression RPAREN
                         | MIN LPAREN ValueList RPAREN
                         | MIN LPAREN NumericExpression RPAREN
                         | MIN LPAREN Identifier RPAREN
                         | MIN LPAREN SymbolicExpression RPAREN
                         | SIN LPAREN NumericExpression RPAREN
                         | SIN LPAREN Identifier RPAREN
                         | COS LPAREN NumericExpression RPAREN
                         | COS LPAREN Identifier RPAREN
                         | LOG LPAREN NumericExpression RPAREN
                         | LOG LPAREN Identifier RPAREN
                         | LN LPAREN NumericExpression RPAREN
                         | LN LPAREN Identifier RPAREN
                         | EXP LPAREN NumericExpression RPAREN
                         | EXP LPAREN Identifier RPAREN
                         | ARCTAN LPAREN NumericExpression RPAREN
                         | ARCTAN LPAREN Identifier RPAREN
                         | ARCTAN LPAREN NumericExpression COMMA NumericExpression RPAREN
                         | ARCTAN LPAREN NumericExpression COMMA Identifier RPAREN
                         | ARCTAN LPAREN Identifier COMMA NumericExpression RPAREN
                         | ARCTAN LPAREN Identifier COMMA Identifier RPAREN
                         | CARD LPAREN SetExpression RPAREN
                         | CARD LPAREN Range RPAREN
                         | CARD LPAREN Identifier RPAREN
                         | LENGTH LPAREN NumericExpression RPAREN
                         | LENGTH LPAREN Identifier RPAREN
                         | LENGTH LPAREN SymbolicExpression RPAREN
                         | ROUND LPAREN NumericExpression RPAREN
                         | ROUND LPAREN Identifier RPAREN
                         | ROUND LPAREN NumericExpression COMMA NumericExpression RPAREN
                         | ROUND LPAREN NumericExpression COMMA Identifier RPAREN
                         | ROUND LPAREN Identifier COMMA NumericExpression RPAREN
                         | ROUND LPAREN Identifier COMMA Identifier RPAREN
                         | STR2TIME LPAREN NumericExpression COMMA NumericExpression RPAREN
                         | STR2TIME LPAREN NumericExpression COMMA Identifier RPAREN
                         | STR2TIME LPAREN Identifier COMMA NumericExpression RPAREN
                         | STR2TIME LPAREN Identifier COMMA Identifier RPAREN
                         | STR2TIME LPAREN NumericExpression COMMA SymbolicExpression RPAREN
                         | STR2TIME LPAREN Identifier COMMA SymbolicExpression RPAREN
                         | STR2TIME LPAREN SymbolicExpression COMMA NumericExpression RPAREN
                         | STR2TIME LPAREN SymbolicExpression COMMA Identifier RPAREN
                         | STR2TIME LPAREN SymbolicExpression COMMA SymbolicExpression RPAREN
                         | TRUNC LPAREN NumericExpression RPAREN
                         | TRUNC LPAREN Identifier RPAREN
                         | TRUNC LPAREN NumericExpression COMMA NumericExpression RPAREN
                         | TRUNC LPAREN NumericExpression COMMA Identifier RPAREN
                         | TRUNC LPAREN Identifier COMMA NumericExpression RPAREN
                         | TRUNC LPAREN Identifier COMMA Identifier RPAREN
                         | UNIFORM LPAREN NumericExpression COMMA NumericExpression RPAREN
                         | UNIFORM LPAREN NumericExpression COMMA Identifier RPAREN
                         | UNIFORM LPAREN Identifier COMMA NumericExpression RPAREN
                         | UNIFORM LPAREN Identifier COMMA Identifier RPAREN
                         | NORMAL LPAREN NumericExpression COMMA NumericExpression RPAREN
                         | NORMAL LPAREN NumericExpression COMMA Identifier RPAREN
                         | NORMAL LPAREN Identifier COMMA NumericExpression RPAREN
                         | NORMAL LPAREN Identifier COMMA Identifier RPAREN
                         | GMTIME LPAREN RPAREN
                         | IRAND224 LPAREN RPAREN
                         | UNIFORM01 LPAREN RPAREN
                         | NORMAL01 LPAREN RPAREN'''

    if t[1] == "card":
        op = NumericExpressionWithFunction.CARD

        if not isinstance(t[3], SetExpression):
          t[3] = SetExpressionWithValue(t[3])

    elif t[1] == "length":
        op = NumericExpressionWithFunction.LENGTH
    elif t[1] == "round":
        op = NumericExpressionWithFunction.ROUND
    elif t[1] == "trunc":
        op = NumericExpressionWithFunction.TRUNC
    elif t[1] == "\\sqrt":
        op = NumericExpressionWithFunction.SQRT
    elif t[1] == "\\lfloor":
        op = NumericExpressionWithFunction.FLOOR
    elif t[1] == "\\lceil":
        op = NumericExpressionWithFunction.CEIL
    elif re.search(r"\\mid|\\vert|\|", t[1]):
        op = NumericExpressionWithFunction.ABS
    elif t[1] == "\\max":
        op = NumericExpressionWithFunction.MAX
    elif t[1] == "\\min":
        op = NumericExpressionWithFunction.MIN
    elif t[1] == "\\sin":
        op = NumericExpressionWithFunction.SIN
    elif t[1] == "\\cos":
        op = NumericExpressionWithFunction.COS
    elif t[1] == "\\log":
        op = NumericExpressionWithFunction.LOG10
    elif t[1] == "\\ln":
        op = NumericExpressionWithFunction.LOG
    elif t[1] == "\\exp":
        op = NumericExpressionWithFunction.EXP
    elif t[1] == "\\arctan":
        op = NumericExpressionWithFunction.ATAN
    elif t[1] == "Uniform01":
        op = NumericExpressionWithFunction.UNIFORM01
    elif t[1] == "Uniform":
        op = NumericExpressionWithFunction.UNIFORM
    elif t[1] == "Normal01":
        op = NumericExpressionWithFunction.NORMAL01
    elif t[1] == "Normal":
        op = NumericExpressionWithFunction.NORMAL
    elif t[1] == "gmtime":
        op = NumericExpressionWithFunction.GMTIME
    elif t[1] == "Irand224":
        op = NumericExpressionWithFunction.IRAND224
    elif t[1] == "str2time":
        op = NumericExpressionWithFunction.STR2TIME

    if len(t) > 5:
        if isinstance(t[3], NumericExpression) or isinstance(t[3], SymbolicExpression) or isinstance(t[3], Identifier):
          t[3] = ValueList([t[3]])

        t[0] = NumericExpressionWithFunction(op, t[3], t[5])
    elif len(t) > 4:
        if isinstance(t[3], NumericExpression) or isinstance(t[3], SymbolicExpression) or isinstance(t[3], Identifier):
          t[3] = ValueList([t[3]])

        t[0] = NumericExpressionWithFunction(op, t[3])
    else:
        if t[2] == "(":
          t[0] = NumericExpressionWithFunction(op)
        else:
          t[0] = NumericExpressionWithFunction(op, t[2])

def p_ConditionalNumericExpression(t):
    '''ConditionalNumericExpression : LPAREN Identifier RPAREN QUESTION_MARK NumericExpression COLON NumericExpression
                                    | LPAREN Identifier RPAREN QUESTION_MARK NumericExpression COLON Identifier
                                    | LPAREN Identifier RPAREN QUESTION_MARK Identifier COLON NumericExpression
                                    | LPAREN Identifier RPAREN QUESTION_MARK Identifier COLON Identifier
                                    | LPAREN NumericExpression RPAREN QUESTION_MARK NumericExpression COLON NumericExpression
                                    | LPAREN NumericExpression RPAREN QUESTION_MARK NumericExpression COLON Identifier
                                    | LPAREN NumericExpression RPAREN QUESTION_MARK Identifier COLON NumericExpression
                                    | LPAREN NumericExpression RPAREN QUESTION_MARK Identifier COLON Identifier
                                    | LPAREN LogicalExpression RPAREN QUESTION_MARK NumericExpression COLON NumericExpression
                                    | LPAREN LogicalExpression RPAREN QUESTION_MARK NumericExpression COLON Identifier
                                    | LPAREN LogicalExpression RPAREN QUESTION_MARK Identifier COLON NumericExpression
                                    | LPAREN LogicalExpression RPAREN QUESTION_MARK Identifier COLON Identifier'''
    if isinstance(t[2], NumericExpression) or isinstance(t[2], Identifier):
      t[2] = LogicalExpression([EntryLogicalExpressionNumericOrSymbolic(t[2])])
    
    if isinstance(t[5], Identifier):
      t[5] = ValuedNumericExpression(t[5])

    if isinstance(t[7], Identifier):
      t[7] = ValuedNumericExpression(t[7])

    t[0] = ConditionalNumericExpression(t[2], t[5])
    t[0].addElseExpression(t[7])

#def p_NumericOrSymbolicExpression(t):
#    '''NumericOrSymbolicExpression : NumericExpression
#                                   | SymbolicExpression'''
#    t[0] = t[1]


def p_Range(t):
    '''Range : NumericExpression DOTS NumericExpression BY NumericExpression
             | NumericExpression DOTS NumericExpression BY Identifier
             | NumericExpression DOTS Identifier BY NumericExpression
             | NumericExpression DOTS Identifier BY Identifier
             | Identifier DOTS NumericExpression BY NumericExpression
             | Identifier DOTS NumericExpression BY Identifier
             | Identifier DOTS Identifier BY NumericExpression
             | Identifier DOTS Identifier BY Identifier
             | NumericExpression DOTS NumericExpression
             | NumericExpression DOTS Identifier
             | Identifier DOTS NumericExpression
             | Identifier DOTS Identifier'''

    if len(t) > 4:
      t[0] = Range(t[1], t[3], t[5])
    else:
      t[0] = Range(t[1], t[3])

def p_Identifier(t):
    '''Identifier : ID UNDERLINE LBRACE ValueList RBRACE
                | ID UNDERLINE LBRACE NumericExpression RBRACE
                | ID UNDERLINE LBRACE Identifier RBRACE
                | ID UNDERLINE LBRACE SymbolicExpression RBRACE
                | ID LBRACKET ValueList RBRACKET
                | ID LBRACKET NumericExpression RBRACKET
                | ID LBRACKET Identifier RBRACKET
                | ID LBRACKET SymbolicExpression RBRACKET
                | ID'''

    if len(t) > 5:
        if isinstance(t[4], ValueList):
          t[0] = Identifier(ID(t[1]), t[4].getValues())
        else:
          t[0] = Identifier(ID(t[1]), [t[4]])
    elif len(t) > 2:
        if isinstance(t[3], ValueList):
          t[0] = Identifier(ID(t[1]), t[3].getValues())
        else:
          t[0] = Identifier(ID(t[1]), [t[3]])
    else:
        t[0] = Identifier(ID(t[1]))

def p_ValueList(t):
    '''ValueList : ValueList COMMA NumericExpression
                 | ValueList COMMA Identifier
                 | ValueList COMMA SymbolicExpression
                 | NumericExpression COMMA NumericExpression
                 | NumericExpression COMMA Identifier
                 | Identifier COMMA NumericExpression
                 | Identifier COMMA Identifier
                 | NumericExpression COMMA SymbolicExpression
                 | Identifier COMMA SymbolicExpression
                 | SymbolicExpression COMMA NumericExpression
                 | SymbolicExpression COMMA Identifier
                 | SymbolicExpression COMMA SymbolicExpression'''

    if not isinstance(t[1], ValueList):
        t[0] = ValueList([t[1],t[3]])
    else:
        t[0] = t[1].add(t[3])

def p_IdentifierList(t):
    '''IdentifierList : IdentifierList COMMA ID
                      | ID COMMA ID'''

    if not isinstance(t[1], ValueList):
        t[0] = ValueList([Identifier(ID(t[1])),Identifier(ID(t[3]))])
    else:
        t[0] = t[1].add(Identifier(ID(t[3])))

def p_Tuple(t):
    '''Tuple : LPAREN IdentifierList RPAREN'''

    t[0] = Tuple(t[2].getValues())

def p_TupleListItem(t):
    '''TupleListItem : LPAREN ValueList RPAREN
                     | Tuple'''

    if len(t) > 2:
      t[0] = Tuple(t[2].getValues())
    else:
      t[0] = t[1]


def p_TupleList(t):
    '''TupleList : TupleList COMMA TupleListItem
                 | TupleListItem'''

    if not isinstance(t[1], TupleList):
        t[0] = TupleList([t[1]])
    else:
        t[0] = t[1].add(t[3])

def p_error(t):
  if t:
    raise SyntaxException(t.lineno, t.lexpos, t.value)
  else:
    raise SyntaxException("EOF")