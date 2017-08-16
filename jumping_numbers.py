s = set()

def get_next_numbers(c, n):
    if c > n:
        return
    if c in s:
        return
    s.add(c)
    if c%10 == 0:
        c = c*10 + 1
        get_next_numbers(c, n)
        return
    elif c%10 == 9:
        c = c*10 + 8
        get_next_numbers(c, n)
        return
    else:
        d = c
        c = c*10 + (c%10) + 1
        get_next_numbers(c, n)
        d = d*10 + (d%10) - 1
        get_next_numbers(d, n)
        return
s.add(0)
abc = 105
get_next_numbers(1, abc)
get_next_numbers(2, abc)
get_next_numbers(3, abc)
get_next_numbers(4, abc)
get_next_numbers(5, abc)
get_next_numbers(6, abc)
get_next_numbers(7, abc)
get_next_numbers(8, abc)
get_next_numbers(9, abc)
print s
