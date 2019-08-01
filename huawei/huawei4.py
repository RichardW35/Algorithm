while True:
    try:
        N, M = map(int, input().split())
        score = list(map(int, input().split()))
        op = []
        for i in range(M):
            op1 = input().split()
            op.append(op1)
        for i in range(M):
            if op[i][0] == 'Q':
                a, b = min(int(op[i][1]), int(op[i][2])), max(
                    int(op[i][1]), int(op[i][2]))
                print(max(score[a - 1:b]))
            elif op[i][0] == 'U':
                score[int(op[i][1]) - 1] = int(op[i][2])
    except:
        break

##输入包括多组测试数据。
##每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。生ID编号从1编到N。
##第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
##接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少
##当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。