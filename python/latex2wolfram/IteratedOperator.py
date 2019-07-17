from BaseExpression import *

class IteratedOperator(BaseExpression):
    """
    Class representing the Binary Operator in the AST
    """

    SUM  = "sum"
    PROD = "prod"
    MAX  = "max"
    MIN  = "min"

    def __init__(self, operator):
        """
        BinaryOperator

        :param function: str
        """

        BaseExpression.__init__(self)

        self.operator = operator

    def __str__(self):
        """
        to string
        """

        return "IteratedOperator:"+str(self.operator)

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
