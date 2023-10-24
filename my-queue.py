class Queue:
  def __init__(self):
    self.list = []
  
  def __len__(self):
    return len(self.list)
  
  def is_empty(self):
    return len(self.list) == 0

  def peek(self):
    if self.is_empty(): return None
    return self.list[-1]

  def enqueue(self, item):
    self.list.append(item)
  
  def dequeue(self):
    if self.is_empty(): return None
    return self.list.pop(0)
