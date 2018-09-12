# -*- coding: utf-8 -*-
'''
A modification of `random_string_3.py`.
The modification allows us to have our output in a particular order,
that is, chronological order in this case.
We will use the `Pool` class, which has the following methods of interest:
1. `apply`
2. `map`
3. `apply_async`
4. `map_async`

In this file we will the `map` method,
but produces completely different output.
'''

import multiprocessing as mp
import random
import string

random.seed(123)

# Example function
def random_string(length):
    '''Generates a random string of numbers and letters.'''
    return ''.join(random.choice(
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
    ) for i in range(length))

# Set the number of processes we want to run
POOL = mp.Pool(processes=4)

# Immediately retrieve our results
RESULTS = POOL.map(random_string, range(20))

# Get process results
print(RESULTS)
