from BaseExpression import *

class Limit(BaseExpression):
    """
    Class representing an limit in the AST
    """

    def __init__(self, variable, to, expression):
        """
        Set the expression

        :param variable   : Identifier
        :param to         : Expression
        :param expression : Expression
        """

        BaseExpression.__init__(self)

        self.variable   = variable
        self.to         = to
        self.expression = expression

    def __str__(self):
        """
        to string
        """
        return "Limit: " + str(self.expression) + " as " + str(self.variable) + " -> " + str(self.to)

    def getDependencies(self, codeGenerator):
        dep = self.variable.getDependencies(codeGenerator) + self.to.getDependencies(codeGenerator) + self.expression.getDependencies(codeGenerator)
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
