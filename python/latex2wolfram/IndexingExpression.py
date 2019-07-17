from BaseExpression import *

class IndexingExpression(BaseExpression):
    """
    Class representing an IndexingExpression in the AST
    """

    def __init__(self, identifier, _range):
        """
        Set the identifier and the range

        :param identifier : ID
        :param _range     : Range
        """

        BaseExpression.__init__(self)

        self.identifier = identifier
        self.range = _range

    def __str__(self):
        """
        to string
        """
        return "IndexingExpression: "+str(self.identifier)+" in "+str(self.range)

    def getDependencies(self, codeGenerator):
        return list(set(self.identifier.getDependencies(codeGenerator) + self.range.getDependencies(codeGenerator)))

    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this expression
        """
        return codeGenerator.generateCode(self)

class Range(BaseExpression):
    """
    Class representing an Range in the AST
    """

    def __init__(self, lowerBound, upperBound):
        """
        Set the lower and upper bounds

        :param lowerBound : Expression
        :param upperBound : Expression
        """

        BaseExpression.__init__(self)

        self.lowerBound = lowerBound
        self.upperBound = upperBound

    def __str__(self):
        """
        to string
        """
        return "Range: "+str(self.lowerBound)+".."+str(self.upperBound)

    def getDependencies(self, codeGenerator):
        return list(set(self.lowerBound.getDependencies(codeGenerator) + self.upperBound.getDependencies(codeGenerator)))

    def setupEnvironment(self, codeSetup):
        """
        Generate the Wolfram code for the identifiers and sets used in this expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the Wolfram code for this expression
        """
        return codeGenerator.generateCode(self)

