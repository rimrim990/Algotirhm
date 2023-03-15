# 3-6. 동물 보호소
from collections import deque

class AnimalShelter:
  def __init__(self):
    self.animals = deque()

  def enqueue(self, animal):
    self.animals.append(animal)

  def dequeue_any(self):
    return self.animals.popleft()

  def dequeue_dog(self):
    self.animals.remove('dog')