class Stack:
  def __init__(self):
    self.items = []
    self.size = 0
  
  def __len__(self):
    return self.size

  def push(self, item):
    self.size += 1
    self.items.append(item)
  
  def pop(self):
    if self.size == 0: return None

    self.size -= 1
    return self.items.pop()
