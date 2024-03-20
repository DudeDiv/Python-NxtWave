#Given an integer N. Write a program to create two sets with N multiples of 2 and 3 and print the following
#  1. All the multiples of 2 but not the multiplies of 3
#  2. Uncommon multiples of 2 and 3
N = int(input())
list_1 = []
list_2 = []
for i in range(1,N+1):
    list_1.append(2*i)
    list_2.append(3*i)

list_1 = set(list_1)
list_2 = set(list_2)

multiples_of_2_but_not_3 = sorted(list_1 - list_2)
uncommon_multiples_of_2_and_3 = sorted(list_1 ^ list_2)

print(multiples_of_2_but_not_3)
print(uncommon_multiples_of_2_and_3)
