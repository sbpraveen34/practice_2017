def insertionSort(ar):
    e = ar[-1]
    for i in xrange(len(ar)-2, -1, -1):
        if ar[i] > e:
            ar[i+1] = ar[i]
        else:
            ar[i+1] = e
            print " ".join([str(a) for a in ar])
            break
        print " ".join([str(a) for a in ar])

        if i == 0:
            ar[i] = e
            print " ".join([str(a) for a in ar])


    return ""

insertionSort([1,2,3,4,5,7,8,9,10,10])
