
def fib(n): #argument jako n-ty ("entny") element ciągu
    if n < 1:
        return None
    if n < 3:
        return 1

    return fib(n - 1) + fib(n - 2) #fib (2) + fib(2)

for n in range(1, 100):
    print(n, "->", fib(n))