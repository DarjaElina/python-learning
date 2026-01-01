# The nonlocal keyword is used to work with variables inside nested functions,
# where the variable should not belong to the inner function.

def outer():
  x = "local"
  
  def inner():
    nonlocal x
    x = "nonlocal"
    print(f"inner: {x}")

  inner()
  print(f"outer: {x}")

outer()