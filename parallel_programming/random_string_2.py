# -*- coding: utf-8 -*-
'''
A modification of `random_string.py`.
The modification allows us to have our output in a particular order,
that is, chronological order in this case.
We have manually coded this modification.
'''

import multiprocessing as mp
import random
import string

random.seed(123)

# Define an output queue
OUTPUT = mp.Queue()

# Example function
def random_string(length, position, output):
    '''Generates a random string of numbers and letters.'''
    rand_str = ''.join(random.choice(
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
    ) for i in range(length))
    output.put((position, rand_str))

# Setup a list oF processes we want to run
PROCESSES = [mp.Process(target=random_string, args=(5, x, OUTPUT)) for x in range(20)]

# Running the processes
for p in PROCESSES:
    p.start()

# Exit the completed processes
for p in PROCESSES:
    p.join()

# Get process results
RESULTS = [OUTPUT.get() for p in PROCESSES]
print("Raw Results:\n{}".format(RESULTS))

# Sorting the results
RESULTS.sort()
RESULTS = [r[1] for r in RESULTS]
print("Sorted Results:\n{}".format(RESULTS))
