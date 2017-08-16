def findend(str1, str2, pos):
    i = 0
    j = pos
    while(i < len(str2) and j < len(str1)):
        if str2[i] == str1[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(str2):
        return True, j-1
    else:
        return False, -1

def subsequence(str1, str2):
    maxlen = len(str1)
    for i in xrange(len(str1)):
        if str1[i] == str2[0]:
            result, pos = findend(str1, str2, i)
            if result:
                print "{}    {}       {}".format(i, pos, str1[i:pos+1])
                maxlen = min(maxlen, pos-i+1)
    print maxlen


str1 = "this is a test string"
str2 = "tist"

print subsequence(str1, str2)
