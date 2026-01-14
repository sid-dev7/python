"""file_io_and_exceptions.py
Demonstrate basic file read/write and exception handling.
"""

def write_read_file(path='demo_output.txt'):
    """Write a small string to a file and read it back."""
    text = 'Hello from file_io_and_exceptions!'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

    with open(path, 'r', encoding='utf-8') as f:
        read = f.read()
    return read


def handle_exceptions(dividend, divisor):
    """Show try/except/finally and raising a ValueError for invalid input."""
    if divisor == 0:
        raise ValueError('divisor must not be zero')
    try:
        result = dividend / divisor
    except TypeError as e:
        return f'Invalid types: {e}'
    finally:
        # cleanup or logging could go here
        pass
    return result


if __name__ == "__main__":
    print('write_read_file ->', write_read_file())
    try:
        print('handle_exceptions(10, 2) ->', handle_exceptions(10, 2))
    except ValueError as e:
        print('Caught ValueError:', e)
