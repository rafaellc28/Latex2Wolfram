from BaseExpression import *

class DifferentialVariable(BaseExpression):
    """
    Class representing the Differential Variable in the AST
    """

    def __init__(self, identifier, primeList, argumentList = None):
        """
        DifferentialVariable

        :param identifier   : Identifier
        :param primeList    : [Symbol]
        :param argumentList : ExpressionList
        """

        BaseExpression.__init__(self)

        self.identifier   = identifier
        self.primeList    = primeList
        self.argumentList = argumentList

    def __str__(self):
        """
        to string
        """
        res = "DifferentialVariable: " + str(self.identifier) + "".join(map(lambda el: str(el), self.primeList))

        if self.argumentList:
            res += "(" + str(self.argumentList) + ")"

        return res

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
