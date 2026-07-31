class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Key: key, Value: [frequency, value, timestamp]
        self.timestamp = 0

    def get(self, key: int) -> int:
        # If the key is not available in the cache
        if key not in self.cache:
            return -1
        
        # Update the frequency
        self.cache[key][0] += 1

        # Udpate timestamp
        self.timestamp += 1
        self.cache[key][2] = self.timestamp

        return self.cache[key][1]

    def put(self, key: int, value: int) -> None:
        # Corner case:
        if self.cap == 0:
            return
        
        # If the key already exists in the dict
        # Upadate it
        self.timestamp += 1
        if key in self.cache:
            self.cache[key][0] += 1
            self.cache[key][1] = value
            self.cache[key][2] = self.timestamp
            return 
        
        # If this is a new key and exceed the length of the dict
        if len(self.cache) == self.cap:
            del self.cache[self.findleastFreqUsed()]
        
        # Add new data into the cache
        self.cache[key] = [1, value, self.timestamp]
        return 
            

    
    def findleastFreqUsed(self) -> int:
        least_used = None
        min_freq = float('inf')
        min_time = float('inf')

        # Loop through all items to find the least used data
        for k, (freq, val, time) in self.cache.items():
            # Comparison
            if freq < min_freq or (freq == min_freq and time < min_time):
                # Udpate the value
                min_freq = freq
                min_time = time
                least_used = k
        return least_used


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)