
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIDleftNUMBERINFINITYleftINTEGRALDIFFERENTIALDPARTIALrightCOMMArightPIPErightLPARENRPARENrightLBRACERBRACELBRACKETRBRACKETFRACrightDOTSleftSUMPRODleftFACTORIALleftPLUSMINUSleftTIMESDIVIDEMODrightCARETleftLFLOORRFLOORLCEILRCEILSINCOSTANATANSQRTLNLOGEXPFRAC NUMBER PLUS MINUS TIMES DIVIDE LPAREN RPAREN LBRACKET RBRACKET LBRACE RBRACE LFLOOR RFLOOR LCEIL RCEIL SIN COS TAN ATAN SQRT LOG LN EXP MOD CARET COMMA ID PIPE INFINITY UNDERLINE INTEGRAL DIFFERENTIAL D PARTIAL SUM PROD IN DOTS EQ FACTORIALMAIN : ExpressionFactor : NUMBER\n            | ID\n            | INFINITY\n            | IteratedExpression\n            | Derivative\n            | Integral\n            | LPAREN Expression RPARENTerm : Term TIMES Factor\n          | Term DIVIDE Factor\n          | Term MOD Factor\n          | Term CARET LBRACE Expression RBRACE\n          | FactorExpression : Expression PLUS Term\n                  | Expression MINUS Term\n                  | TermFactor : NUMBER FACTORIAL\n              | ID FACTORIAL\n              | LPAREN Expression RPAREN FACTORIALFactor : FRAC LBRACE Expression RBRACE LBRACE Expression RBRACEFactor : SQRT LBRACE Expression RBRACE\n\n              | SQRT LBRACKET NUMBER RBRACKET LBRACE Expression RBRACE\n                         \n              | LFLOOR Expression RFLOOR\n                         \n              | LCEIL Expression RCEIL\n                         \n              | PIPE Expression PIPE\n                         \n              | SIN LPAREN Expression RPAREN\n                         \n              | COS LPAREN Expression RPAREN\n\n              | TAN LPAREN Expression RPAREN\n                         \n              | ATAN LPAREN Expression COMMA Expression RPAREN\n              | ATAN LPAREN Expression RPAREN\n                         \n              | LOG LPAREN Expression RPAREN\n                         \n              | LN LPAREN Expression RPAREN\n                         \n              | EXP LPAREN Expression RPAREN\n\n              | ID LPAREN ExpressionList RPAREN\n\n              | ID LPAREN RPARENRange : Expression DOTS ExpressionIndexingExpression : ID IN RangeIteratedExpression : SUM UNDERLINE LBRACE IndexingExpression RBRACE Expression\n                          | SUM UNDERLINE LBRACE ID EQ Expression RBRACE CARET LBRACE Expression RBRACE Expression\n                          | PROD UNDERLINE LBRACE IndexingExpression RBRACE Expression\n                          | PROD UNDERLINE LBRACE ID EQ Expression RBRACE CARET LBRACE Expression RBRACE ExpressionIntegral : INTEGRAL UNDERLINE LBRACE Expression RBRACE CARET LBRACE Expression RBRACE Expression DIFFERENTIAL\n                | INTEGRAL UNDERLINE LBRACE Expression RBRACE Expression DIFFERENTIAL\n                | INTEGRAL CARET LBRACE Expression RBRACE Expression DIFFERENTIAL\n                | INTEGRAL Expression DIFFERENTIALDerivative : FRAC LBRACE D RBRACE LBRACE DIFFERENTIAL RBRACE Expression\n                  | FRAC LBRACE D CARET LBRACE NUMBER RBRACE RBRACE LBRACE DIFFERENTIAL CARET LBRACE NUMBER RBRACE RBRACE ExpressionDerivative : FRAC LBRACE D Expression RBRACE LBRACE DIFFERENTIAL RBRACE\n                  | FRAC LBRACE D CARET LBRACE NUMBER RBRACE Expression RBRACE LBRACE DIFFERENTIAL CARET LBRACE NUMBER RBRACE RBRACEDerivative : FRAC LBRACE PARTIAL RBRACE LBRACE PARTIAL ID RBRACE Expression\n                  | FRAC LBRACE PARTIAL CARET LBRACE NUMBER RBRACE RBRACE LBRACE PARTIAL ID CARET LBRACE NUMBER RBRACE RBRACE ExpressionDerivative : FRAC LBRACE PARTIAL Expression RBRACE LBRACE PARTIAL ID RBRACE\n                  | FRAC LBRACE PARTIAL CARET LBRACE NUMBER RBRACE Expression RBRACE LBRACE PARTIAL ID CARET LBRACE NUMBER RBRACE RBRACEExpressionList : ExpressionList COMMA Expression\n                    | Expression'
    
