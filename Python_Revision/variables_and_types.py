"""variables_and_types.py
Demonstrate variable declarations and basic types in Python.
Contains small functions you can import or run directly.
"""

def demonstrate_variables():
    """Show variable creation and types."""
    a = 10                  # int
    b = 3.14                # float
    c = "hello"           # str
    d = True                # bool
    e = None                # NoneType

    # multiple assignment
    x, y, z = 1, 2.0, "three"

    return {
        'a': (a, type(a)),
        'b': (b, type(b)),
        'c': (c, type(c)),
        'd': (d, type(d)),
        'e': (e, type(e)),
        'x': (x, type(x)),
        'y': (y, type(y)),
        'z': (z, type(z)),
    }


def type_examples():
    """Simple casting and formatted output examples."""
    n = 5
    s = "4"
    summed = n + int(s)     # cast str to int
    formatted = f"{n} + {s} = {summed}"
    return formatted


if __name__ == "__main__":
    print("Variable examples:\n", demonstrate_variables())
    print("Type examples:\n", type_examples())
