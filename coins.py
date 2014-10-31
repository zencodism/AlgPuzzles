def check_denomination():
    desc = raw_input()
    if desc.strip() == '':
        desc = raw_input() # just ate empty line between problems
    desc = desc.split(' ')
    n = int(desc[0])
    target = int(desc[1]) if len(desc) > 1 else 0
    target = target * target
    T = [(9001, 0, 0)] * (target + 1) # it is always named T in denomination problems. Also, it's over nine thousand!
    T[0] = (0, 0, 0) # how many coins, sum of normal value, sum of info value

    for i in range(n):
        values = raw_input().split(' ')
        for i in range(target):
            if T[i][0] != 9001:
                x = T[i][1] + int(values[0])
                y = T[i][2] + int(values[1])
                tmp = x*x + y*y
                if tmp <= target and T[i][0] + 1 < T[tmp][0]:
                    T[x*x + y*y] = (T[i][0] + 1, x, y) 

    if T[target] == 9001:
        print "not possible"
    else:
        print T[target]

t = int(raw_input())
for i in range(t):
    check_denomination()
