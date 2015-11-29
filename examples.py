#Assignment commands
x = 5
y = 6

# { (x,5),(y,6) }

# Conditions
if(True):
    x = 0
    z = 10
else:
    x = 1
    z = 11
# { (x, 0), (y,6), (z,10) }

#if (x > 0 v y == 6):
 #   x = 0
  #  z = 10
#else:
 #   x = 1
  #  z = 11


# Iteration

times = 10
while (times > 0):
    print("Wassup")
    times = (times - 2)

# Procedure call
def fun(a, b, c, x):
    result = a * (x*x) + b * x + c
    return result
