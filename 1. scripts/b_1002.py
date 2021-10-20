import math

T = int(input())

case = []
for i in range(T):
    case.append(input().split())

for idx in case:
    x1, y1, r1, x2, y2, r2 = map(int, idx)

    dist = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    r = [r1, r2, dist]
    mr = max(r)
    r.remove(mr)

    if dist==0 and r1==r2:
        print("-1")
    elif dist==r1+r2 or mr==sum(r):
        print("1")
    elif mr > sum(r):
        print("0")
    else:
        print("2")  