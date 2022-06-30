def checkWin(grid,last_move):
    r = last_move[0]
    c = last_move[1]
    for i in range(c):
        if grid[r][c] == 1:
            print("he")






grid = [[1,1,1],
        [0,0,0],
        [0,0,0]]

last_move = [0,1]
#checkWin(grid, last_move)
print(sum(grid[0]))