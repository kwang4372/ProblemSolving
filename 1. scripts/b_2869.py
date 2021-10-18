A, B, V = map(int, input().split())
day=0

step = A - B
h = V - A

if h%step == 0:
    day = h // step +1
else:
    day = h // step +2

print(day)