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

def solution_using_trie(words, queries):
  trie = Trie()
  rtrie = Trie()
  for word in words:
    trie.gen_tree(word)
    rtrie.gen_tree(word[::-1])

  answer = []
  for q in queries:
    key = q.replace('?', '')
    if q[-1] == '?':
      answer.append(trie.count_key(key, len(q)))
    else:
      answer.append(rtrie.count_key(key[::-1], len(q)))

  return answer

class Trie:
  N = 10_001

  def __init__(self):
    self.trie = [{'': [{}, 0]} for _ in range(self.N)]

  def count_key(self, key, n):
    if key == '':
      return self.trie[n][''][1]

    ptr = self.trie[n][''][0]
    for i in range(len(key)):
      if key[i] not in ptr:
        return 0

      if i == len(key)-1:
        return ptr[key[i]][1]

      ptr = ptr[key[i]][0]

  def gen_tree(self, word):
    n = len(word)
    self.trie[n][''][1] += 1
    ptr = self.trie[n][''][0]

    for i in range(n):
      key = word[i]

      if key not in ptr:
        ptr[key] = [{}, 0]

      ptr[key][1] += 1
      ptr = ptr[key][0]