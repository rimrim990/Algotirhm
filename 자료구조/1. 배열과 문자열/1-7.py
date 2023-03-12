# 1-7. 행렬 회전 - O(N)

def solution(img):
  # NxN 행렬 크기
  N = len(img)
  # 90 도 회전된 이미지 행렬
  rotated = [[0 for _ in range(N)] for _ in range(N)]

  for i in range(N):
    for j in range(N):
      rotated[i][j] = img[N-j-1][i]

  return rotated

# 행렬을 추가로 사용하지 않고 회전
def solution_without_matrix(img):
  pass