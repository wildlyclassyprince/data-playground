# -*- coding: utf-8 -*-
'''
A simple example of parallel programming.

We will use Python's `multiprocessing` module to run
a function that generates a list of random strings.
'''

import multiprocessing as mp
import random
import string

random.seed(123)

# Define an output queue
OUTPUT = mp.Queue()

# Example function
def random_string(length, output):
    '''Generates a random string of numbers and letters.'''
    rand_str = ''.join(random.choice(
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
    ) for i in range(length))
    OUTPUT.put(rand_str)

# Setup a list oF processes we want to run
PROCESSES = [mp.Process(target=random_string, args=(5, OUTPUT)) for x in range(1000)]

# Running the processes
for p in PROCESSES:
    p.start()

# Exit the completed processes
for p in PROCESSES:
    p.join()

# Get process results
RESULTS = [OUTPUT.get() for p in PROCESSES]
print(RESULTS)
