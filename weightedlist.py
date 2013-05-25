import random

def pick(lst):
    '''
    lst = [(weight, value)]
    '''
    total = 0
    for weight, value in lst:
        if weight <= 0:
            raise ValueError('weights must be > 0')
        total += weight
    n = random.randint(1, total)
    for weight, value in lst:
        n -= weight
        if n <= 0:
            return value