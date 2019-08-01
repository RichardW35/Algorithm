import sys

if __name__ == "__main__":

    def sum_of_int(s):
        sums, num, pos = 0, 0, 1
        if s == None:
            return 0
        for i in range(len(s)):
            if 48 <= ord(s[i]) <= 57:
                num = num * 10 + int(s[i]) * pos
            else:
                sums = sums + num
                num = 0
                if s[i] == '-':
                    if i > 0 and s[i - 1] == '-':
                        pos = -pos
                    else:
                        pos = -1
                else:
                    pos = 1
        sums = sums + num
        return sums

    e = sys.stdin.readline().strip()
    result = sum_of_int(e)
    print(result)
