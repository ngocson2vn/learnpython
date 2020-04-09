def changer(x):
    print("id(x) = {}".format(id(x)))
    x[1] = 'Son'
    x = ['a', 'b']
    print("id(x) = {}".format(id(x)))

L = [1, 2]
print("id(L) = {}".format(id(L)))
print("L = {}".format(L))
changer(L)
print("L = {}".format(L))
