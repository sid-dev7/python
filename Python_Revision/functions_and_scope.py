"""functions_and_scope.py
Demonstrate function definitions, args, kwargs and variable scope.
"""

def basic_function(a, b):
    """Return sum of two values."""
    return a + b


def default_and_kw_args(a, b=10, *args, **kwargs):
    """Show default args, varargs and kwargs usage."""
    result = a + b
    extra = sum(args) if args else 0
    # merge kwargs values if they are numeric
    kw_sum = sum(v for v in kwargs.values() if isinstance(v, (int, float)))
    return result + extra + kw_sum


def scope_example():
    """Illustrate local, global and nonlocal scope."""
    x = 'outer'

    def inner():
        nonlocal x
        x = 'inner'
        return x

    before = x
    after = inner()
    return before, after


if __name__ == "__main__":
    print('basic_function(2,3)=', basic_function(2, 3))
    print('default_and_kw_args(1, 2, 3, 4, extra=5)=', default_and_kw_args(1, 2, 3, 4, extra=5))
    print('scope_example before/after:', scope_example())
