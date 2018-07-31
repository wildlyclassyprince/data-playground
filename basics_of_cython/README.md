# Basics of Cython

This repository is a tutorial on the fundamental basics of Cython.

The most basic nature of Cython can be stated as: Cython is Python with C data types.

There are several features of Cython that we need to be aware of:

1. Cython is Python: Almost any piece of Python code is also valid Cython code.

2. The Cython compiler converts Python code into C code which makes equivalent calls ot the Python/C API (this is partially how Cython is Python).

3. Conversions of Python values and C values occurs automatically wherever possible. In addition to this, error checking of Python operations and reference counting are also done automatically.

4. Python's full power of exception handling is available in Cython, i.e., the try-except and try-finally statements, all in the midst of handling C data.

We demonstrate some essential fundamentals using simple examples.