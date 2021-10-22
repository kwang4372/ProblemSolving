import sys
sys.setrecursionlimit(100000)

needed = 0
def calMoney(price, count):
    global needed
    needed += price*count
    if count > 0:
        return calMoney(price, count-1)
    else:
        return needed

def solution(price, money, count):    
    rest = money - calMoney(price, count) 
    answer = -1*rest if rest<0 else 0
    
    return answer