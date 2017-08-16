def getnextmove(n, x, y, visited):
    x1 = [  2, 1, -1, -2, -2, -1,  1,  2 ]
    y1 = [  1, 2,  2,  1, -1, -2, -2, -1 ]
    next_move = []
    for i in xrange(len(x1)):
        if -1 < x + x1[i] < n and -1 < y + y1[i] < n and not visited[x + x1[i]][y + y1[i]]:
            next_move.append((x + x1[i], y + y1[i]))
    return next_move


def solution(n):
    visited = [[0]*n for _ in xrange(n)]
    solutionutil(2, 2, visited)
    for i in visited:
        print i


def solutionutil(x, y, visited):
    next_moves = getnextmove(len(visited), x, y, visited)
    cur_val = visited[x][y]
    if not next_moves:
        all_visited = True
        for i in xrange(len(visited)):
            for j in xrange(len(visited[i])):
                if visited[i][j] == 0:
                    all_visited = False
                    break
            if not all_visited:
                break
        if not all_visited:
            return False
        else:
            return True

    # if not next_moves:
    #     print cur_val
    #     print x
    #     print y
    #     for i in visited:
    #         print i
    #     print "====================="
    #     return
    for i in next_moves:
        # print i
        # for i in visited:
        #     print i
        print "before {}".format(i)
        print cur_val + 1
        print "\n".join( str(j) for j in visited)
        visited[i[0]][i[1]] = cur_val+1
        status = solutionutil(i[0], i[1], visited)
        if status:
            print "Answer Found"
            for i in visited:
                print i
            return status
        else:
            visited[i[0]][i[1]] = 0
            print "after {}".format(i)
            print "\n".join( str(j) for j in visited)
            # import pdb; pdb.set_trace()
            # print

print solution(5)
