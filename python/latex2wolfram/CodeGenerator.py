from Utils import *
from Constants import *
from Expression import *
from Integral import *
from FunctionName import *
from BinaryOperator import *
from Identifier import *
from Infinity import *
from Number import *

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
        if not isinstance(node.function, str):
            function = node.function.generateCode(self)
        else:
            function = node.function

        res = function + BEGIN_ARGUMENT_LIST

        if node.expression1 != None:
            res += node.expression1.generateCode(self)

        if node.expression2 != None:
            res += COMMA+SPACE + node.expression2.generateCode(self)

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

    def generateCode_ExpressionWithArithmeticOperation(self, node):
        
        if node.op.operator == BinaryOperator.POW:
            expression2 = self._getGeneratedExpression(node.expression2)
        else:
            expression2 = node.expression2.generateCode(self)

        return node.expression1.generateCode(self) + SPACE + node.op.generateCode(self) + SPACE + expression2

    def generateCode_MinusExpression(self, node):
        return MINUS + node.expression.generateCode(self)

    def generateCode_IteratedExpression(self, node):
        if node.supExpression:
            supExpression = self._getValueFromNumericExpression(node.supExpression)

            if isinstance(supExpression, Identifier) or isinstance(supExpression, Number):
                supExpression = supExpression.generateCode(self)
            else:
                supExpression = BEGIN_ARGUMENT_LIST + supExpression.generateCode(self) + END_ARGUMENT_LIST

            res = str(node.op) + BEGIN_SET + node.indexingExpression.generateCode(self) + FROM_TO + supExpression + END_SET
        else:
            res = str(node.op) + BEGIN_SET + node.indexingExpression.generateCode(self) + END_SET

        res += node.expression.generateCode(self)

        return res

    def generateCode_ExpressionList(self, node):
        return (COMMA+SPACE).join(map(lambda el: el.generateCode(self), node.values))

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
            differential = D + POW + order + DIV + D + node.differential + POW + order
        else:
            differential = D + DIV + D + node.differential

        expression = node.expression.generateCode(self)

        if not isinstance(node.expression, ExpressionBetweenParenthesis) or \
            (isinstance(node.expression, Integral) and not expression.startswith(BEGIN_ARGUMENT_LIST)):

            expression = BEGIN_ARGUMENT_LIST + expression + END_ARGUMENT_LIST

        return differential + SPACE + expression

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

        else:

            if node.function == FunctionName.SQRT:
                function = SQRT

            elif node.function == FunctionName.FLOOR:
                function = FLOOR

            elif node.function == FunctionName.CEIL:
                function = CEIL

            elif node.function == FunctionName.ABS:
                function = ABS

            elif node.function == FunctionName.SIN:
                function = SIN

            elif node.function == FunctionName.COS:
                function = COS

            elif node.function == FunctionName.LOG:
                function = LOG

            elif node.function == FunctionName.LN:
                function = LN

            elif node.function == FunctionName.EXP:
                function = EXP

            elif node.function == FunctionName.TAN:
                function = TAN

            elif node.function == FunctionName.ATAN:
                function = ATAN

        return function

    # BinaryOperator
    def generateCode_BinaryOperator(self, node):
        operator = EMPTY_STRING

        if node.operator == BinaryOperator.PLUS:
            operator = PLUS

        elif node.operator == BinaryOperator.MINUS:
            operator = MINUS

        elif node.operator == BinaryOperator.TIMES:
            operator = TIMES

        elif node.operator == BinaryOperator.DIV:
            operator = DIV

        elif node.operator == BinaryOperator.MOD:
            operator = MOD

        elif node.operator == BinaryOperator.POW:
            operator = POW

        return operator

    # Number
    def generateCode_Number(self, node):
        return node.number

    # ID
    def generateCode_ID(self, node):
        return node.value

    # Infinity
    def generateCode_Infinity(self, node):
        return INFINITY
