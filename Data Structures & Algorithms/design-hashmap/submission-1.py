class MyHashMap:
    # collision management: chaining

    def __init__(self):
        self.size = 0
        self.capacity = 8

        self.threshold = 0.75 # resizes when load factor > threshold

        self.buckets = [[] for _ in range(self.capacity)] # indexes 0 - 7

    def _index(self, key: int) -> int:
        # hashes key and compresses to capacity bounds to get bucket index
        return hash(key) % self.capacity

    def put(self, key: int, value: int) -> None:
        index = self._index(key)

        bucket = self.buckets[index]
        for pair in bucket: # cant extract k,v here as reassinging v wont work
            if pair[0] == key:
                pair[1] = value #update value
                return

        # otherwise insert it.
        bucket.append([key, value])
        self.size += 1

        if self._load_factor() > self.threshold:
            self._resize()
        
    def get(self, key: int) -> int:
        index = self._index(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        index = self._index(key)
        bucket = self.buckets[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                self.size -=1
                return
    
    
    def _resize(self) -> None:
        # doubles number of buckets when load factor > threshold
        self.capacity *= 2
        new_buckets = [[] for _ in range(self.capacity)]

        # rehash existing keys and move to new buckets
        for bucket in self.buckets:
            for key, value in bucket:
                new_index = self._index(key)
                new_buckets[new_index].append([key, value])
        
        self.buckets = new_buckets

    def _load_factor(self) -> float:
        return self.size / self.capacity
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)