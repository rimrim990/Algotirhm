def solution(words):
  trie = Trie()
  for word in words:
    trie.make_tree(word)

  answer = 0
  for word in words:
    answer += trie.count(word)

  return answer

class Trie:
  def __init__(self):
    self.trie = {}

  def count(self, word):
    ptr = self.trie
    for i in range(len(word)):
      if ptr[word[i]][1] == 1:
        return i+1

      ptr = ptr[word[i]][0]

    return len(word)


  def make_tree(self, word):
    ptr = self.trie
    for w in word:
      if w not in ptr:
        ptr[w] = [{}, 0]

      ptr[w][1] += 1
      ptr = ptr[w][0]