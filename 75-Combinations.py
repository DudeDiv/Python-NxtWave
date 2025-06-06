from itertools import combinations
line = input().split() #a,b = input().split(" ")
int_val = int(line[1]) #b = int(b)
for i in range(1, int_val+1):
    for j in list(combinations(sorted(line[0]), i)):
        print("".join(j))

"""
from itertools import combinations
word, value = input().strip().split()
word = sorted(word)
value = int(value)
for i in range(1,value+1):
    for combos in combinations(word, i):
        print("".join(combos))
"""
