#Given comma-separated numbers, write a program to find the Mode of the given numbers.
num_list = input().split(",")
count = 0
mode = 0
for i in num_list:
    num_count = num_list.count(i)
    if num_count > count:
        count = num_count
        mode = i
print(mode)
