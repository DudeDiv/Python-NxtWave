if __name__ == '__main__':
    N = int(input())
    list1 = []
    for i in range(N):
        operation = input().split()
        if(operation[0]=='insert'):
            list1.insert(int(operation[1]),int(operation[2]))
        if(operation[0]=='print'):
            print(list1)
        if(operation[0]=='remove'):
            list1.remove(int(operation[1]))
        if(operation[0]=='append'):
            list1.append(int(operation[1]))
        if(operation[0]=='sort'):
            list1.sort()
        if(operation[0]=='pop'):
            list1.pop()
        if(operation[0]=='reverse'):
            list1.reverse()
