"""
 This program about method of newton-rephson, with changes (changes to the original) -
 Creating a class for improvement and efficiency such as organization, reuse, etc
"""


class NewtonRaphson:
    def __init__(self, f, df, p0, tolerance=1e-6, max_iteration=50):  # Constructor with boot lines
        self.f = f
        self.df = df
        self.p0 = p0
        self.tolerance = tolerance
        self.max_iteration = max_iteration

    def find_root(self):  # A general function for finding a root with the Newton-Raphson method
        p1 = None
        print("{:<10} {:<15} {:<15} ".format("Iteration", "po", "p1"))
        for i in range(self.max_iteration):
            # if abs(self.df(self.p0)) < self.tolerance:
            if df(self.p0) == 0:
                print("Derivative is zero at p0, method cannot continue.")
                return

            p1 = self.p0 - self.f(self.p0) / self.df(self.p0)

            if abs(p1 - self.p0) < self.tolerance:
                return p1
            print("{:<10} {:<15.9f} {:<15.9f} ".format(i, self.p0, p1))
            self.p0 = p1
        return p1


if __name__ == '__main__':
    f = lambda x: x**3 - 3*x**2
    df = lambda x: 3*x**2 - 6*x
    p0 = -5
    tolerance = 1e-6
    max_iteration = 100

    root_finder = NewtonRaphson(f, df, p0, tolerance, max_iteration)  # Creating an object from class NewtonRephson
    root = root_finder.find_root()  # Calling the function 'find_root' of the object 'root_finder'
    print("\nThe equation f(x) has an approximate root at x = {:<15.9f} ", root)
