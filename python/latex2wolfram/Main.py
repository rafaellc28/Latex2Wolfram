# Abstract Syntax Tree (AST) for Latex (Mixed) Linear Progamming formulation (MLP) or System of Linear Equations
class Main:
    """
    Class representing the root node in the AST of a MLP
    """

    def __init__(self, problem):
        """
        Set the objective and the constraints
        
        :param problem: LinearProgram|LinearEquations
        """
        self.problem = problem
    
    def __str__(self):
        """
        to string
        """
        return str(self.problem) + "\n\n"

    def setupEnvironment(self, codeSetup):
        codeSetup.setupEnvironment(self)
    
    def generateCode(self, codeGenerator):
        """
        Generate the code in MathProg for this Linear Program
        """
        return codeGenerator.generateCode(self)
