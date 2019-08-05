from BaseExpression import *
from FunctionName import *

class Expression(BaseExpression):
    """
    Class representing a expression node in the AST
    """
    def __init__(self):
        BaseExpression.__init__(self)

class ExpressionWithFunction(Expression):
    """
    Class representing a expression with function node in the AST
    """

    def __init__(self, function, expression1 = None, expression2 = None):
        """
        Set the expression and the function

        :param function    : FunctionName
        :param expression1 : Expression
        :param expression2 : Expression
        """

        Expression.__init__(self)

        self.function = function
        self.expression1 = expression1
        self.expression2 = expression2

    def __str__(self):
        """
        to string
        """
        res = str(self.function)

        if (self.function == FunctionName.SQRT or self.function == FunctionName.LOG) and self.expression2 != None:
            res += "["+str(self.expression2)+"]"

        res += "("

        if self.expression1 != None:
            res += str(self.expression1)

        if self.expression2 != None and self.function != FunctionName.SQRT:
            res += ", " + str(self.expression2)

        res += ")"
        
        return res

    def getDependencies(self, codeGenerator):
        dep = []

        if self.expression1 != None:
            dep += self.expression1.getDependencies(codeGenerator)

        if self.expression2 != None:
            dep += self.expression2.getDependencies(codeGenerator)

        return list(set(dep))

    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this expression with function
        """
        return codeGenerator.generateCode(self)

class FractionalExpression(Expression):
    """
    Class representing a fractional expression node in the AST
    """

    def __init__(self, numerator, denominator):
        """
        Set the single value of this expression

        :param numerator   : Identifier | Expression
        :param denominator : Identifier | Expression
        """

        Expression.__init__(self)

        self.numerator   = numerator
        self.denominator = denominator

    def __str__(self):
        """
        to string
        """
        return "FractionalExpression: " + str(self.numerator) + "/"+str(self.denominator)

    def __len__(self):
        """
        length method
        """

        return 1

    def __iter__(self):
        """
        Get the iterator of the class
        """

        return [self]

    def getDependencies(self, codeGenerator):
        dep = []

        if self.numerator != None:
            dep += self.numerator.getDependencies(codeGenerator)

        if self.denominator != None:
            dep += self.denominator.getDependencies(codeGenerator)

        return list(set(dep))

    def setupEnvironment(self, codeSetup):
        """
        Generate the AMPL code for the identifiers and sets used in this fractional expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the AMPL code for this fractional expression
        """
        return codeGenerator.generateCode(self)

class ExpressionBetweenParenthesis(Expression):
    """
    Class representing a expression between parenthesis node in the AST
    """

    def __init__(self, expression):
        """
        Set the expression

        :param expression : Expression
        """

        Expression.__init__(self)

        self.expression = expression

    def __str__(self):
        """
        to string
        """
        
        return "ExpressionBetweenParenthesis: (" + str(self.expression) + ")"

    def getDependencies(self, codeGenerator):
        return self.expression.getDependencies(codeGenerator)
    
    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this expression
        """
        return codeGenerator.generateCode(self)


class ExpressionWithBinaryOperation(Expression):
    """
    Class representing a expression with arithmetic operation node in the AST
    """
    
    def __init__(self, op, expression1, expression2):
        """
        Set the expressions participating in the arithmetic operation
        
        :param op          : BinaryOperator
        :param expression1 : Expression
        :param expression2 : Expression
        """

        Expression.__init__(self)
        
        self.op          = op
        self.expression1 = expression1
        self.expression2 = expression2
    
    def __str__(self):
        """
        to string
        """
        return "ExpressionWithBinaryOperation:" + str(self.expression1) + " " + str(self.op) + " " + str(self.expression2)

    def getDependencies(self, codeGenerator):
        return list(set(self.expression1.getDependencies(codeGenerator) + self.expression2.getDependencies(codeGenerator)))

    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this expression with arithmetic operation
        """
        return codeGenerator.generateCode(self)

class ExpressionWithUnaryOperation(Expression):
    """
    Class representing a expression with unary operation node in the AST
    """
    
    def __init__(self, op, expression, afterExpression = False):
        """
        Set the expressions participating in the arithmetic operation
        
        :param op         : UnaryOperator
        :param expression : Expression
        :param afterExpression : Bool
        """

        Expression.__init__(self)
        
        self.op          = op
        self.expression = expression
        self.afterExpression = afterExpression
    
    def __str__(self):
        """
        to string
        """
        if self.afterExpression:
            code = str(self.expression) + str(self.op)
        else:
            code = str(self.op)+str(self.expression)

        return "ExpressionWithUnaryOperation: " + code

    def getDependencies(self, codeGenerator):
        return self.expression.getDependencies(codeGenerator)

    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this expression with unary operation
        """
        return codeGenerator.generateCode(self)


