
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIDleftNUMBERINFINITYleftINTEGRALDIFFERENTIALrightCOMMArightPIPErightLPARENRPARENrightLBRACERBRACEFRACleftPLUSMINUSleftTIMESDIVIDEMODQUOTIENTrightCARETleftLFLOORRFLOORLCEILRCEILSINCOSTANATANSQRTLNLOGEXPFRAC NUMBER PLUS MINUS TIMES DIVIDE QUOTIENT LPAREN RPAREN LBRACE RBRACE LFLOOR RFLOOR LCEIL RCEIL SIN COS TAN ATAN SQRT LOG LN EXP MOD CARET COMMA ID PIPE INFINITY UNDERLINE INTEGRAL DIFFERENTIALMAIN : ExpressionFactor : NUMBER\n            | Identifier\n            | INFINITY\n            | LPAREN Expression RPARENTerm : Term TIMES Factor\n          | Term DIVIDE Factor\n          | Term MOD Factor\n          | Term QUOTIENT Factor\n          | Term CARET LBRACE Factor RBRACE\n          | FactorExpression : Expression PLUS Term\n                  | Expression MINUS Term\n                  | TermExpression : FRAC LBRACE Expression RBRACE LBRACE Expression RBRACEFactor : SQRT LBRACE Expression RBRACE\n                         \n              | LFLOOR Expression RFLOOR\n                         \n              | LCEIL Expression RCEIL\n                         \n              | PIPE Expression PIPE\n                         \n              | SIN LPAREN Expression RPAREN\n                         \n              | COS LPAREN Expression RPAREN\n\n              | TAN LPAREN Expression RPAREN\n                         \n              | ATAN LPAREN Expression COMMA Expression RPAREN\n              | ATAN LPAREN Expression RPAREN\n                         \n              | LOG LPAREN Expression RPAREN\n                         \n              | LN LPAREN Expression RPAREN\n                         \n              | EXP LPAREN Expression RPAREN\n\n              | Identifier LPAREN ExpressionList RPAREN\n\n              | Identifier LPAREN RPARENFactor : INTEGRAL UNDERLINE LBRACE Expression RBRACE CARET LBRACE Expression RBRACE Expression DIFFERENTIALIdentifier : IDExpressionList : ExpressionList COMMA Expression\n                    | Expression'
    
