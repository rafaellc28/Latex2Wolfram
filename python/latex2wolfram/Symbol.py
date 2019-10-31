from BaseExpression import *

class Symbol(BaseExpression):
    """
    Class representing the Symbol in the AST
    """

    PI = "pi"
    PRIME = "prime"
    PHI_LOWER = "phi_lower"
    SIGMA_LOWER = "sigma_lower"
    MU = "mu"

    def __init__(self, symbol):
        """
        Symbol

        :param symbol: str
        """

        BaseExpression.__init__(self)

        self.symbol = symbol

    def __str__(self):
        """
        to string
        """

        return "Symbol:"+str(self.symbol)

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
