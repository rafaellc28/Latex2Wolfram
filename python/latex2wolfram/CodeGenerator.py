from Utils import *
from Constants import *
from Expression import *

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
        res = node.expression1.generateCode(self) + SPACE + node.op + SPACE

        if node.op == ExpressionWithArithmeticOperation.POW and not (isinstance(node.expression2, ValuedExpression) or isinstance(node.expression2, ExpressionBetweenParenthesis)):
            res += BEGIN_ARGUMENT_LIST + node.expression2.generateCode(self) + END_ARGUMENT_LIST
        else:
            res += node.expression2.generateCode(self)

        return res

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

    # Value
    def generateCode_Value(self, node):
        return node.value.generateCode(self)

    # Identifier
    def generateCode_Identifier(self, node):
        return node.identifier.generateCode(self)

    # Number
    def generateCode_Number(self, node):
        return node.number

    # ID
    def generateCode_ID(self, node):
        return node.value
