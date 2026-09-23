p = int(input("write number of p:"))
a = 0
b = 1
if 0 > p:
    result = a
else:
    while a <= p:
        a, b = b, a + b
        result = a
    result = a

print(f"Перше число Фібоначчі, більше за {p}: {result}")
