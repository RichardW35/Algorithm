while True:
    try:
        ip1 = list(map(int, input().split(".")))
        ip2 = list(map(int, input().split(".")))
        mask = list(map(int, input().split(".")))
        ip_res = []
        flag = 1
        for i in range(4):
            ip_res.append(ip1[i] & mask[i])
            if ip1[i] & mask[i] != ip2[i] & mask[i]:
                flag = 0
        print("{0} {1}.{2}.{3}.{4}".format(flag, ip_res[0], ip_res[1],
                                           ip_res[2], ip_res[3]))

    except:
        break