_lr_action_items = {'LFLOOR':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]),'CARET':([7,8,10,11,17,18,22,23,24,36,51,55,59,63,65,67,70,73,74,75,77,78,79,80,85,86,93,101,102,103,105,107,108,110,118,126,133,135,146,148,150,151,153,157,161,168,169,181,182,186,192,194,195,197,198,202,215,216,219,220,],[33,-2,-13,-6,43,-4,-3,-5,-7,-17,-18,-23,-24,-45,94,98,-25,-10,-9,-11,-8,43,43,-35,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,137,-12,-40,-38,-29,162,164,-44,-43,-20,-22,-46,-48,-50,-52,193,-42,200,201,-41,-39,206,-47,-49,-51,-53,]),'COS':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'LOG':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'SUM':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'INTEGRAL':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'NUMBER':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,54,61,62,65,67,72,106,109,112,113,114,115,116,117,118,119,122,123,129,149,152,154,155,158,172,174,175,176,190,191,199,204,205,210,211,217,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,84,8,8,8,8,8,8,8,8,8,8,8,8,8,8,139,8,143,8,8,8,8,8,8,8,8,8,8,8,8,203,208,209,214,8,8,]),'RFLOOR':([8,10,11,17,18,22,23,24,27,36,51,55,59,63,70,73,74,75,77,78,79,80,85,86,93,101,102,103,105,107,108,110,126,133,135,146,151,153,157,161,168,169,181,182,192,197,198,215,216,219,220,],[-2,-13,-6,-16,-4,-3,-5,-7,55,-17,-18,-23,-24,-45,-25,-10,-9,-11,-8,-14,-15,-35,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,-12,-40,-38,-29,-44,-43,-20,-22,-46,-48,-50,-52,-42,-41,-39,-47,-49,-51,-53,]),'LBRACKET':([25,],[54,]),'EXP':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'INFINITY':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'RCEIL':([8,10,11,17,18,22,23,24,31,36,51,55,59,63,70,73,74,75,77,78,79,80,85,86,93,101,102,103,105,107,108,110,126,133,135,146,151,153,157,161,168,169,181,182,192,197,198,215,216,219,220,],[-2,-13,-6,-16,-4,-3,-5,-7,59,-17,-18,-23,-24,-45,-25,-10,-9,-11,-8,-14,-15,-35,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,-12,-40,-38,-29,-44,-43,-20,-22,-46,-48,-50,-52,-42,-41,-39,-47,-49,-51,-53,]),'SIN':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'RBRACE':([8,10,11,17,18,22,23,24,36,51,55,59,63,65,66,67,70,73,74,75,77,78,79,80,83,85,86,88,90,91,92,93,96,100,101,102,103,104,105,107,108,110,126,130,131,133,134,135,139,140,142,143,146,147,151,153,154,156,157,158,159,161,163,165,167,168,169,171,173,181,182,183,184,192,197,198,203,207,208,209,212,213,214,215,216,218,219,220,],[-2,-13,-6,-16,-4,-3,-5,-7,-17,-18,-23,-24,-45,95,97,99,-25,-10,-9,-11,-8,-14,-15,-35,110,-27,-31,114,116,117,118,-33,121,125,-32,-26,-28,126,-30,-19,-34,-21,-12,148,-37,-40,150,-38,154,155,157,158,-29,161,-44,-43,166,169,-20,170,172,-22,-36,176,178,-46,-48,180,182,-50,-52,190,191,-42,-41,-39,207,211,212,213,216,217,218,-47,-49,220,-51,-53,]),'RPAREN':([8,10,11,17,18,22,23,24,36,48,51,52,55,56,57,59,63,64,68,69,70,71,73,74,75,76,77,78,79,80,81,82,85,86,93,101,102,103,105,107,108,110,126,127,128,133,135,146,151,153,157,161,168,169,181,182,192,197,198,215,216,219,220,],[-2,-13,-6,-16,-4,-3,-5,-7,-17,77,-18,80,-23,85,86,-24,-45,93,101,102,-25,103,-10,-9,-11,105,-8,-14,-15,-35,108,-55,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,-12,146,-54,-40,-38,-29,-44,-43,-20,-22,-46,-48,-50,-52,-42,-41,-39,-47,-49,-51,-53,]),'LN':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'MINUS':([8,10,11,17,18,21,22,23,24,27,31,35,36,41,48,51,55,56,57,59,63,64,66,68,69,70,71,73,74,75,76,77,78,79,80,82,83,85,86,91,92,93,96,100,101,102,103,104,105,107,108,110,126,127,128,130,132,133,134,135,136,138,142,146,147,151,153,157,161,163,165,167,168,169,171,181,182,183,184,185,192,197,198,215,216,219,220,],[-2,-13,-6,-16,-4,50,-3,-5,-7,50,50,50,-17,50,50,-18,-23,50,50,-24,-45,50,50,50,50,-25,50,-10,-9,-11,50,-8,-14,-15,-35,50,50,-27,-31,50,50,-33,50,50,-32,-26,-28,50,-30,-19,-34,-21,-12,50,50,50,50,50,50,50,50,50,50,-29,50,-44,-43,-20,-22,50,50,50,50,-48,50,50,-52,50,50,50,-42,50,50,50,-49,50,-53,]),'PIPE':([0,1,5,7,8,10,11,15,17,18,20,22,23,24,28,29,36,37,38,39,40,41,42,44,45,46,47,49,50,51,52,53,55,59,61,62,63,65,67,70,72,73,74,75,77,78,79,80,85,86,93,101,102,103,105,106,107,108,109,110,112,113,114,115,116,117,118,122,126,129,133,135,146,149,151,152,153,154,155,157,158,161,168,169,172,174,175,176,181,182,190,191,192,197,198,211,215,216,217,219,220,],[15,15,15,15,-2,-13,-6,15,-16,-4,15,-3,-5,-7,15,15,-17,15,15,15,15,70,15,15,15,15,15,15,15,-18,15,15,-23,-24,15,15,-45,15,15,-25,15,-10,-9,-11,-8,-14,-15,-35,-27,-31,-33,-32,-26,-28,-30,15,-19,-34,15,-21,15,15,15,15,15,15,15,15,-12,15,-40,-38,-29,15,-44,15,-43,15,15,-20,15,-22,-46,-48,15,15,15,15,-50,-52,15,15,-42,-41,-39,15,-47,-49,15,-51,-53,]),'PLUS':([8,10,11,17,18,21,22,23,24,27,31,35,36,41,48,51,55,56,57,59,63,64,66,68,69,70,71,73,74,75,76,77,78,79,80,82,83,85,86,91,92,93,96,100,101,102,103,104,105,107,108,110,126,127,128,130,132,133,134,135,136,138,142,146,147,151,153,157,161,163,165,167,168,169,171,181,182,183,184,185,192,197,198,215,216,219,220,],[-2,-13,-6,-16,-4,49,-3,-5,-7,49,49,49,-17,49,49,-18,-23,49,49,-24,-45,49,49,49,49,-25,49,-10,-9,-11,49,-8,-14,-15,-35,49,49,-27,-31,49,49,-33,49,49,-32,-26,-28,49,-30,-19,-34,-21,-12,49,49,49,49,49,49,49,49,49,49,-29,49,-44,-43,-20,-22,49,49,49,49,-48,49,49,-52,49,49,49,-42,49,49,49,-49,49,-53,]),'COMMA':([8,10,11,17,18,22,23,24,36,51,55,59,63,70,73,74,75,76,77,78,79,80,81,82,85,86,93,101,102,103,105,107,108,110,126,128,133,135,146,151,153,157,161,168,169,181,182,192,197,198,215,216,219,220,],[-2,-13,-6,-16,-4,-3,-5,-7,-17,-18,-23,-24,-45,-25,-10,-9,-11,106,-8,-14,-15,-35,109,-55,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,-12,-54,-40,-38,-29,-44,-43,-20,-22,-46,-48,-50,-52,-42,-41,-39,-47,-49,-51,-53,]),'TAN':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'UNDERLINE':([4,6,7,],[30,32,34,]),'$end':([8,10,11,17,18,21,22,23,24,26,36,51,55,59,63,70,73,74,75,77,78,79,80,85,86,93,101,102,103,105,107,108,110,126,133,135,146,151,153,157,161,168,169,181,182,192,197,198,215,216,219,220,],[-2,-13,-6,-16,-4,-1,-3,-5,-7,0,-17,-18,-23,-24,-45,-25,-10,-9,-11,-8,-14,-15,-35,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,-12,-40,-38,-29,-44,-43,-20,-22,-46,-48,-50,-52,-42,-41,-39,-47,-49,-51,-53,]),'DOTS':([8,10,11,17,18,22,23,24,36,51,55,59,63,70,73,74,75,77,78,79,80,85,86,93,101,102,103,105,107,108,110,126,132,133,135,146,151,153,157,161,168,169,181,182,192,197,198,215,216,219,220,],[-2,-13,-6,-16,-4,-3,-5,-7,-17,-18,-23,-24,-45,-25,-10,-9,-11,-8,-14,-15,-35,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,-12,149,-40,-38,-29,-44,-43,-20,-22,-46,-48,-50,-52,-42,-41,-39,-47,-49,-51,-53,]),'LCEIL':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'FRAC':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'DIVIDE':([8,10,11,17,18,22,23,24,36,51,55,59,63,70,73,74,75,77,78,79,80,85,86,93,101,102,103,105,107,108,110,126,133,135,146,151,153,157,161,168,169,181,182,192,197,198,215,216,219,220,],[-2,-13,-6,44,-4,-3,-5,-7,-17,-18,-23,-24,-45,-25,-10,-9,-11,-8,44,44,-35,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,-12,-40,-38,-29,-44,-43,-20,-22,-46,-48,-50,-52,-42,-41,-39,-47,-49,-51,-53,]),'ATAN':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'D':([38,],[65,]),'TIMES':([8,10,11,17,18,22,23,24,36,51,55,59,63,70,73,74,75,77,78,79,80,85,86,93,101,102,103,105,107,108,110,126,133,135,146,151,153,157,161,168,169,181,182,192,197,198,215,216,219,220,],[-2,-13,-6,45,-4,-3,-5,-7,-17,-18,-23,-24,-45,-25,-10,-9,-11,-8,45,45,-35,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,-12,-40,-38,-29,-44,-43,-20,-22,-46,-48,-50,-52,-42,-41,-39,-47,-49,-51,-53,]),'LPAREN':([0,1,2,3,5,7,9,13,14,15,16,19,20,22,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[20,20,28,29,20,20,37,39,40,20,42,47,20,52,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'IN':([87,89,],[113,113,]),'EQ':([87,89,],[112,115,]),'ID':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,58,60,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,144,149,152,154,155,158,160,172,174,175,176,188,190,191,196,211,217,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,87,89,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,159,22,22,22,22,22,173,22,22,22,22,195,22,22,202,22,22,]),'LBRACE':([12,25,30,32,33,34,43,94,95,97,98,99,111,121,125,137,162,164,166,170,178,180,193,200,201,206,],[38,53,58,60,61,62,72,119,120,122,123,124,129,141,145,152,174,175,177,179,187,189,199,204,205,210,]),'PARTIAL':([38,124,145,179,189,],[67,144,160,188,196,]),'FACTORIAL':([8,22,77,],[36,51,107,]),'DIFFERENTIAL':([8,10,11,17,18,22,23,24,35,36,51,55,59,63,70,73,74,75,77,78,79,80,85,86,93,101,102,103,105,107,108,110,120,126,133,135,136,138,141,146,151,153,157,161,168,169,177,181,182,185,187,192,197,198,215,216,219,220,],[-2,-13,-6,-16,-4,-3,-5,-7,63,-17,-18,-23,-24,-45,-25,-10,-9,-11,-8,-14,-15,-35,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,140,-12,-40,-38,151,153,156,-29,-44,-43,-20,-22,-46,-48,186,-50,-52,192,194,-42,-41,-39,-47,-49,-51,-53,]),'SQRT':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'RBRACKET':([84,],[111,]),'PROD':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'MOD':([8,10,11,17,18,22,23,24,36,51,55,59,63,70,73,74,75,77,78,79,80,85,86,93,101,102,103,105,107,108,110,126,133,135,146,151,153,157,161,168,169,181,182,192,197,198,215,216,219,220,],[-2,-13,-6,46,-4,-3,-5,-7,-17,-18,-23,-24,-45,-25,-10,-9,-11,-8,46,46,-35,-27,-31,-33,-32,-26,-28,-30,-19,-34,-21,-12,-40,-38,-29,-44,-43,-20,-22,-46,-48,-50,-52,-42,-41,-39,-47,-49,-51,-53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Term':([0,1,5,7,15,20,28,29,37,38,39,40,42,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,78,79,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'IteratedExpression':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'Integral':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'Range':([113,],[131,]),'ExpressionList':([52,],[81,]),'Factor':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[10,10,10,10,10,10,10,10,10,10,10,10,10,73,74,75,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'IndexingExpression':([58,60,],[88,90,]),'Derivative':([0,1,5,7,15,20,28,29,37,38,39,40,42,44,45,46,47,49,50,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'MAIN':([0,],[26,]),'Expression':([0,1,5,7,15,20,28,29,37,38,39,40,42,47,52,53,61,62,65,67,72,106,109,112,113,114,115,116,117,118,122,129,149,152,154,155,158,172,174,175,176,190,191,211,217,],[21,27,31,35,41,48,56,57,64,66,68,69,71,76,82,83,91,92,96,100,104,127,128,130,132,133,134,135,136,138,142,147,163,165,167,168,171,181,183,184,185,197,198,215,219,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> MAIN","S'",1,None,None,None),
  ('MAIN -> Expression','MAIN',1,'p_Main','parser.py',38),
  ('Factor -> NUMBER','Factor',1,'p_Factor','parser.py',42),
  ('Factor -> ID','Factor',1,'p_Factor','parser.py',43),
  ('Factor -> INFINITY','Factor',1,'p_Factor','parser.py',44),
  ('Factor -> IteratedExpression','Factor',1,'p_Factor','parser.py',45),
  ('Factor -> Derivative','Factor',1,'p_Factor','parser.py',46),
  ('Factor -> Integral','Factor',1,'p_Factor','parser.py',47),
  ('Factor -> LPAREN Expression RPAREN','Factor',3,'p_Factor','parser.py',48),
  ('Term -> Term TIMES Factor','Term',3,'p_Term','parser.py',60),
  ('Term -> Term DIVIDE Factor','Term',3,'p_Term','parser.py',61),
  ('Term -> Term MOD Factor','Term',3,'p_Term','parser.py',62),
  ('Term -> Term CARET LBRACE Expression RBRACE','Term',5,'p_Term','parser.py',63),
  ('Term -> Factor','Term',1,'p_Term','parser.py',64),
  ('Expression -> Expression PLUS Term','Expression',3,'p_Expression_binop','parser.py',90),
  ('Expression -> Expression MINUS Term','Expression',3,'p_Expression_binop','parser.py',91),
  ('Expression -> Term','Expression',1,'p_Expression_binop','parser.py',92),
  ('Factor -> NUMBER FACTORIAL','Factor',2,'p_Factorial','parser.py',108),
  ('Factor -> ID FACTORIAL','Factor',2,'p_Factorial','parser.py',109),
  ('Factor -> LPAREN Expression RPAREN FACTORIAL','Factor',4,'p_Factorial','parser.py',110),
  ('Factor -> FRAC LBRACE Expression RBRACE LBRACE Expression RBRACE','Factor',7,'p_FractionalExpression','parser.py',114),
  ('Factor -> SQRT LBRACE Expression RBRACE','Factor',4,'p_FunctionExpression','parser.py',119),
  ('Factor -> SQRT LBRACKET NUMBER RBRACKET LBRACE Expression RBRACE','Factor',7,'p_FunctionExpression','parser.py',121),
  ('Factor -> LFLOOR Expression RFLOOR','Factor',3,'p_FunctionExpression','parser.py',123),
  ('Factor -> LCEIL Expression RCEIL','Factor',3,'p_FunctionExpression','parser.py',125),
  ('Factor -> PIPE Expression PIPE','Factor',3,'p_FunctionExpression','parser.py',127),
  ('Factor -> SIN LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',129),
  ('Factor -> COS LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',131),
  ('Factor -> TAN LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',133),
  ('Factor -> ATAN LPAREN Expression COMMA Expression RPAREN','Factor',6,'p_FunctionExpression','parser.py',135),
  ('Factor -> ATAN LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',136),
  ('Factor -> LOG LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',138),
  ('Factor -> LN LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',140),
  ('Factor -> EXP LPAREN Expression RPAREN','Factor',4,'p_FunctionExpression','parser.py',142),
  ('Factor -> ID LPAREN ExpressionList RPAREN','Factor',4,'p_FunctionExpression','parser.py',144),
  ('Factor -> ID LPAREN RPAREN','Factor',3,'p_FunctionExpression','parser.py',146),
  ('Range -> Expression DOTS Expression','Range',3,'p_Range','parser.py',202),
  ('IndexingExpression -> ID IN Range','IndexingExpression',3,'p_IndexingExpression','parser.py',206),
  ('IteratedExpression -> SUM UNDERLINE LBRACE IndexingExpression RBRACE Expression','IteratedExpression',6,'p_IteratedExpression','parser.py',210),
  ('IteratedExpression -> SUM UNDERLINE LBRACE ID EQ Expression RBRACE CARET LBRACE Expression RBRACE Expression','IteratedExpression',12,'p_IteratedExpression','parser.py',211),
  ('IteratedExpression -> PROD UNDERLINE LBRACE IndexingExpression RBRACE Expression','IteratedExpression',6,'p_IteratedExpression','parser.py',212),
  ('IteratedExpression -> PROD UNDERLINE LBRACE ID EQ Expression RBRACE CARET LBRACE Expression RBRACE Expression','IteratedExpression',12,'p_IteratedExpression','parser.py',213),
  ('Integral -> INTEGRAL UNDERLINE LBRACE Expression RBRACE CARET LBRACE Expression RBRACE Expression DIFFERENTIAL','Integral',11,'p_Integral','parser.py',230),
  ('Integral -> INTEGRAL UNDERLINE LBRACE Expression RBRACE Expression DIFFERENTIAL','Integral',7,'p_Integral','parser.py',231),
  ('Integral -> INTEGRAL CARET LBRACE Expression RBRACE Expression DIFFERENTIAL','Integral',7,'p_Integral','parser.py',232),
  ('Integral -> INTEGRAL Expression DIFFERENTIAL','Integral',3,'p_Integral','parser.py',233),
  ('Derivative -> FRAC LBRACE D RBRACE LBRACE DIFFERENTIAL RBRACE Expression','Derivative',8,'p_Derivative1','parser.py',250),
  ('Derivative -> FRAC LBRACE D CARET LBRACE NUMBER RBRACE RBRACE LBRACE DIFFERENTIAL CARET LBRACE NUMBER RBRACE RBRACE Expression','Derivative',16,'p_Derivative1','parser.py',251),
  ('Derivative -> FRAC LBRACE D Expression RBRACE LBRACE DIFFERENTIAL RBRACE','Derivative',8,'p_Derivative2','parser.py',260),
  ('Derivative -> FRAC LBRACE D CARET LBRACE NUMBER RBRACE Expression RBRACE LBRACE DIFFERENTIAL CARET LBRACE NUMBER RBRACE RBRACE','Derivative',16,'p_Derivative2','parser.py',261),
  ('Derivative -> FRAC LBRACE PARTIAL RBRACE LBRACE PARTIAL ID RBRACE Expression','Derivative',9,'p_Derivative3','parser.py',270),
  ('Derivative -> FRAC LBRACE PARTIAL CARET LBRACE NUMBER RBRACE RBRACE LBRACE PARTIAL ID CARET LBRACE NUMBER RBRACE RBRACE Expression','Derivative',17,'p_Derivative3','parser.py',271),
  ('Derivative -> FRAC LBRACE PARTIAL Expression RBRACE LBRACE PARTIAL ID RBRACE','Derivative',9,'p_Derivative4','parser.py',280),
  ('Derivative -> FRAC LBRACE PARTIAL CARET LBRACE NUMBER RBRACE Expression RBRACE LBRACE PARTIAL ID CARET LBRACE NUMBER RBRACE RBRACE','Derivative',17,'p_Derivative4','parser.py',281),
  ('ExpressionList -> ExpressionList COMMA Expression','ExpressionList',3,'p_ExpessionList','parser.py',291),
  ('ExpressionList -> Expression','ExpressionList',1,'p_ExpessionList','parser.py',292),
]