class MinusExpression(Expression):
    """
    Class representing a minus expression node in the AST
    """
    
    def __init__(self, expression):
        """
        Set the expression being negated
        
        :param expression: Expression
        """

        Expression.__init__(self)
        
        self.expression = expression
    
    def __str__(self):
        """
        to string
        """
        
        return "MinusExpression:" + "-(" + str(self.expression) + ")"

    def getDependencies(self, codeGenerator):
        return self.expression.getDependencies(codeGenerator)

    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this minus expression
        """
        return codeGenerator.generateCode(self)


class IteratedExpression(Expression):
    """
    Class representing a iterated expression node in the AST
    """

    def __init__(self, op, expression, indexingExpression, supExpression = None):
        """
        Set the components of the iterated linear expression

        :param op                 : op
        :param expression         : Expression
        :param indexingExpression : IndexingExpression
        :param supExpression      : Expression
        """

        Expression.__init__(self)
        
        self.op                   = op
        self.expression    = expression
        self.indexingExpression   = indexingExpression
        self.supExpression = supExpression

    def __str__(self):
        """
        to string
        """
        
        res = str(self.op) + "(" + str(self.indexingExpression) + ")"

        if self.supExpression:
            res += "^" + str(self.supExpression)

        res += str(self.expression)

        return "IteratedExpression:" + res + "|"

    def getDependencies(self, codeGenerator):
        dep = self.expression.getDependencies(codeGenerator) + self.indexingExpression.getDependencies(codeGenerator)

        if self.supExpression != None:
            dep += self.supExpression.getDependencies(codeGenerator)

        return list(set(dep))
    
    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this iterated expression
        """
        return codeGenerator.generateCode(self)

class ConditionalExpression(Expression):
    """
    Class representing a conditional expression node in the AST of a MLP
    """
    
    def __init__(self, logicalExpression, expression1, expression2 = None):
        """
        Set the conditional expression
        
        :param logicalExpression : LogicalExpression
        :param expression1: Expression
        :param expression2: Expression
        """

        Expression.__init__(self)
        
        self.logicalExpression  = logicalExpression
        self.expression1 = expression1
        self.expression2 = expression2
    
    def __str__(self):
        """
        to string
        """
        res = "ConditionalExpression: " + "("+str(self.logicalExpression)+")?" + str(self.expression1)

        if self.expression2 != None:
            res += ": " + str(self.expression2)

        return res

    def addElseExpression(self, elseExpression):
        self.expression2 = elseExpression
    
    def getDependencies(self, codeGenerator):
        dep = self.logicalExpression.getDependencies(codeGenerator) + self.expression1.getDependencies(codeGenerator)

        if self.expression2 != None:
            dep += self.expression2.getDependencies(codeGenerator)

        return list(set(dep))

    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this conditional expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this conditional expression
        """
        return codeGenerator.generateCode(self)

class ExpressionList(Expression):
    """
    Class representing a expression list node in the AST
    """
    
    def __init__(self, values = []):
        """
        Set the expression list
        
        :param values : [Expression]
        """

        Expression.__init__(self)
        
        self.values  = values
    
    def __str__(self):
        """
        to string
        """
        return "ExpressionList: " + "("+", ".join(map(lambda el: str(el), self.values))+")"

    def getDependencies(self, codeGenerator):
        return self.values.getDependencies(codeGenerator)

    def add(self, value):
        self.values.append(value)

    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this conditional expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this conditional expression
        """
        return codeGenerator.generateCode(self)
