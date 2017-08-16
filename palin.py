import sys

def get_next_palin(f, l):
    if l%2 == 0:
        j = l/2
        carry = 0
        fi = []
        if f[l/2] == '9':
            carry = 1
            fi.append('0')
            fi.append('0')
        else:
            fi.append(str(int(f[l/2]) + 1))
            fi.append(str(int(f[l/2]) + 1))

        for i in xrange(l/2 -2, -1, -1):
            digit = f[i]
            if carry:
                if digit == '9':
                    digit = '0'
                else:
                    digit = str(int(digit) + 1)
                    carry = 0
            fi.insert(0, digit)
            fi.append(digit)

        if carry:
            fi.insert(0, '1')
            fi[-1] = '1'
    else:
        fi = []
        carry = 0
        if f[l/2] == '9':
            carry = 1
            fi.append('0')
        else:
            fi.append(str(int(f[l/2]) + 1))

        for i in xrange(l/2-1, -1, -1):
            digit = f[i]
            if carry:
                if digit == '9':
                    digit = '0'
                else:
                    digit = str(int(digit) + 1)
                    carry = 0
            fi.insert(0, digit)
            fi.append(digit)
        if carry:
            fi.insert(0, '1')
            fi[-1] = '1'
    return ''.join(fi)

t = int(sys.stdin.readline().strip())
for _ in xrange(0, t):
    a = sys.stdin.readline().strip()
    l = len(a)
    if l > 1:
        if l%2 == 0:
            f = a[0:l/2]+ ''.join(reversed((a[0:l/2])))
        else:
            f = a[0:l/2] + a[l/2] + ''.join(reversed((a[0:l/2])))

        if (int(f)) > (int(a)):
            print f
        else:
            print get_next_palin(f, len(f))
    else:
        print a
