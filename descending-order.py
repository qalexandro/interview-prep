def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

# with lambda
Descending_Order1 = lambda n: int(''.join(reversed(sorted(str(n)))))

# with slicing
def Descending_Order(num):
    return int(''.join(sorted(str(num))[::-1]))

print(Descending_Order(34453))
print(Descending_Order1(34453))
print(descending_order(34453))