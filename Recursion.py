#POWER OF TWO

def poweroftwo(n):
    if n == 0:
        return 1
    else:
        power = poweroftwo(n-1)
        return power*2
print(poweroftwo(5))


#FACTORIAL

def factorial(n):
    assert n>=0 and int(n) == n, "The number should be int only"
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#FABONACCI

def fabonacci(n):
    if n in [0,1]:
        return n
    else:
        return fabonacci(n-1)+fabonacci(n-2)
print(fabonacci(5))