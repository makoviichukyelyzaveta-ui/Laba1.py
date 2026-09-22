import math
x= float(input("enter the value of x:"))
if x > 45:
    z = -math.sqrt(x)
else:
    z = math.sin(2 * x)

print(f"Значення z({x}) = {z}")