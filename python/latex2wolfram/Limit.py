from BaseExpression import *

class Limit(BaseExpression):
    """
    Class representing an limit in the AST
    """

    FROM_LEFT  = "fromLeft"
    FROM_RIGHT = "fromRight"

    def __init__(self, variable, to, expression, approachesFrom = None):
        """
        Set the expression

        :param variable       : Identifier
        :param to             : Expression
        :param expression     : Expression
        :param approachesFrom : FROM_LEFT | FROM_RIGHT
        """

        BaseExpression.__init__(self)

        self.variable       = variable
        self.to             = to
        self.expression     = expression
        self.approachesFrom = approachesFrom

    def __str__(self):
        """
        to string
        """
        res = "Limit: " + str(self.expression) + " as " + str(self.variable) + " -> " + str(self.to)

        if self.approachesFrom == Limit.FROM_LEFT:
            res += "-"

        elif self.approachesFrom == Limit.FROM_RIGHT:
            res += "+"

        return res

    def getDependencies(self, codeGenerator):
        dep = self.variable.getDependencies(codeGenerator) + self.to.getDependencies(codeGenerator) + self.expression.getDependencies(codeGenerator)
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
