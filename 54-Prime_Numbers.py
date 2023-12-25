#A function is given in the prefilled code that takes a number N as an argument.
#Write a program that returns all the prime numbers from 1 to N separated by a space.
def is_prime(n):
    if(n == 1 or n == 0):
        return False
        
    for i in range(2, n):
        if(n % i == 0):
            return False
            
    return True
 
n = int(input())
prime_numbers_list = []

for i in range(1, n + 1):
    if(is_prime(i)):
        prime_numbers_list.append(str(i))

prime_numbers_separated_by_spaces = " ".join(prime_numbers_list)
print(prime_numbers_separated_by_spaces)


#((OR))

