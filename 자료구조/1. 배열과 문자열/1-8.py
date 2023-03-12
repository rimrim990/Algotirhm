# 1-8. 0 행렬 - O(N^2)

def solution(matrix):
  # 0 인 원소 탐색
  row = -1; col = -1;
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 0:
        row = i; col = j;
        break
    if row != -1 and col != -1:
      break

  # 행과 열의 모든 원소를 0으로 설정
  for i in range(len(matrix)):
    matrix[i][col] = 0

  for j in range(len(matrix[0])):
    matrix[row][j] = 0

  return matrix