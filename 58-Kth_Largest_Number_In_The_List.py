#Write a program to print the Kth largest number in the list.
string = input()
K = int(input())
string_list = string.split(",")
for i in range(len(string_list)):
    string_list[i] = int(string_list[i])
string_list = sorted(string_list)
kth_largest = string_list[-K]
print(kth_largest)
