#ciąg Fibonacciego to ciag liczb ktory zaczyna sie od dwoch jedynek. Pierwszy element to jedynka, drugi to jedynka a kolejny to suma poprzednich

# 1 1 2 3 5 8 ...

def fib(n): #argument jako n-ty ("entny") element ciągu
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    sum = 0

    for i in range (3, n+1):
        sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, sum #zamieniamy element 1 z 2 i 2 staje sie suma 1 1 2 3 ---> z kazda iteracja przesuwamy sie, 1 i 1 to elem 1 i elem 2, 1 elem 1 a elem 2 to 2 czyli suma

    return sum

for n in range(1, 10):
    print(n, "->}" , fib(n))

print(fib(6))