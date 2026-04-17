import sympy as sp

class IntegralSolver:
    def __init__(self, expression, variable):
        self.expression = expression
        self.variable = variable
        self.method = None

    def detect_method(self):
        # This method detects the best solving method automatically
        if self.expression.has(sp.sin, sp.cos):
            self.method = 'trigonometric'
        elif self.expression.has(sp.exp):
            self.method = 'exponential'
        else:
            self.method = 'default'

    def solve(self):
        self.detect_method()
        if self.method == 'trigonometric':
            return sp.integrate(self.expression, self.variable)  # Simplification for demonstration
        elif self.method == 'exponential':
            return sp.integrate(self.expression, self.variable)  # Simplification for demonstration
        else:
            return sp.integrate(self.expression, self.variable)  # Fallback method

# Example usage:
# solver = IntegralSolver(sp.sin(sp.Symbol('x')), sp.Symbol('x'))
# result = solver.solve()
# print(result)