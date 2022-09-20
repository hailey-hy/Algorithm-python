# 종이의 개수

n = int(input())

paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

answer = dict({"-1":0, "0":0, "1":0})

def cut(start_row, start_col, size):
    num = paper[start_row][start_col]
    global answer

    if size == 1:
        answer[str(num)] += 1
        return
    
    else:
        for i in range(start_row, start_row + size):
            for j in range(start_col, start_col + size):
                if paper[i][j] != num:
                    size //= 3
                    cut(start_row, start_col, size) # 0, 0, 3 (0, 0)
                    cut(start_row + size, start_col + size, size)# 3, 3, 3 (1, 1)
                    cut(start_row + size * 2, start_col + size * 2, size) #6, 6, 3 (2, 2)
                    cut(start_row, start_col + size, size) # 0, 3, 3 (1, 0)
                    cut(start_row, start_col + size * 2, size) # 0, 6, 3 (2, 0)
                    cut(start_row + size, start_col, size) #3, 0, 3 (0, 1)
                    cut(start_row + size * 2, start_col, size) # 6, 0, 3 (0, 2)
                    cut(start_row + size, start_col + size * 2, size) # 3, 6, 3 (2, 1)
                    cut(start_row + size * 2, start_col + size, size) # 6, 3, 3 (0, 2)
                    return

                
        answer[str(num)] += 1

cut(0, 0, n)
for i in answer.values():
    print(i)