_lr_action_items = {'LFLOOR':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]),'CARET':([6,8,9,14,18,20,45,48,53,56,57,58,59,62,63,66,67,69,70,72,73,74,75,78,80,82,83,84,90,96,],[-2,-11,-4,33,-3,-31,-17,-18,-19,-7,-6,-8,-9,-5,-29,33,33,-21,-25,-27,-26,-20,-22,-24,-28,-16,88,-10,-23,-30,]),'COS':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'LOG':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'INTEGRAL':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'NUMBER':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'RFLOOR':([6,8,9,14,18,20,23,45,48,53,56,57,58,59,62,63,66,67,69,70,72,73,74,75,78,80,82,84,90,92,96,],[-2,-11,-4,-14,-3,-31,45,-17,-18,-19,-7,-6,-8,-9,-5,-29,-12,-13,-21,-25,-27,-26,-20,-22,-24,-28,-16,-10,-23,-15,-30,]),'EXP':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'FRAC':([0,1,4,12,17,24,25,28,29,30,32,38,39,41,44,49,79,81,85,91,94,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'RCEIL':([6,8,9,14,18,20,26,45,48,53,56,57,58,59,62,63,66,67,69,70,72,73,74,75,78,80,82,84,90,92,96,],[-2,-11,-4,-14,-3,-31,48,-17,-18,-19,-7,-6,-8,-9,-5,-29,-12,-13,-21,-25,-27,-26,-20,-22,-24,-28,-16,-10,-23,-15,-30,]),'SIN':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'RBRACE':([6,8,9,14,18,20,45,48,53,56,57,58,59,60,62,63,66,67,68,69,70,71,72,73,74,75,76,78,80,82,84,89,90,92,93,96,],[-2,-11,-4,-14,-3,-31,-17,-18,-19,-7,-6,-8,-9,77,-5,-29,-12,-13,82,-21,-25,83,-27,-26,-20,-22,84,-24,-28,-16,-10,92,-23,-15,94,-30,]),'RPAREN':([6,8,9,14,18,20,40,41,45,46,47,48,50,51,52,53,54,56,57,58,59,61,62,63,64,65,66,67,69,70,72,73,74,75,78,80,82,84,86,87,90,92,96,],[-2,-11,-4,-14,-3,-31,62,63,-17,69,70,-18,72,73,74,-19,75,-7,-6,-8,-9,78,-5,-29,80,-33,-12,-13,-21,-25,-27,-26,-20,-22,-24,-28,-16,-10,90,-32,-23,-15,-30,]),'LN':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'MINUS':([6,8,9,14,18,19,20,23,26,31,40,45,46,47,48,50,51,52,53,54,56,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,78,80,82,84,86,87,89,90,92,93,95,96,],[-2,-11,-4,-14,-3,43,-31,43,43,43,43,-17,43,43,-18,43,43,43,-19,43,-7,-6,-8,-9,43,43,-5,-29,43,-12,-13,43,-21,-25,43,-27,-26,-20,-22,-24,-28,-16,-10,43,43,43,-23,-15,43,43,-30,]),'PIPE':([0,1,4,6,8,9,12,14,17,18,20,24,25,28,29,30,31,32,34,35,36,37,38,39,41,42,43,44,45,48,49,53,55,56,57,58,59,62,63,66,67,69,70,72,73,74,75,78,79,80,81,82,84,85,90,91,92,94,96,],[12,12,12,-2,-11,-4,12,-14,12,-3,-31,12,12,12,12,12,53,12,12,12,12,12,12,12,12,12,12,12,-17,-18,12,-19,12,-7,-6,-8,-9,-5,-29,-12,-13,-21,-25,-27,-26,-20,-22,-24,12,-28,12,-16,-10,12,-23,12,-15,12,-30,]),'PLUS':([6,8,9,14,18,19,20,23,26,31,40,45,46,47,48,50,51,52,53,54,56,57,58,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,78,80,82,84,86,87,89,90,92,93,95,96,],[-2,-11,-4,-14,-3,42,-31,42,42,42,42,-17,42,42,-18,42,42,42,-19,42,-7,-6,-8,-9,42,42,-5,-29,42,-12,-13,42,-21,-25,42,-27,-26,-20,-22,-24,-28,-16,-10,42,42,42,-23,-15,42,42,-30,]),'COMMA':([6,8,9,14,18,20,45,48,53,56,57,58,59,61,62,63,64,65,66,67,69,70,72,73,74,75,78,80,82,84,87,90,92,96,],[-2,-11,-4,-14,-3,-31,-17,-18,-19,-7,-6,-8,-9,79,-5,-29,81,-33,-12,-13,-21,-25,-27,-26,-20,-22,-24,-28,-16,-10,-32,-23,-15,-30,]),'TAN':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'UNDERLINE':([5,],[27,]),'$end':([6,8,9,14,18,19,20,22,45,48,53,56,57,58,59,62,63,66,67,69,70,72,73,74,75,78,80,82,84,90,92,96,],[-2,-11,-4,-14,-3,-1,-31,0,-17,-18,-19,-7,-6,-8,-9,-5,-29,-12,-13,-21,-25,-27,-26,-20,-22,-24,-28,-16,-10,-23,-15,-30,]),'LCEIL':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'INFINITY':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'DIVIDE':([6,8,9,14,18,20,45,48,53,56,57,58,59,62,63,66,67,69,70,72,73,74,75,78,80,82,84,90,96,],[-2,-11,-4,34,-3,-31,-17,-18,-19,-7,-6,-8,-9,-5,-29,34,34,-21,-25,-27,-26,-20,-22,-24,-28,-16,-10,-23,-30,]),'ATAN':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'TIMES':([6,8,9,14,18,20,45,48,53,56,57,58,59,62,63,66,67,69,70,72,73,74,75,78,80,82,84,90,96,],[-2,-11,-4,35,-3,-31,-17,-18,-19,-7,-6,-8,-9,-5,-29,35,35,-21,-25,-27,-26,-20,-22,-24,-28,-16,-10,-23,-30,]),'LPAREN':([0,1,2,3,4,7,10,11,12,13,16,17,18,20,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[17,17,24,25,17,28,29,30,17,32,39,17,41,-31,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'ID':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'LBRACE':([15,21,27,33,77,88,],[38,44,49,55,85,91,]),'DIFFERENTIAL':([6,8,9,14,18,20,45,48,53,56,57,58,59,62,63,66,67,69,70,72,73,74,75,78,80,82,84,90,92,95,96,],[-2,-11,-4,-14,-3,-31,-17,-18,-19,-7,-6,-8,-9,-5,-29,-12,-13,-21,-25,-27,-26,-20,-22,-24,-28,-16,-10,-23,-15,96,-30,]),'SQRT':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'QUOTIENT':([6,8,9,14,18,20,45,48,53,56,57,58,59,62,63,66,67,69,70,72,73,74,75,78,80,82,84,90,96,],[-2,-11,-4,37,-3,-31,-17,-18,-19,-7,-6,-8,-9,-5,-29,37,37,-21,-25,-27,-26,-20,-22,-24,-28,-16,-10,-23,-30,]),'MOD':([6,8,9,14,18,20,45,48,53,56,57,58,59,62,63,66,67,69,70,72,73,74,75,78,80,82,84,90,96,],[-2,-11,-4,36,-3,-31,-17,-18,-19,-7,-6,-8,-9,-5,-29,36,36,-21,-25,-27,-26,-20,-22,-24,-28,-16,-10,-23,-30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Term':([0,1,4,12,17,24,25,28,29,30,32,38,39,41,42,43,44,49,79,81,85,91,94,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,66,67,14,14,14,14,14,14,14,]),'MAIN':([0,],[22,]),'ExpressionList':([41,],[64,]),'Factor':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[8,8,8,8,8,8,8,8,8,8,8,56,57,58,59,8,8,8,8,8,8,8,76,8,8,8,8,8,]),'Identifier':([0,1,4,12,17,24,25,28,29,30,32,34,35,36,37,38,39,41,42,43,44,49,55,79,81,85,91,94,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'Expression':([0,1,4,12,17,24,25,28,29,30,32,38,39,41,44,49,79,81,85,91,94,],[19,23,26,31,40,46,47,50,51,52,54,60,61,65,68,71,86,87,89,93,95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> MAIN","S'",1,None,None,None),
  ('MAIN -> Expression','MAIN',1,'p_Main','parser.py',28),
  ('Factor -> NUMBER','Factor',1,'p_Factor','parser.py',32),
  ('Factor -> Identifier','Factor',1,'p_Factor','parser.py',33),
  ('Factor -> INFINITY','Factor',1,'p_Factor','parser.py',34),
  ('Factor -> LPAREN Expression RPAREN','Factor',3,'p_Factor','parser.py',35),
  ('Term -> Term TIMES Factor','Term',3,'p_Term','parser.py',43),
  ('Term -> Term DIVIDE Factor','Term',3,'p_Term','parser.py',44),
  ('Term -> Term MOD Factor','Term',3,'p_Term','parser.py',45),
  ('Term -> Term QUOTIENT Factor','Term',3,'p_Term','parser.py',46),
  ('Term -> Term CARET LBRACE Factor RBRACE','Term',5,'p_Term','parser.py',47),
  ('Term -> Factor','Term',1,'p_Term','parser.py',48),
  ('Expression -> Expression PLUS Term','Expression',3,'p_Expression_binop','parser.py',77),
  ('Expression -> Expression MINUS Term','Expression',3,'p_Expression_binop','parser.py',78),
  ('Expression -> Term','Expression',1,'p_Expression_binop','parser.py',79),
  ('Expression -> FRAC LBRACE Expression RBRACE LBRACE Expression RBRACE','Expression',7,'p_FractionalExpression','parser.py',95),
  ('Factor -> SQRT LBRACE Expression RBRACE','Factor',4,'p_FunctionExpression','parser.py',100),
  ('Factor -> LFLOOR Expression RFLOOR','Factor',3,'p_FunctionExpression','parser.py',102),
  ('Factor -> LCEIL Expression RCEIL','Factor',3,'p_FunctionExpression','parser.py',104),
  ('Factor -> PIPE Expression PIPE','Factor',3,'p_FunctionExpression','parser.py',106),
  ('Factor -> SIN LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',108),
  ('Factor -> COS LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',110),
  ('Factor -> TAN LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',112),
  ('Factor -> ATAN LPAREN Expression COMMA Expression RPAREN','Factor',6,'p_FunctionExpression','parser.py',114),
  ('Factor -> ATAN LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',115),
  ('Factor -> LOG LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',117),
  ('Factor -> LN LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',119),
  ('Factor -> EXP LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',121),
  ('Factor -> Identifier LPAREN ExpressionList RPAREN','Factor',4,'p_FunctionExpression','parser.py',123),
  ('Factor -> Identifier LPAREN RPAREN','Factor',3,'p_FunctionExpression','parser.py',125),
  ('Factor -> INTEGRAL UNDERLINE LBRACE Expression RBRACE CARET LBRACE Expression RBRACE Expression DIFFERENTIAL','Factor',11,'p_Integral','parser.py',177),
  ('Identifier -> ID','Identifier',1,'p_Identifier','parser.py',181),
  ('ExpressionList -> ExpressionList COMMA Expression','ExpressionList',3,'p_ExpessionList','parser.py',185),
  ('ExpressionList -> Expression','ExpressionList',1,'p_ExpessionList','parser.py',186),
]
