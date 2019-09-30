h=int(input())
for i in range(h):
    for k in range(h-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()

        
