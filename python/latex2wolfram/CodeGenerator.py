from Utils import *
from Constants import *
from Expression import *
from FunctionName import *
from BinaryOperator import *
from Identifier import *
from Infinity import *

class CodeGenerator:
    """ Visitor in the Visitor Pattern """
    
    def generateCode(self, node):
        cls = node.__class__
        method_name = 'generateCode_' + cls.__name__
        method = getattr(self, method_name, None)

        if method:
            return method(node)

    def generateCode_Main(self, node):
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
        
        numerator = node.numerator
        if isinstance(node.numerator, ValuedExpression):
            numerator = numerator.value
            
        if not isinstance(numerator, Identifier) and not isinstance(numerator, Number) and not isinstance(numerator, ExpressionWithFunction):
            numerator = BEGIN_ARGUMENT_LIST+numerator.generateCode(self)+END_ARGUMENT_LIST
        else:
            numerator = numerator.generateCode(self)
            
        denominator = node.denominator
        if isinstance(denominator, ValuedExpression):
            denominator = denominator.value
            
        if not isinstance(denominator, Identifier) and not isinstance(denominator, Number) and not isinstance(denominator, ExpressionWithFunction):
            denominator = BEGIN_ARGUMENT_LIST+denominator.generateCode(self)+END_ARGUMENT_LIST
        else:
            denominator = denominator.generateCode(self)
            
        return numerator+DIV+denominator

    def generateCode_ValuedExpression(self, node):
        return node.value.generateCode(self)

    def generateCode_ExpressionBetweenParenthesis(self, node):
        return BEGIN_ARGUMENT_LIST + node.expression.generateCode(self) + END_ARGUMENT_LIST

    def generateCode_ExpressionWithArithmeticOperation(self, node):
        return node.expression1.generateCode(self) + SPACE + node.op.generateCode(self) + SPACE + node.expression2.generateCode(self)

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

        return INTEGRATE + SPACE + node.integrand.generateCode(self) + SPACE + D + d + limits

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
