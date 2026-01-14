"""data_structures.py
Examples for lists, dictionaries, sets and tuples.
"""

def list_ops():
    lst = [1, 2, 3]
    lst.append(4)
    lst.extend([5, 6])
    sliced = lst[1:4]
    comp = [x * x for x in lst]
    return {'list': lst, 'sliced': sliced, 'comp': comp}


def dict_ops():
    d = {'a': 1, 'b': 2}
    d['c'] = 3
    val = d.get('d', 'missing')
    # dict comprehension
    squared = {k: v * v for k, v in d.items()}
    return {'dict': d, 'get_missing': val, 'squared': squared}


def set_tuple_ops():
    t = (1, 2, 3)
    s = set([1, 2, 2, 3])
    s.add(4)
    union = s.union({5, 6})
    return {'tuple': t, 'set': s, 'union': union}


if __name__ == "__main__":
    print('list_ops:', list_ops())
    print('dict_ops:', dict_ops())
    print('set_tuple_ops:', set_tuple_ops())
