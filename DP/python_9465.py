# 스티커

n = int(input())

for i in range(n):
  stickers = []
  cnt = int(input())
  for j in range(2):
    stickers.append(list(map(int, input().split())))
  for l in range(1, cnt):
    if l == 1:
      stickers[0][l] += stickers[1][l - 1]
      stickers[1][l] += stickers[0][l - 1]
    else:
      stickers[0][l] += max(stickers[1][l - 1], stickers[1][l - 2])
      stickers[1][l] += max(stickers[0][l - 1], stickers[0][l - 2])
  print(max(stickers[0][cnt - 1], stickers[1][cnt - 1]))