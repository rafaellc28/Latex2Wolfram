from BaseExpression import *

class Integral(BaseExpression):
    """
    Class representing an integral in the AST
    """

    def __init__(self, lowerBound, upperBound, integrand, differential):
        """
        Set the expression and the function

        :param lowerBound   : Expression
        :param upperBound   : Expression
        :param integrand    : Expression
        :param differential : [a-zA-Z]
        """

        BaseExpression.__init__(self)

        self.lowerBound   = lowerBound
        self.upperBound   = upperBound
        self.integrand    = integrand
        self.differential = differential

    def __str__(self):
        """
        to string
        """
        return "Integral["+str(self.lowerBound)+","+str(self.upperBound)+"]("+str(self.integrand)+")d"+str(self.differential)

    def getDependencies(self, codeGenerator):
        dep = self.lowerBound.getDependencies(codeGenerator) + self.upperBound.getDependencies(codeGenerator) + self.differential.getDependencies(codeGenerator)
        return list(set(dep))

    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this expression with function
        """
        return codeGenerator.generateCode(self)
