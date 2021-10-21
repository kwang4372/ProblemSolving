def Fibonacci(k):
    if k > 2:
        return Fibonacci(k-1) + Fibonacci(k-2)
    elif k==1 or k==2:
        return 1
    else:
        return 0

n = int(input())
print(Fibonacci(n))