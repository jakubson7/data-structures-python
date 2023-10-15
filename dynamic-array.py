class Dynamic_array:
    def __init__(self, capacity = 16):
        if capacity < 1: capacity = 1

        self.__length = 0
        self.__capacity = capacity
        self.__array = [None] * capacity

    def get(self, index):
        return self.__array[index]
    
    def gatAll(self):
        return self.__array

    def clear(self):
        for i in range(0, self.__capacity):
            self.__array[i] = None
        
        self.__length = 0

    def add(self, element):
        if self.__length + 1 >= self.__capacity:
            self.__capacity *= 2
            new_array = [None] * self.__capacity

            for index, e in enumerate(self.__array):
                new_array[index] = e
            self.__array = new_array

        self.__array[self.__length] = element
        self.__length += 1

    def removeAt(self, remove_index):
        if remove_index < 0 or remove_index > self.__length: return

        new_array = [None] * self.__capacity
        for index, element in enumerate(self.__array):
            if index != remove_index: new_array.append(element)

        self.__array = new_array
        self.__len -= 1

    def indexOf(self, index_element):
        for index, element in enumerate(self.__array):
            if element == index_element: return index

        return -1

    def remove(self, remove_element):
        remove_index = self.indexOf(remove_element)
        if remove_index == -1: return
        self.removeAt(remove_index)
    
    def contains(self, element):
        return self.indexof(element) != -1


    def __len__(self):
        return self.__length

