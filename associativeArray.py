class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
         index = len(key) % self.size
         self.values[index] = key
         return index

    def is_key(self, key):
        for i in range(self.size):
            if self.values[i] == key:
                return True

        return False

    def put(self, key, value):
        index = self.hash_fun(key)
        self.slots[index] = value


    def get(self, key):
        for i in range(self.size):
            if self.values[i] == key:
                return self.slots[i]

        return None

aa = NativeDictionary(4)
print(aa)
print(aa.hash_fun("sddddddddddddd"))

print(8 % 4)

aa.put("star", 1)
aa.put("s", 2)
aa.put("sta", 4)
aa.put("st", 3)
aa.put("sfa", 34)

print("is key", aa.is_key("star"))

print("get", aa.get("starf"))

print(aa.slots)
print(aa.values)