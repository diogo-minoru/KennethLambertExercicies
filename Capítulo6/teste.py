"""
def summation(lower, upper):
    if lower > upper:
        return 0
    else:
        return lower + summation (lower + 1, upper)
   
print(summation(2,5))

"""
"""
def summation(lower, upper):
    resultado = 0
    return sum([resultado + n for n in range(lower, upper + 1)])

"""
"""
def fibonacci(n):
    if n < 3:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))

"""
"""
def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci_iterativo())
"""

"""
def fatorial(n):
    if n <= 1:
        return 1
    else: return n * fatorial(n - 1) 

print(fatorial(-5))

"""
def example(aString, index):
   if index < len(aString):
     print(index)
     example(aString, index + 1)
     #print(index)
     #print(aString[index], end = "")

example("hello", 0)