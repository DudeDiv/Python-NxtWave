# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M = input().split()
L = '.|.'
M = int(M)
N = int(N)
print((L).center(M,'-'))
for i in range(1,int(N/2)):
    print((L+L*(i*2)).center(M,'-'))
print('WELCOME'.center(M,'-'))
for i in range(int(N/2)-1,-1,-1):
    print((L+L*(i*2)).center(M,'-'))
