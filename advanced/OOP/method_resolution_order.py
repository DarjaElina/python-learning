class A():
  num = 10

class B(A):
  pass

class C(A):
  num = 1

class D(B, C):
  pass

print(D.num) # 1

print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# It goes through all of the objects above
# And tries to find num
# And takes the first it finds
# In our case from class C


class X:
  pass

class Y:
  pass

class Z:
  pass

class A(X, Y):
  pass

class B(Y, Z):
  pass

class M(B, A, Z):
  pass

print(M.mro()) # [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>] 🥲