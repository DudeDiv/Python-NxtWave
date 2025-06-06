from itertools import permutations
line = input().split()
string = line[0].upper()
int_val = int(line[1])
X = sorted(permutations(string, int_val))
for i in X:
    print("".join(i))
