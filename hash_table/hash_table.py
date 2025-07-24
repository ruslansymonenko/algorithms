class HashTable:
    def __init__(self, size=16):
        self.table = [[] for _ in range(size)]
        self.size = size
    
    def _hash(self, key):
        return sum(ord(char) for char in key) % self.size
    
    def set(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        self.table[index] = [(k, v) for k, v in bucket if k != key]



ht = HashTable()

ht.set("apple", "123")
ht.set("orange", "456")

print(ht.get("orange"))

