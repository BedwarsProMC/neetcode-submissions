class MyHashSet:

    def __init__(self):
        self.size = 0
        self.capacity = 8

        self.threshold = 0.75
        self.buckets = [[] for _ in range(self.capacity)]
        
    def _load_factor(self) -> int:
        return self.size / self.capacity

    def _index(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        self.capacity *= 2
        new_buckets = [[] for _ in range(self.capacity)]

        for bucket in self.buckets:
            for key in bucket:
                index = self._index(key)
                new_buckets[index].append(key)
        
        self.buckets = new_buckets

    def add(self, key: int) -> None:
        index = self._index(key)
        bucket = self.buckets[index]

        for k in bucket:
            if k == key:
                return # exists already
        
        #otherwise add it
        bucket.append(key)
        self.size += 1

        if self._load_factor() > self.threshold:
            self._resize()

    def remove(self, key: int) -> None:
        index = self._index(key)
        bucket = self.buckets[index]

        for i, k in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return
        
    def contains(self, key: int) -> bool:
        index = self._index(key)
        bucket = self.buckets[index]

        for k in bucket:
            if k == key:
                return True
        return False
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)