def fixed_point(f, start):
    """
    Find a fixed point of the function f starting from start.
    """
    tolerance = 0.0001
    def is_close_enough(x, y):
        return abs(x - y) < tolerance
    def iterate(old, new):
        if is_close_enough(old, new):
            return new
        else:
            return iterate(new, f(new))
    return iterate(start, f(start))

def derivative(f):
    """
    Return a function that computes the derivative of f.
    """
    dx = 0.00001
    return lambda x: (f(x + dx) - f(x)) / dx

def newton(f, guess):
    """
    Use Newton's method to find a root of f.
    """
    df = derivative(f)
    return fixed_point(lambda x: f(x)/df(x), guess)

def sqrt(x):
    """
    Return the square root of x.
    """
    return newton(lambda y: y**2 - x, 1.0)

print(sqrt(9))



