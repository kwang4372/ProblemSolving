N = input()
sizeN = len(N)

minval = int(N) - 9*sizeN if int(N) - 9*sizeN >= 0 else 0
maxval = int(N) + 1
print(minval, maxval)

for num in range(minval, maxval):
    listNum = list(map(int, str(num)))
    
    if int(N) == num + sum(listNum):
        print(num)
        break
    elif int(N) == num:
        print(0)