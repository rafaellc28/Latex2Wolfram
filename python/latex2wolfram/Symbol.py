from BaseExpression import *

class Symbol(BaseExpression):
    """
    Class representing the Symbol in the AST
    """
    PRIME = "prime"
    XI_LOWER = "xi_lower"
    CHI_LOWER = "chi_lower"
    PHI_LOWER = "phi_lower"
    PSI_LOWER = "psi_lower"
    SIGMA_LOWER = "sigma_lower"
    ZETA_LOWER = "zeta_lower"
    ETA_LOWER = "eta_lower"
    DELTA_LOWER = "delta_lower"
    THETA_LOWER = "theta_lower"
    LAMBDA_LOWER = "lambda_lower"
    EPSILON_LOWER = "epsilon_lower"
    TAU_LOWER = "tau_lower"
    KAPPA_LOWER = "kappa_lower"
    OMEGA_LOWER = "omega_lower"
    ALPHA_LOWER = "alpha_lower"
    NU_LOWER = "nu_lower"
    RHO_LOWER = "rho_lower"
    OMICRON_LOWER = "omicron_lower"
    UPSILON_LOWER = "upsilon_lower"
    IOTA_LOWER = "iota_lower"
    BETA_LOWER = "beta_lower"
    GAMMA_LOWER = "gamma_lower"
    MU_LOWER = "mu_lower"
    PI_UPPER = "pi_upper"
    PI = "pi"
    BETA = "beta"
    GAMMA = "gamma"
    MU = "mu"
    KAPPA = "kappa"
    OMICRON = "omicron"
    IOTA = "iota"
    OMEGA = "omega"
    LAMBDA = "lambda"
    PSI = "psi"
    PHI = "phi"
    SIGMA = "sigma"
    ETA = "eta"
    ZETA = "zeta"
    THETA = "theta"
    EPSILON = "epsilon"
    TAU = "tau"
    ALPHA = "alpha"
    XI = "xi"
    CHI = "chi"
    NU = "nu"
    RHO = "rho"
    UPSILON = "upsilon"

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
