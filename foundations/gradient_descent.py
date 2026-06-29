class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        x = init
        F = self.f
        Fp = self.fp

        for i in range(iterations):
            F_val = F(x)
            Fp_val = Fp(x)

            x = x - learning_rate * Fp_val

        return round(x, 5)


    def f(self, x):
        return x**2

    def fp(self, x):
        return 2*x
