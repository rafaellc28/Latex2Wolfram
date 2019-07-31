from BaseExpression import *

class Constraint(BaseExpression):
    """
    Class representing a constraint node in the AST
    """

    def __init__(self, op, expression1, expression2):
        """
        Set the expression and the function

        :param op          : ConstraintOperator
        :param expression1 : Expression
        :param expression2 : Expression
        """
        BaseExpression.__init__(self)

        self.op = op
        self.expression1 = expression1
        self.expression2 = expression2

    def __str__(self):
        """
        to string
        """
        return str(self.expression1) + " " + str(self.op) + " " + str(self.expression2)

    def getDependencies(self, codeGenerator):
        return list(set(self.expression1.getDependencies(codeGenerator) + self.expression2.getDependencies(codeGenerator)))

    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this constraint
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this constraint
        """
        return codeGenerator.generateCode(self)
