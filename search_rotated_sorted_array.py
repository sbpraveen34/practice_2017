def search_array(a):
    start = 0
    stop = len(a)-1

    while(start < stop):
        import pdb; pdb.set_trace()
        mid = (start + stop)/2
        print "start {}  ===  stop {} === mid {}".format(start, stop, mid)
        print "start {}  ===  stop {} === mid {}".format(a[start], a[stop], a[mid])
        if  a[mid-1] > a[mid] < a[mid+1]:
            print a[mid]
            break
        else:
            if a[mid-1] > a[mid] > a[mid+1]:
                stop = mid
            else:
                start = mid


a = [1, 2, 3, 4]

print search_array(a)
