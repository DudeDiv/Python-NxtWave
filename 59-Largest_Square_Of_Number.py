#A function is given in the prefilled code that takes a list L as an argument.
#Write a program to find the largest of the squares of the numbers in the list L using recursion.
def get_largest_square(numbers):
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])*int(numbers[i])
    numbers = sorted(numbers)
    return max(numbers)

numbers = input().split()

result = get_largest_square(numbers)
print(result)
