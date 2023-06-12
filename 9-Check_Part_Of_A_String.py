#Write a program that reads two words A, B, and an index I. Check if B starts at index I in A.
A = input()
B = input()
I = int(input())
B_len = len(B)
print(B==A[I:(I+B_len)])
