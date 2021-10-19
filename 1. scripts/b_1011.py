import math

T = int(input())
xy = []
for i in range(T):
    x, y = map(int, input().split())
    xy.append((x,y))


for xx, yy in xy:
    count = 0
    
    dist = yy - xx
    sq = round(math.sqrt(dist))
    
    if sq*sq < dist <= sq*sq + sq:
        count = 2*sq
    else:
        count = 2*sq - 1    

    print(count)

'''
20  12344321     4^2+4 8         4.xxx
25  123454321    5^2 9           5
30  1234554321   5^2+5 10(2i)    5.xxx
36  12345654321  6^6  11(2i-1)   6
'''