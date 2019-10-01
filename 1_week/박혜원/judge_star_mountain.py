h = int(input())
n = h*2-1
#가로 개수는 h*2-1이 됨

for i in range(h):
    for j in range(n):
        if j < n//2 - i:
            print(' ', end = '')
        elif n//2 -i <= j < n - n//2 +i:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
