

a = {1 ,2 ,3 ,4 ,5}
b = {3, 4, 5, 6, 7}

# intersection 
print( a & b)  # { 3, 4 ,5} 
# или a.intersection(b)
# или сразу применить к "a"
# a &= b
# примерно как +=
# или a.intersection_update(b)


# union
print( a | b) # {1, 2, 3, 4, 5, 6, 7}
# аналог a.union(b)
# a |= b результат сохр в "а"


# вычитание (отнимает общие от первого сета)
print(a - b) # {1, 2}
print( b - a) # {6, 7}
# a -= b

# исключение общих элементов ^
print(a ^ b) # {1, 2, 6, 7}
# a ^= b

# является подмножеством или нет 
c = {2, 3}
d = {2, 3, 4, 5, 6}
print(c < d) # True

