from Expression import *

class Range(Expression):
    """
    Class representing a range in the AST of the MLP
    """
    
    def __init__(self, rangeInit, rangeEnd, by = None):
        """
        Set the range init and end
        
        :param rangeInit : NumericExpression | Identifier
        :param rangeEnd  : NumericExpression | Identifier
        :param by        : NumericExpression | Identifier
        """
        
        self.rangeInit = rangeInit
        self.rangeEnd  = rangeEnd
        self.by = by

    def __str__(self):
        """
        to string
        """
        res = "Range: [" + str(self.rangeInit) + ".." + str(self.rangeEnd)
        if self.by != None:
            res += " by " + str(self.by)
        res += "]"
        
        return res
        
    def getRangeInit(self):
        return self.rangeInit
        
    def getRangeEnd(self):
        return self.rangeEnd
        
    def getBy(self):
        return self.by
        
    def getDependencies(self, codeGenerator):
        dep = self.rangeInit.getDependencies(codeGenerator) + self.rangeEnd.getDependencies(codeGenerator)

        if self.by != None:
            dep += self.by.getDependencies(codeGenerator)

        return list(set(dep))

    def setupEnvironment(self, codeSetup):
        """
        Generate the MathProg code for the declaration of identifiers used in this range expression
        """
        codeSetup.setupEnvironment(self)

    def generateCode(self, codeGenerator):
        """
        Generate the MathProg code for this Range
        """
        return codeGenerator.generateCode(self)
