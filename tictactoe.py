import sys

def get_diagonal_elements(n):
    d1 = []
    d2 = []
    for i in xrange(n):
        d1.append((i, i))
        d2.append((n-i-1, i))
    return set(d1), set(d2)

n = 3
a = [[None]*n  for _ in xrange(n)]
p1 = None
p2 = None
d1, d2 = get_diagonal_elements(n)


def check_row(grid, player_type, current_position):
    for row_id in xrange(len(grid)):
        if grid[row_id][current_position.y] != player_type:
            return False

    return True

def check_column(grid, player_type, current_position):
    for column_id in xrange(len(grid)):
        if grid[current_position.x][column_id] != player_type:
            return False

    return True

def check_main_diagonal(grid, player_type, current_position):


def check_winner(a, ch, i, j):

    is_found_in_main_d = False
    if (i, j) in d1:
        is_found_in_main_d = True
        for k in d1:
            if a[k[0]][k[1]] != ch:
                is_found_in_main_d = False

    is_found_in_s_d = False
    if (i, j) in d2:
        is_found_in_s_d = True
        for k in d2:
            if a[k[0]][k[1]] != ch:
                is_found_in_s_d = False
    return check_row(a, ch, ) or is_found_in_column or is_found_in_main_d or is_found_in_s_d



print "Player 1 Input"
p1 = sys.stdin.readline().strip()
print "Player 2 Input"
p2 = sys.stdin.readline().strip()
print "Game Starts Now"
while(True):

    print "Player 1 Position please"
    i, j = map(int, sys.stdin.readline().strip().split(' '))
    a[i][j] = p1
    if check_winner(a, p1, i, j):
        print "Player 1 has won"
        # for i in
        break
    print "Player 2 Position please"
    i, j = map(int, sys.stdin.readline().strip().split(' '))
    a[i][j] = p2
    if check_winner(a, p2, i, j):
        print "Player 2 has won"
        break
