N = int(input())

numbers = []
for i in range(N):
    numbers.append(int(input()))

for i in range(N-1):
    for j in range(i, N):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]            

for num in numbers:
    print(num)

