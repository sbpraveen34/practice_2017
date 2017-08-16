a = [ [1, 2, 3],
        [4, 8, 2],
[1, 5, 3] ]

m = len(a)
n = len(a[0])
t = [ [None]*n for _ in xrange(m)]
print a
print t


def min_path_sum(a, m, n):
    if m < 0 or n < 0:
        return 999999999999999
    if m ==0  and n ==0:
        return a[0][0]

    if t[m][n]:
        return t[m][n]

    t[m][n] = min(min_path_sum(a, m-1, n), min_path_sum(a, m, n-1), min_path_sum(a, m-1, n-1)) + a[m][n]

    return t[m][n]


print min_path_sum(a, m-1, n-1)

print t
