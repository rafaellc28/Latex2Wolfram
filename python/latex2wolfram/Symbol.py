from BaseExpression import *

class Symbol(BaseExpression):
    """
    Class representing the Symbol in the AST
    """
    PRIME = "prime"
    PHI_LOWER = "phi_lower"
    PSI_LOWER = "psi_lower"
    SIGMA_LOWER = "sigma_lower"
    ZETA_LOWER = "zeta_lower"
    ETA_LOWER = "eta_lower"
    DELTA_LOWER = "delta_lower"
    THETA_LOWER = "theta_lower"
    MU = "mu"
    PI = "pi"
    BETA = "beta"
    GAMMA = "gamma"

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
