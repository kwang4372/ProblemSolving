n = int(input())
words = []
for i in range(0, n):
    words.append(input())

count = n
for word in words:
    for i in range(0, len(word)-1):
        if word[i] == word[i+1]:
            pass
        else:
            if word[i] in word[(i+1):]:
                count -= 1
                break

print(count)