def palin(a, start, end):
    if start==end:
        return 1
    if start > end:
        return 0
    if a[start] == a[end]:
        return 2+palin(a, start+1, end-1)
    else:
        return max(palin(a, start, end-1), palin(a, start+1, end))

a = "BBABCBCAB"
print palin(a, 0, len(a)-1)
