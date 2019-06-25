from Expression import *
from ID import *
from Number import *
from Utils import *

class Identifier(Expression):
    """
    Class representing an Identifier in the AST of the MLP
    """
    
    def __init__(self, identifier):
        """
        Set the identifier
        
        :param identifier: ID
        """
        Expression.__init__(self)
        
        self.identifier = identifier

    def __str__(self):
        """
        to string
        """
        return "Identifier:" + str(self.identifier)

    def __len__(self):
        """
        length method
        """

        return 1

    def __iter__(self):
        """
        Get the iterator of the class
        """

        return [self]
        
    def getDependencies(self, codeGenerator):
        return [self.identifier.getDependencies(codeGenerator)]

    def setupEnvironment(self, codeSetup):
        """
        Generate the MathProg code for the declaration of this Identifier
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the MathProg code for this Identifier
        """
        return codeGenerator.generateCode(self)
    
    def generateCodeWithoutIndices(self, codeGenerator):
        """
        Generate the MathProg code for this Identifier without the Indexing, if there are 
        """
        return self.identifier.generateCode(codeGenerator)
