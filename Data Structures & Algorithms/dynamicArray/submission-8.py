import ctypes

def make_raw_block(capacity):
    """Return a contiguous block of memory with room for `capacity` references."""
    block_type = ctypes.py_object * capacity
    return block_type()

class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise Exception("capacity must be above 0")

        self.array = make_raw_block(capacity) # initialises NULL pointers
        for i in range(capacity):
            self.array[i] = None # so make None to not crash

        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # if full double size
        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        last_item = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1

        # if size is a quarter of capacity, half the capacity
        # to save memory. do at quarter not half to avoid thrashing
        # if self.size <= self.capacity // 4:
        #     # resze
        
        return last_item

    def resize(self) -> None:
        new_capacity = self.capacity * 2

        new_block = make_raw_block(new_capacity)
        for i in range(self.size):
            new_block[i] = self.array[i]

        self.array = new_block
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
