#A function is given in the prefilled code that takes two numbers M and N as arguments.
#Write a program that returns all the prime numbers from M to N separated by a space.
def check_is_prime(m, n):
    prime_numbers_list = []
    for i in range(m,n+1):
        flag = False
        if(i==0 or i==1):
            flag = True
        for j in range(2,i):
            if(i%j==0):
                flag = True
                break
        if(flag == False):
            prime_numbers_list.append(str(i))
    prime_numbers_list = " ".join(prime_numbers_list)
    return prime_numbers_list
    
m = int(input())
n = int(input())
prime_numbers  = check_is_prime(m,n)
print(prime_numbers)
