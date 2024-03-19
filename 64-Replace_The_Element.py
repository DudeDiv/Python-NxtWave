#For this problem, the prefilled code will contain a list of tuples. Write a program to replace the last number of each tuple in the list with the given number (N).
num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
N = int(input())
new_list = []
for tuple_a in num_list:
    updated_table = tuple_a[:-1] + (N,)
    new_list.append(updated_table)
print(new_list)
