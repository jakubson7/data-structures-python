class Doubly_linked_list:
  class Node:
    def __init__(self, value, previous=None, next=None):
      self.value = value
      self.previous = previous
      self.next = next
  
  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__length = 0
  
  def __len__(self):
    return self.__length

  def get(self, get_index):
    trav = self.__head
    index = 0

    while trav:
      if index == get_index: return trav.value
      trav = trav.next
      index += 1
    
    return None

  def getAll(self):
    elements = []
    trav = self.__head

    while trav:
      elements.append(trav.value)
      trav = trav.next
    
    return elements

  def append(self, element):
    if self.__length == 0:
      self.__head = self.__tail = self.Node(element)
    else:
      self.__tail.next = self.Node(element, previous = self.__tail)
      self.__tail = self.__tail.next

    self.__length += 1

  def unshift(self, element):
    if self.__length == 0:
      self.__head = element
      self.__tail = element
    else:
      self.__head.previous = self.Node(element, next = self.__head)
      self.__head = self.__head.previous

    self.__length += 1

  def removeHead(self):
    if not self.__head: return None

    value = self.__head.value
    self.__head = self.__head.next
    self.__length -= 1

    if self.__length == 0: self.__tail = None
    else: self.__head.previous = None

    return value

  def removeTail(self):
    if not self.__tail: return None

    value = self.__tail
    self.__tail = self.__tail.previous
    self.__length -= 1

    if self.__length == 0: self.__head = None
    else: self.__tail.next = None

    return value

  def removeAt(self, remove_index):
    if remove_index < 0 or remove_index > self.__length - 1: return None
    if remove_index == 0: return self.removeHead()
    if remove_index == self.__length - 1: return self.removeTail()

    trav = self.__head
    index = 0

    while trav:
      if remove_index == index:
        trav.previous.next = trav.next
        trav.next.previous = trav.previous

        self.__length -= 1
        return trav.value

      trav = trav.next
      index += 1

    return None

  def remove(self, element):
    trav = self.__head
    index = 0

    while trav:
      if trav.value == element:
        return self.removeAt(index)

      trav = trav.next
      index += 1
    
    return None

  def indexOf(self, element):
    trav = self.__head
    index = 0

    while trav:
      if trav.value == element: return index

      trav = trav.next
      index += 1

    return -1

  def contains(self, element):
    return self.indexOf(element) != -1
