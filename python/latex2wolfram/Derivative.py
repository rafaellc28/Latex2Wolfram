from BaseExpression import *

class Derivative(BaseExpression):
    """
    Class representing an derivative in the AST
    """

    def __init__(self, differential, expression, order = None):
        """
        Set the expression

        :param differential : [a-zA-Z]
        :param expression   : Expression
        :param order        : Number
        """

        BaseExpression.__init__(self)

        self.differential = differential
        self.expression   = expression
        self.order        = order

    def __str__(self):
        """
        to string
        """
        if self.order:
            differential = "d^" + str(self.order) + "/d" + str(self.differential) + "^" + str(self.order)
        else:
            differential = "d" + str(self.order) + "/d" + str(self.differential)

        return "Derivative: " + differential + "(" + str(self.expression) + ")"

    def getDependencies(self, codeGenerator):
        dep = self.lowerBound.getDependencies(codeGenerator) + self.upperBound.getDependencies(codeGenerator) + self.differential.getDependencies(codeGenerator)
        return list(set(dep))

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
