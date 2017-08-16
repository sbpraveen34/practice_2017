import sys
val = {}
val[0] = 0
val[1] = 1
def cal(n):
    if n in val:
        return val[n]
    else:
        val[n] = max(n, (cal(n/2) + cal(n/3) + cal(n/4)) )
        return val[n]
while(True):
    r = sys.stdin.readline()
    r = r.strip()
    if r:
        r = int(r)
        if r < 5:
            print r
            continue
        if r in val:
            print val[r]
        else:
            print cal(r)
    else:
        break;
