def check_denomination():
    desc = raw_input()
    if desc.strip() == '':
        desc = raw_input() # just ate empty line between problems
    desc = desc.split(' ')
    n = int(desc[0])
    target = int(desc[1]) if len(desc) > 1 else 0
    target = target * target
    T = [(90001, 0, 0)] * (target + 1) # it is always named T in denomination problems. Also, it's over nine thousand!
    T[0] = (0, 0, 0) # how many coins, sum of normal value, sum of info value

    for i in range(n):
        values = raw_input().split(' ')
        x = int(values[0])
        y = int(values[1])
        tmp = x*x + y*y
        X = x
        Y = y
        for i in range(target):
            if T[i][0] != 90001:
                x = X + T[i][1]
                y = Y + T[i][2]
                tmp = x*x + y*y
                if tmp <= target and T[i][0] + 1 < T[tmp][0]:
                    T[tmp] = (T[i][0] + 1, x, y) 
    if T[target][0] == 90001:
        print "not possible"
    else:
        print T[target][0]

t = int(raw_input())
for i in range(t):
    check_denomination()
