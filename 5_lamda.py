add = lambda a, b, c : a+b+c
print(add(10, 20, 30))


number = [1,2,3,4,5]

squares = map(lambda x: x*x, number)

print( list (squares))

evneNumber = filter(lambda x: x % 2 == 0, number)


print( list (evneNumber))


