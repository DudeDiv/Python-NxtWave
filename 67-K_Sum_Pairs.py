#Write a program that reads comma-separated numbers and the number K and then finds all the unique pairs in the given numbers whose sum is equal to K.
def convert(i):
    new_list = []
    for each in i:
        each = int(each)
        new_list.append(each)
    return new_list

def get_unique_pairs(integers_list, K):
    unique_pairs_set = set()
    stop_index = len(integers_list) - 1
    for cur_index in range(stop_index):
        num1 = integers_list[cur_index]
        num2 = K - num1
        remaining_list = integers_list[cur_index+1:]
        if num2 in remaining_list:
            pair = (num1, num2)
            sorted_pair = tuple(sorted(pair))
            unique_pairs_set.add(sorted_pair)
    return unique_pairs_set
    
integers = input().split(",")
K = int(input())
integers_list = convert(integers)
unique_pairs = get_unique_pairs(integers_list, K)
unique_pairs = list(unique_pairs)
unique_pairs.sort()
for pairs in unique_pairs:
    print(pairs)
