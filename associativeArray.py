class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
         index = len(key) % self.size
         return index

    def is_key(self, key):
        for i in range(self.size):
            print("i", i)
            if self.values[i] == key:
                return True

        return False

    def put(self, key, value):
        index = self.hash_fun(key)
        self.slots[index] = value
        self.values[index] = key

    def get(self, key):
        for i in range(self.size):
            if self.values[i] == key:
                return self.slots[i]

        return None
