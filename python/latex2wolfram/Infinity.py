from BaseExpression import *

class Infinity(BaseExpression):
    """
    Class representing the infinity symbol in the AST
    """

    def __init__(self):
        """
        Infinity
        """

        BaseExpression.__init__(self)

    def __str__(self):
        """
        to string
        """
        return "Infinity"

    def getDependencies(self, codeGenerator):
        return []

    def setupEnvironment(self, codeSetup):
        """
        Setup the Wolfram code
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code
        """
        return codeGenerator.generateCode(self)
