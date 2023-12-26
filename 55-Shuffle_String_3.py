#A function is given in the prefilled code that takes a string S and N space-separated indices as an argument.
#Write a program that prints a string by joining characters present at each index of the given N indices.
def shuffle_string(string, indices_list):
    S = ""
    indices_list = indices_list.split()
    for i in indices_list:
        i = int(i)
        S = S + string[i]
    return S

string = input()
indices_list = input()

result = shuffle_string(string,indices_list)
print(result)
