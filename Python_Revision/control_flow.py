"""control_flow.py
Examples of if/else, loops, and list comprehensions.
"""

def if_else_examples(n):
    """Return a string describing n."""
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"


def loops_examples():
    """Demonstrate for, while, break/continue and loop else."""
    out = {}

    # for loop
    items = [1, 2, 3]
    squared = []
    for i in items:
        squared.append(i * i)
    out['squared'] = squared

    # list comprehension
    out['comp'] = [x * 2 for x in range(5)]

    # while loop with break
    i = 0
    acc = []
    while i < 5:
        i += 1
        if i == 3:
            continue
        if i == 5:
            break
        acc.append(i)
    else:
        # runs if loop wasn't broken
        acc.append('done')
    out['while_acc'] = acc

    return out


if __name__ == "__main__":
    print("if/else examples: -2 ->", if_else_examples(-2))
    print("loops examples:\n", loops_examples())
