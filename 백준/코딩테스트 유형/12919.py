# 백준 12919. A 와 B 2
s = input()
t = input()

def parse(cur, tar):
  if len(cur) == len(tar):
    return cur == tar

  ava = False
  if cur[-1] == 'A':
    ava = ava or parse(cur[:-1], tar)

  if cur[0] == 'B':
    ava = ava or parse(cur[-1:0:-1], tar)

  return ava

print(1 if parse(t, s) else 0)