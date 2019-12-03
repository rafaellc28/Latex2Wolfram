from Utils import *
from Constants import *
from Expression import *
from Integral import *
from Limit import *
from FunctionName import *
from UnaryOperator import *
from BinaryOperator import *
from IteratedOperator import *
from ConstraintOperator import *
from Identifier import *
from Infinity import *
from Number import *
from Symbol import *

class CodeGenerator:
    """ Visitor in the Visitor Pattern """
    
    def __init__(self):
        self.isIntegralExpression = False

    def generateCode(self, node):
        cls = node.__class__
        method_name = 'generateCode_' + cls.__name__
        method = getattr(self, method_name, None)

        if method:
            return method(node)

    def _getGeneratedExpression(self, expression):
        generatedExpression = expression.generateCode(self)

        if not isinstance(expression, Identifier) and not isinstance(expression, Number) and not isinstance(expression, Infinity) and \
           not isinstance(expression, ExpressionWithFunction) and not isinstance(expression, ExpressionBetweenParenthesis):

            generatedExpression = BEGIN_ARGUMENT_LIST + generatedExpression + END_ARGUMENT_LIST

        return generatedExpression

    def generateCode_Main(self, node):
        if isinstance(node.problem, Integral) or (isinstance(node.problem, ExpressionBetweenParenthesis) and isinstance(node.problem.expression, Integral)):
            self.isIntegralExpression = True

        return node.problem.generateCode(self)

    # Expression
    def generateCode_ExpressionWithFunction(self, node):

        if isinstance(node.function, Symbol) and node.function.symbol == Symbol.SIGMA_LOWER and node.expression2 != None:
            function = node.function.generateCode(self) + UNDERLINE + node.expression2.generateCode(self)

        elif not isinstance(node.function, str):
            function = node.function.generateCode(self)

        else:
            function = node.function

        if function == FunctionName.SQRT and node.expression2 != None:
            res = BEGIN_ARGUMENT_LIST + node.expression2.generateCode(self) + TH + SPACE + ROOTOF

        else:
            res = function

        if function == FunctionName.LOG and node.expression2 != None:
            res += node.expression2.generateCode(self)

        res += BEGIN_ARGUMENT_LIST

        if node.expression1 != None:
            res += node.expression1.generateCode(self)

        if node.expression2 != None and function != FunctionName.SQRT and function != FunctionName.LOG and \
            not (function.startswith(SIGMA) and node.expression2 != None):
            res += COMMA+SPACE + node.expression2.generateCode(self)

        res += END_ARGUMENT_LIST

        if function == FunctionName.SQRT and node.expression2 != None:
            res += END_ARGUMENT_LIST

        return res

    def generateCode_FractionalExpression(self, node):
        
        numerator = self._getGeneratedExpression(node.numerator)
        denominator = self._getGeneratedExpression(node.denominator)
            
        return numerator+DIV+denominator

    def generateCode_ExpressionBetweenParenthesis(self, node):
        isIntegralExpression = self.isIntegralExpression
        
        if isinstance(node.expression, Integral):
            self.isIntegralExpression = True

        expression = BEGIN_ARGUMENT_LIST + node.expression.generateCode(self) + END_ARGUMENT_LIST

        self.isIntegralExpression = isIntegralExpression

        return expression

    def generateCode_ExpressionWithBinaryOperation(self, node):
        
        if node.op.operator == BinaryOperator.POW:
            exponent = node.expression2.generateCode(self)

            if exponent.upper() in ["T", "(T)"] and isinstance(node.expression1, ExpressionsRow):
                return BEGIN_EXPRESSION + TRANSPOSE + SPACE + node.expression1.generateCode(self) + END_EXPRESSION

            expression2 = self._getGeneratedExpression(node.expression2)
        else:
            expression2 = node.expression2.generateCode(self)

        return node.expression1.generateCode(self) + SPACE + node.op.generateCode(self) + SPACE + expression2

    def generateCode_ExpressionWithUnaryOperation(self, node):
        
        if node.afterExpression:
            expression = node.expression.generateCode(self) + node.op.generateCode(self)
        else:
            expression = node.op.generateCode(self) + node.expression.generateCode(self)

        return expression

    def generateCode_IteratedExpression(self, node):
        res = BEGIN_ARGUMENT_LIST + node.op.generateCode(self) + BEGIN_ARGUMENT_LIST + node.expression.generateCode(self) + \
            END_ARGUMENT_LIST + COMMA + SPACE + FROM + SPACE + node.indexingExpression.identifier.generateCode(self) + EQUAL +\
            node.indexingExpression.range.lowerBound.generateCode(self) + SPACE + TO + SPACE + \
            node.indexingExpression.range.upperBound.generateCode(self) + END_ARGUMENT_LIST

        return res

    def generateCode_ExpressionList(self, node):
        return (COMMA+SPACE).join(map(lambda el: el.generateCode(self), node.values))

    # Constraint
    def generateCode_Constraint(self, node):
        return node.expression1.generateCode(self) + SPACE + node.op.generateCode(self) + SPACE + node.expression2.generateCode(self)

    def generateCode_Constraints(self, node):
        return (COMMA+SPACE).join(map(lambda el: el.generateCode(self), node.values))

    # Matrix
    def generateCode_ExpressionsRow(self, node):
        return BEGIN_VECTOR + (COMMA+SPACE).join(map(lambda el: el.generateCode(self), node.values)) + END_VECTOR

    # Integral
    def generateCode_Integral(self, node):

        d = node.differential
        limits = EMPTY_STRING

        if node.lowerBound and node.upperBound:
            limits += SPACE + FROM + SPACE + d + EQUAL + node.lowerBound.generateCode(self) + SPACE + TO + SPACE + node.upperBound.generateCode(self)

        elif node.lowerBound and not node.upperBound:
            limits += SPACE + FROM + SPACE + d + EQUAL + node.lowerBound.generateCode(self) + SPACE + TO + SPACE + Infinity().generateCode(self)

        elif not node.lowerBound and node.upperBound:
            limits += SPACE + FROM + SPACE + d + EQUAL + MINUS + Infinity().generateCode(self) + SPACE + TO + SPACE + node.upperBound.generateCode(self)

        integrand = node.integrand.generateCode(self)
        
        if isinstance(node.integrand, Integral) and not integrand.startswith(BEGIN_ARGUMENT_LIST):
            integrand = BEGIN_ARGUMENT_LIST + integrand + END_ARGUMENT_LIST
        
        integralExpression = INTEGRATE + SPACE + integrand + SPACE + D + d + limits

        if not self.isIntegralExpression and (node.lowerBound or node.upperBound):
            integralExpression = BEGIN_ARGUMENT_LIST + integralExpression + END_ARGUMENT_LIST

        return integralExpression

    # Derivative
    def generateCode_Derivative(self, node):

        if node.order:
            order = node.order.generateCode(self)
            differential = D + POW + order + DIV + D + node.differential[:1] + POW + order
        else:
            differential = D + DIV + D + node.differential[:1]

        expression = node.expression.generateCode(self)

        if not isinstance(node.expression, ExpressionBetweenParenthesis) or \
            (isinstance(node.expression, Integral) and not expression.startswith(BEGIN_ARGUMENT_LIST)):

            expression = BEGIN_ARGUMENT_LIST + expression + END_ARGUMENT_LIST

        return differential + SPACE + expression

    # Imaginary Number
    def generateCode_ImaginaryNumber(self, node):
        res = I

        if node.number:
            res = node.number.generateCode(self) + res
            
        return res

    # Napier Number
    def generateCode_NapierNumber(self, node):
        res = E

        if node.number:
            res = node.number.generateCode(self) + res
            
        return res

    # Limit
    def generateCode_Limit(self, node):

        res = LIMIT + SPACE + node.expression.generateCode(self) + SPACE + AS + SPACE + node.variable.generateCode(self) + SPACE + \
                APPROACHES + SPACE + node.to.generateCode(self)

        if node.approachesFrom == Limit.FROM_LEFT:
            res += MINUS

        elif node.approachesFrom == Limit.FROM_RIGHT:
            res += PLUS

        return res

    # Differential Variable
    def generateCode_DifferentialVariable(self, node):

        res = node.identifier.generateCode(self) + EMPTY_STRING.join(map(lambda el: el.generateCode(self), node.primeList))

        if node.argumentList:
            res += BEGIN_ARGUMENT_LIST + node.argumentList.generateCode(self) + END_ARGUMENT_LIST

        return res

    # Choose Expression
    def generateCode_ChooseExpression(self, node):

        return BEGIN_ARGUMENT_LIST + self._getGeneratedExpression(node.expression1) + SPACE + CHOOSE + SPACE + \
            node.expression2.generateCode(self) + END_ARGUMENT_LIST

    # Value
    def generateCode_Value(self, node):
        return node.value.generateCode(self)

    # Identifier
    def generateCode_Identifier(self, node):
        return node.identifier.generateCode(self)

    # FunctionName
    def generateCode_FunctionName(self, node):
        function = EMPTY_STRING

        if isinstance(node.function, Identifier):
            function = node.function.generateCode(self)

            if function == ADJ:
                function = ADJUGATE

            elif function == LU:
                function = LU_DECOMPOSITION_OF

            elif function.upper() == HESSENBERG:
                function = HESSENBERG_DECOMPOSITION

        else:
            
            if node.function == FunctionName.SQRT:
                function = SQRT

            elif node.function == FunctionName.FLOOR:
                function = FLOOR

            elif node.function == FunctionName.CEIL:
                function = CEIL

            elif node.function == FunctionName.ABS:
                function = ABS

            elif node.function == FunctionName.ASINH:
                function = ASINH

            elif node.function == FunctionName.SINH:
                function = SINH

            elif node.function == FunctionName.ASIN:
                function = ASIN

            elif node.function == FunctionName.SIN:
                function = SIN

            elif node.function == FunctionName.ACOSH:
                function = ACOSH

            elif node.function == FunctionName.COSH:
                function = COSH

            elif node.function == FunctionName.ACOS:
                function = ACOS

            elif node.function == FunctionName.COS:
                function = COS

            elif node.function == FunctionName.ATANH:
                function = ATANH

            elif node.function == FunctionName.TANH:
                function = TANH

            elif node.function == FunctionName.ATAN:
                function = ATAN

            elif node.function == FunctionName.TAN:
                function = TAN

            elif node.function == FunctionName.ASEC:
                function = ASEC

            elif node.function == FunctionName.SEC:
                function = SEC

            elif node.function == FunctionName.ACSC:
                function = ACSC

            elif node.function == FunctionName.CSC:
                function = CSC

            elif node.function == FunctionName.ACOTH:
                function = ACOTH

            elif node.function == FunctionName.COTH:
                function = COTH

            elif node.function == FunctionName.ACOT:
                function = ACOT

            elif node.function == FunctionName.COT:
                function = COT

            elif node.function == FunctionName.LOG:
                function = LOG

            elif node.function == FunctionName.LN:
                function = LN

            elif node.function == FunctionName.EXP:
                function = EXP

            elif node.function == FunctionName.GCD:
                function = GCD

            elif node.function == FunctionName.DEG:
                function = DEGREE

            elif node.function == FunctionName.GRAD:
                function = GRADIENT

            elif node.function == FunctionName.LAPL:
                function = LAPLACIAN

            elif node.function == FunctionName.DIV:
                function = DIVERGENCE

            elif node.function == FunctionName.CURL:
                function = CURL

            elif node.function == FunctionName.DET:
                function = DETERMINANT

            elif node.function == FunctionName.NORM:
                function = NORM

        return function

    # UnaryOperator
    def generateCode_UnaryOperator(self, node):
        operator = EMPTY_STRING

        if node.operator == UnaryOperator.PLUS:
            operator = PLUS

        elif node.operator == UnaryOperator.MINUS:
            operator = MINUS

        elif node.operator == UnaryOperator.FACTORIAL:
            operator = FACTORIAL

        elif node.operator == UnaryOperator.PERCENT:
            operator = PERCENT

        return operator

    # BinaryOperator
    def generateCode_BinaryOperator(self, node):
        operator = EMPTY_STRING

        if node.operator == BinaryOperator.PLUS:
            operator = PLUS

        elif node.operator == BinaryOperator.MINUS:
            operator = MINUS

        elif node.operator == BinaryOperator.TIMES:
            operator = TIMES

        elif node.operator == BinaryOperator.DOT:
            operator = DOT

        elif node.operator == BinaryOperator.CROSS:
            operator = CROSS

        elif node.operator == BinaryOperator.DIV:
            operator = DIV

        elif node.operator == BinaryOperator.MOD:
            operator = MOD

        elif node.operator == BinaryOperator.POW:
            operator = POW

        return operator

    # IteratedOperator
    def generateCode_IteratedOperator(self, node):
        operator = EMPTY_STRING

        if node.operator == IteratedOperator.SUM:
            operator = SUM

        elif node.operator == IteratedOperator.PROD:
            operator = PROD

        elif node.operator == IteratedOperator.MAX:
            operator = MAX

        elif node.operator == IteratedOperator.MIN:
            operator = MIN

        return operator

    # ConstraintOperator
    def generateCode_ConstraintOperator(self, node):
        operator = EMPTY_STRING

        if node.operator == ConstraintOperator.EQ:
            operator = EQUAL

        elif node.operator == ConstraintOperator.NEQ:
            operator = UNEQUAL

        elif node.operator == ConstraintOperator.LT:
            operator = LT

        elif node.operator == ConstraintOperator.LE:
            operator = LE

        elif node.operator == ConstraintOperator.GT:
            operator = GT

        elif node.operator == ConstraintOperator.GE:
            operator = GE

        return operator

    # Symbol
    def generateCode_Symbol(self, node):
        symbol = EMPTY_STRING

        if node.symbol == Symbol.PI:
            symbol = PI

        elif node.symbol == Symbol.PRIME:
            symbol = PRIME

        elif node.symbol == Symbol.ALPHA_LOWER:
            symbol = ALPHA

        elif node.symbol == Symbol.XI_LOWER:
            symbol = XI

        elif node.symbol == Symbol.PHI_LOWER:
            symbol = EULER_PHI

        elif node.symbol == Symbol.SIGMA_LOWER:
            symbol = SIGMA

        elif node.symbol == Symbol.ZETA_LOWER:
            symbol = ZETA

        elif node.symbol == Symbol.ETA_LOWER:
            symbol = ETA

        elif node.symbol == Symbol.DELTA_LOWER:
            symbol = DELTA

        elif node.symbol == Symbol.THETA_LOWER:
            symbol = THETA

        elif node.symbol == Symbol.LAMBDA_LOWER:
            symbol = LAMBDA

        elif node.symbol == Symbol.EPSILON_LOWER:
            symbol = EPSILON

        elif node.symbol == Symbol.TAU_LOWER:
            symbol = TAU

        elif node.symbol == Symbol.KAPPA_LOWER:
            symbol = KAPPA

        elif node.symbol == Symbol.OMEGA_LOWER:
            symbol = OMEGA

        elif node.symbol == Symbol.MU:
            symbol = MU

        elif node.symbol == Symbol.BETA:
            symbol = BETA

        elif node.symbol == Symbol.GAMMA:
            symbol = GAMMA

        elif node.symbol == Symbol.PSI_LOWER:
            symbol = DIGAMMA
            
        return symbol

    # Number
    def generateCode_Number(self, node):
        return node.number

    # ID
    def generateCode_ID(self, node):
        return node.value

    # Infinity
    def generateCode_Infinity(self, node):
        return INFINITY
