from BaseExpression import *

class ChooseExpression(BaseExpression):
    """
    Class representing an choose expression in the AST
    """

    def __init__(self, expression1, expression2):
        """
        Set the expression

        :param expression1 : Expression
        :param expression2 : Expression
        """

        BaseExpression.__init__(self)

        self.expression1 = expression1
        self.expression2 = expression2

    def __str__(self):
        """
        to string
        """
        return "ChooseExpression: {" + str(self.expression1) + " choose " + str(self.expression2) + "}"

    def getDependencies(self, codeGenerator):
        dep = self.expression1.getDependencies(codeGenerator) + self.expression2.getDependencies(codeGenerator)
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
