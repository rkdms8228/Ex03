x=1

def func(a):
    global x
    x=100
    return a + x


print(func(10))
print(x)