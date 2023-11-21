from bisect import bisect_left, bisect_right

def solution(words, queries):
  words = [(len(w), w) for w in words]
  words.sort()
  rwords = [(sz, w[::-1]) for sz, w in words]
  rwords.sort()

  answer = []
  for q in queries:
    start = q.replace('?', 'a')
    end = q.replace('?', 'z')

    tar = words;
    if q.startswith('?'):
      tar = rwords
      start = start[::-1]
      end = end[::-1]

    left = bisect_left(tar, (len(q), start))
    right = bisect_right(tar, (len(q), end))
    answer.append(right-left)

  return answer