# The pdb module is Python's built-in debugger.

# Use it to step through code, inspect variables, and set breakpoints during development and troubleshooting.

# Without using pdb (we use `print`` to debug errors)
# def add(n1, n2):
#   print(f"Num is is {n1}, num2 is {n2}")
#   return n1 + n2
# add(4, 'not a number :(')

# With pdp
import pdb

def add(n1, n2):
  pdb.set_trace()
  return n1 + n2

add(4, 'not a number :(')

# Opens an interactive shell:
# (Pdb) n1
# 4
# (Pdb) n2
# 'not a number :('
# (Pdb) 