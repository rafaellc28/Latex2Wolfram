from Expression import *

class Number(Expression):
    """
    Class representing a number node in the AST of the MLP
    """

    def __init__(self, number):
        """
        Set the number
        
        :param number: float
        """
        Expression.__init__(self)

        self.number = number
    
    def __str__(self):
        """
        to string
        """
        
        return str(self.number)

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

    def lessThanZero(self):
        return self.number[0] == "-"

    def getNumber(self):
        return self.number

    def getDependencies(self, codeGenerator):
        return []
        
    def setupEnvironment(self, codeSetup):
        """
        Setup environment
        """
        codeSetup.setupEnvironment(self)
        
    def generateCode(self, codeGenerator):
        """
        Generate the AMPL code for this Number
        """
        return codeGenerator.generateCode(self)

class ImaginaryNumber(Expression):
    """
    Class representing a number node in the AST of the MLP
    """

    def __init__(self, number = None):
        """
        Set the number
        
        :param number: float
        """
        Expression.__init__(self)

        self.number = number
    
    def __str__(self):
        """
        to string
        """
        res = "i"

        if self.number:
            res = str(self.number) + res
            
        return res

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

    def lessThanZero(self):
        return self.number[0] == "-"

    def getNumber(self):
        return self.number

    def getDependencies(self, codeGenerator):
        return []
        
    def setupEnvironment(self, codeSetup):
        """
        Setup environment
        """
        codeSetup.setupEnvironment(self)
        
    def generateCode(self, codeGenerator):
        """
        Generate the AMPL code for this Number
        """
        return codeGenerator.generateCode(self)

class NapierNumber(Expression):
    """
    Class representing a number node in the AST of the MLP
    """

    def __init__(self, number = None):
        """
        Set the number
        
        :param number: float
        """
        Expression.__init__(self)

        self.number = number
    
    def __str__(self):
        """
        to string
        """
        res = "e"

        if self.number:
            res = str(self.number) + res
            
        return res

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

    def lessThanZero(self):
        return self.number[0] == "-"

    def getNumber(self):
        return self.number

    def getDependencies(self, codeGenerator):
        return []
        
    def setupEnvironment(self, codeSetup):
        """
        Setup environment
        """
        codeSetup.setupEnvironment(self)
        
    def generateCode(self, codeGenerator):
        """
        Generate the AMPL code for this Number
        """
        return codeGenerator.generateCode(self)
