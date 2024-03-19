#Given two lines of comma-separated integers, write a program to print the numbers that are present in both of the lines.
def convert_string_to_int(num_list):
    new_list = []
    for each_num in num_list:
        each_num = int(each_num)
        new_list.append(each_num)
    return new_list
list_1 = input().split(",")
list_2 = input().split(",")

list_1 = convert_string_to_int(list_1)
list_2 = convert_string_to_int(list_2)

set_a = set(list_1)
set_b = set(list_2)

operated_list = sorted(set_a & set_b)
print(operated_list)
