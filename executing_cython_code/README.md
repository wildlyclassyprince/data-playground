# Executing Cython Code

## Manual Compilation

Cython code is normally saved in files ending with `.pyx` (the `x` indicates it is different from standard Pythong code).

Translating Cython files to C:

```python
cython my_module.pyx
```

To enable support for Cython compilation in IPython:

```python
%load_ext Cython

%%cython_inline --annotate

def some_function(some_variable):
    return some_thing
```

Using `pyximport`:

```python
import pyximport
```