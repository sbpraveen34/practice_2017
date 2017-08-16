# def rotation(a):
#     for i in xrange(len(a)/2):
#         a[i], a[n-i-1] = a[n-i-1], a[i]
#
#
# n = int(raw_input().strip())
# a = []
# for i in xrange(n):
#     a.append(map(int, raw_input().strip().split(' ')))
#
# a = [list(i) for i in zip(*a)]
#
# rotation(a)
# print
# print
# for i in xrange(len(a)):
#     print " ".join(str(j) for j in a[i])
#

def cmpc(s1, s2):

    for i in xrange(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            return ord(s1[i]) - ord(s2[i])

    if i+1 < len(s1):
        return 1
    elif i + 1 < len(s2):
        return -1
    else:
        return 0


a = ["abc", "cad", "caa"]
a.sort(cmp=cmpc)

print a
