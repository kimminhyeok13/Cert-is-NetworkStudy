height = int(input())
for i in range(height):
    for j in reversed(range(height)):
        if j > i:
            print(' ', end='')
        elif j <= i:
            print('*', end='')
    for j in range(height):
        if j < i:
            print('*', end='')
    print()
