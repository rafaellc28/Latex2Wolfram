from Expression import *
from ID import *
from Number import *
from NumericExpression import *
from Utils import *

class Identifier(Expression):
    """
    Class representing an Identifier in the AST of the MLP
    """
    
    def __init__(self, identifier, sub_indices = []):
        """
        Set the identifier and the sub indices (if there are)
        
        :param identifier: ID
        :param sub_indices: [ID|Number]
        """
        Expression.__init__(self)
        
        self.identifier = identifier
        self.sub_indices = sub_indices
        self.dimenSet = 1
        self.isInSet = False
        self.isSet = None
        self.isVar = None
        self.isParam = None
        self.isReal = False
        self.isSymbolic = False
        self.isLogical = False
        self.isBinary = False
        self.isInteger = False
        self.isNatural = False
        self.isSubIndice = False
        self.isInt = False
        self.isDeclaredAsParam = None
        self.isDeclaredAsSet = None
        self.isDeclaredAsVar = None

    def __str__(self):
        """
        to string
        """
        
        var = ""
        if self.isSet and isinstance(self.dimenSet, int) and self.dimenSet > 1:
            var += str(self.identifier) + "{"+str(self.dimenSet)+"}"
        else:
            var += str(self.identifier)

        if len(self.sub_indices) > 0:
            if isinstance(self.sub_indices, Identifier) or isinstance(self.sub_indices, ID) or isinstance(self.sub_indices, Number) or isinstance(self.sub_indices, NumericExpression):
                res = var + "[" + str(self.sub_indices) + "]"
            else:
                res = var + "[" + ",".join(map(lambda i: str(i), self.sub_indices)) + "]"
        else:
            res = var
        
        return "Var:" + res

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
        
    def getSymbol(self):
        return self
        
    def getSymbolName(self, codeGenerator):
        return self.generateCodeWithoutIndices(codeGenerator)

    def getSymbolNameWithIndices(self, codeGenerator):
        return self.generateCode(codeGenerator)

    def addSet(self, inSet):
        self.inSets += [inSet]

    def setIsInSet(self, isInSet):
        self.isInSet = isInSet
    
    def setIsSet(self, isSet):
        self.isSet = isSet

    def setIsParam(self, isParam):
        self.isParam = isParam

    def setIsSymbolic(self, isSymbolic):
        self.isSymbolic = isSymbolic

    def setIsLogical(self, isLogical):
        self.isLogical = isLogical

    def setDimenSet(self, dimen):
        self.dimenSet = dimen

    def setIsVar(self, isVar):
        self.isVar = isVar

    def setIsSubIndice(self, isSubIndice):
        self.isSubIndice = isSubIndice

    def setSubIndices(self, subIndices):
        self.sub_indices = subIndices
 
    def getDependencies(self, codeGenerator):
        dep = list(set(Utils._flatten(map(lambda el: el.getDependencies(codeGenerator), self.sub_indices))))
        return list(set(self.identifier.getDependencies(codeGenerator) + dep))

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
