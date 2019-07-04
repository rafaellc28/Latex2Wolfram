from BaseExpression import *

class Integral(BaseExpression):
    """
    Class representing an integral in the AST
    """

    def __init__(self, integrand, differential, lowerBound = None, upperBound = None):
        """
        Set the expression and the function

        :param integrand    : Expression
        :param differential : [a-zA-Z]
        :param lowerBound   : Expression
        :param upperBound   : Expression
        """

        BaseExpression.__init__(self)

        self.integrand    = integrand
        self.differential = differential
        self.lowerBound   = lowerBound
        self.upperBound   = upperBound

    def __str__(self):
        """
        to string
        """
        return "Integral["+str(self.lowerBound)+","+str(self.upperBound)+"]("+str(self.integrand)+")d"+str(self.differential)

    def getDependencies(self, codeGenerator):
        dep = self.differential.getDependencies(codeGenerator)

        if self.lowerBound:
            dep += self.lowerBound.getDependencies(codeGenerator)

        if self.upperBound:
            dep += self.upperBound.getDependencies(codeGenerator)
        
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
