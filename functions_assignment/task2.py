
def factorial(n):
    if n>=0:
        if n == 0 or n == 1:
            return n
        return n*factorial(n-1)
    else:
        print("Error...")
print(factorial(5))
print(factorial(0))
print(factorial(-3))
