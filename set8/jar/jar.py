class Jar:
    def __init__(self, capacity: int = 12):
        self.capacity = capacity
        self._size = 0  # By default the number of cookies is 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n: int):
        if n < 0:  # By the meaning, we can't deposit a negative number of cookies
            raise ValueError("Not a valid number!")
        self.size += n

    def withdraw(self, n: int):
        if n < 0: # By the meaning, we can't withdraw a negative number of cookies
            raise ValueError("Not a valid number!")
        self.size -= n


    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter  # We could put this capacity.setter in the __init__. As we have use the getter, we need the setter as well
    def capacity(self, capacity: int):
        if int(capacity) <= 0:
            raise ValueError("Not a valid capacity!")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size: int = 0):
        if (size < 0) or (size > self.capacity): # Check for valid number of cookies in the jar
            raise ValueError("Not a valid number!")
        self._size = size

jar=Jar(20)
jar.withdraw(5)