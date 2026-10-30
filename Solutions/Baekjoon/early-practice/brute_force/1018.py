N, M = map(int,input().split())
white_ver = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
Black_ver = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

board = []
for i in range(N):
    arr = list(input())
    board.append(arr)

sum = 64
start = 0
while start <= (N*M-64):
    start_row = start//M
    start_col = start%M
    if start_row > N-8:
        start = start+1
        continue
    if start_col > M-8:
        start = start+1
        continue
    chess = [row[start_col:start_col+8] for row in board[start_row:start_row+8]]
    white_count = 0
    black_count = 0
    for i in range(8):
        for j in range(8):
            if chess[i][j] != white_ver[i][j]:
                white_count = white_count +1
            if chess[i][j] != Black_ver[i][j]:
                black_count = black_count +1
    if sum > min(white_count, black_count):
        sum = min(white_count, black_count)
    start = start+1
print(sum)

            
        
    
    