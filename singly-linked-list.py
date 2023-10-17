class Singly_linked_list:
  class Node:
    def __init__(self, value, next = None):
      self.value = value
      self.next = next

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__length = 0

  def __getNode(self, get_index):
    trav = self.__head
    index = 0

    while trav:
      if index == get_index: return trav
      trav = trav.next
      index += 1
    
    return None

  def __len__(self):
    return self.__length

  def get(self, get_index):
    element = self.__getNode(get_index)
    if element is None: return None
    return element.value

  def getAll(self):
    trav = self.__head
    elements = []

    while trav:
      elements.append(trav.value)
      trav = trav.next
    
    return elements

  def append(self, value):
    node = self.Node(value)

    if self.__length == 0:
      self.__tail = node
      self.__head = node
    elif self.__length == 1:
      self.__head.next = node
      self.__tail = node
    else:
      trav = self.__getNode(self.__length - 2)

      self.__tail.next = node
      trav.next = self.__tail
      self.__tail = node
    
    self.__length += 1
  
  def unshift(self, value):
    node = self.Node(value)

    if self.__length == 0:
      self.__tail = node
      self.__head = node
    elif self.__length == 1:
      node.next = self.__tail
      self.__head = node
    else:
      node.next = self.__head
      self.__head = node
    
    self.__length += 1

  def insert(self, insert_index, insert_element):
    if insert_index < 0 or insert_index > self.__length - 1: return
    if insert_index == 0: return self.unshift(insert_element)
    if self.__length == 1: return self.append(insert_element)


    insert_node = self.Node(insert_element)
    trav1 = self.__head
    trav2 = self.__head.next
    index = 1

    while trav2:
      if index == insert_index:
        trav1.next = insert_node
        insert_node.next = trav2
        self.__length += 1
        return

      index += 1
      trav1 = trav2
      trav2 = trav2.next
  
  def removeHead(self):
    if self.__head is None: return None

    removed_element = self.__head.value
    self.__head = self.__head.next
    self.__length -= 1

    return removed_element
    
  def removeTail(self):
    if self.__tail is None: return None

    if self.__length == 1:
      removed_element = self.__tail.value
      self.__head = None
      self.__tail = None
      self.__length -= 1
      return removed_element

    removed_element = self.__tail.value
    new_tail = self.__getNode(self.__length - 2)
    new_tail.next = None
    self.__length -= 1

    return removed_element

  def removeAt(self, remove_index):
    if remove_index < 0 or remove_index > self.__length - 1: return None
    if remove_index == 0: return self.removeHead()
    if remove_index == self.__length - 1: return self.removeTail()

    trav1 = self.__head
    trav2 = self.__head.next
    index = 1

    while trav2:
      if index == remove_index:
        removed_element = trav2.value
        trav1.next = trav2.next
        self.__length -= 1
        return removed_element

      index += 1
      trav1 = trav2
      trav2 = trav2.next

    return None

  def remove(self, remove_element):
    remove_index = self.indexOf(remove_element)
    return self.removeAt(remove_index)

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
