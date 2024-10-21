def fun1(n):
    """restituisce i primi tre multipli del numero n"""

    return n, 2*n, 3*n


m1, m2, m3 = fun1(4)
s1, s2, s3 = fun1("ciao")
l1, l2, l3 = fun1([1, 2])

print(m1, m2, m3)
print(s1, s2, s3)
print(l1, l2, l3)


x = 1000
y = 10
print("Parametro 1: ", " " * (10 - len(str(x))), x)
print("Parametro 2: ", " " * (10 - len(str(y))), y)