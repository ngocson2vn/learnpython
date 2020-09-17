# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    if N == 0:
        return 1

    strN = str(N)
    digits = len(strN)
    zeros = strN.count('0')
    print("zeros = {}".format(zeros))
    nonzero_digits = digits - zeros
    
    if nonzero_digits == 1:
        return 1

    s = strN.replace('0', '')
    print("N excluded zeros = {}".format(s))
    if s.count(s[0]) == len(s):
        return 1
    
    return nonzero_digits * (nonzero_digits - 1)


print(solution(0))

print()
print(solution(1))

print()
print(solution(10))

print()
print(solution(100))

print()
print(solution(101))

print()
print(solution(10011))

print()
print(solution(10012))

print()
print(solution(12345))
