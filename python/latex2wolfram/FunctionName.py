from BaseExpression import *

class FunctionName(BaseExpression):
    """
    Class representing the Function Name expression in the AST
    """

    ABS    = "abs"
    CEIL   = "ceil"
    FLOOR  = "floor"
    ROUND  = "round"
    TRUNC  = "trunc"
    LENGTH = "length"
    MIN    = "min"
    MAX    = "max"
    EXP    = "exp"
    LN     = "ln"
    LOG    = "log"
    LOG2   = "log2"
    LOG10  = "log10"
    SQRT   = "sqrt"

    SIN    = "sin"
    COS    = "cos"
    TAN    = "tan"
    ATAN   = "atan"

    def __init__(self, function):
        """
        FunctionName

        :param function: str|Identifier
        """

        BaseExpression.__init__(self)

        self.function = function

    def __str__(self):
        """
        to string
        """

        return "FunctionName:"+str(self.function)

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
