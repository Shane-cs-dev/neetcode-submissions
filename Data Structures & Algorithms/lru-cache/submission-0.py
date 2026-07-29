from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        # If the key is not in the dict
        if key not in self.cache:
            return -1
        # If the key is available in the dict
        # Udpate the dict order
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If the key is available in the dict
        if key in self.cache:
            # Update the dict order for this pair
            self.cache.move_to_end(key)
        # Update the value
        self.cache[key] = value
        
        # If the size if higher than capacity
        if len(self.cache) > self.cap:
            self.cache.popitem(last = False) # This should be FIFO