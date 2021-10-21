from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

cmb = list(combinations(cards, 3))

s = []
for idx in cmb:
    s.append(M-sum(idx))

minval = 100001
minarg = -1
for idx, value in enumerate(s):
    if 0 <= value < minval:
        minval = value
        minarg = idx

print(sum(cmb[minarg]))