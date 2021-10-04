def solution(game_board, table):
    answer = -1
    for i in range(len(game_board)):
        print(game_board[i])
    print ('------')
    for j in range(len(table)):
        print(table[j])
    return answer
game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
ans = solution(game_board,table)
print(ans)