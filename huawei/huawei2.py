def cal(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    else:
        return cal(n - 2) + 1


if __name__ == '__main__':
    while (1):
        emptybottle = int(input())
        if emptybottle != 0:
            print(cal(emptybottle))
        else:
            break
