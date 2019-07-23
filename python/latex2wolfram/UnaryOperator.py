from BaseExpression import *

class UnaryOperator(BaseExpression):
    """
    Class representing the Binary Operator in the AST
    """

    PLUS  = "+"
    MINUS = "-"
    FACTORIAL = "!"

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

        return "UnaryOperator:"+str(self.operator)

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
