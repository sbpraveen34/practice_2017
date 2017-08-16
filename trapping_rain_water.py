def retunit(a):
    curw = 1
    max1 = 0
    max2 = 0
    t = 0
    import pdb; pdb.set_trace()
    for i in a:
        if i != 0:
            if max1 == 0:
                max1 = i
            elif max1 != 0 and max2 == 0:
                max2 = i
                t += curw* min(max1, max2)
                max1 = 0
                max2 = 0
                curw = 1
                max1 = i
        elif i == 0 and max1 != 0:
            curw +=1

    print t
    return t

retunit([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
