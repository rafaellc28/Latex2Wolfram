from BaseExpression import *

class ConstraintOperator(BaseExpression):
    """
    Class representing the Binary Operator in the AST
    """

    LT  = "LT"
    LE  = "LE"
    GT  = "GT"
    GE  = "GE"
    EQ  = "EQ"
    NEQ = "NEQ"

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

        return "ConstraintOperator:"+str(self.operator)

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
