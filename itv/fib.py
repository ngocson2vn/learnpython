def fib1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib1(n-2) + fib1(n-1)

def fib2(n):
    ret = []
    if n == 1:
        ret.append(0)
        return ret
    elif n >= 2:
        ret.extend([0, 1])
    for i in range(2, n):
        ret.append(ret[i-2] + ret[i-1])
    return ret


n = 20
for e in range(1, n + 1):
    print("{}".format(fib1(e)), end=" ")
print("")

ret = fib2(n)
print(" ".join(map(str, ret)))


