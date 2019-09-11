from BaseExpression import *

class BinaryOperator(BaseExpression):
    """
    Class representing the Binary Operator in the AST
    """

    PLUS  = "+"
    MINUS = "-"
    TIMES = "*"
    DIV   = "/"
    MOD   = "%"
    POW   = "^"
    CROSS = "cross"

    def __init__(self, operator):
        """
        BinaryOperator

        :param operator: str
        """

        BaseExpression.__init__(self)

        self.operator = operator

    def __str__(self):
        """
        to string
        """

        return "BinaryOperator:"+str(self.operator)

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
