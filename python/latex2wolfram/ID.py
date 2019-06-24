from Expression import *

class ID(Expression):
    """
    Class representing a Identifier node in the AST of the MLP
    """
    
    def __init__(self, value):
        """
        Set the string that represents the identifier
        
        :param value: string
        """

        Expression.__init__(self)

        value = value.replace("\\_", "_")
        self.value = value
    
    def __str__(self):
        """
        to string
        """
        
        return "ID: " +self.value

    def __iter__(self):
        """
        Get the iterator of the class
        """

        return [self]
    
    def getDependencies(self, codeGenerator):
        return [self.getSymbolName(codeGenerator)]
    
    def setupEnvironment(self, codeSetup):
        """
        Generate the MathProg code for the declaration of this ID
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the MathProg code for this Identifier
        """
        return codeGenerator.generateCode(self)
