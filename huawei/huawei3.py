while True:
    try:
        n = int(input())
        r = []
        for i in range(n):
            r.append(int(input()))
        for i in sorted(set(r)):
            print(i)
    except:
        break