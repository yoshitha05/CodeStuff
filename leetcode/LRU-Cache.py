from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):  # Removed type hints for compatibility
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1  # Key not found
        
        # Move key to end to mark it as recently used
        self.cache[key] = self.cache.pop(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)  # Remove old entry to move it to end
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used item
        
        self.cache[key] = value  # Insert as most recently used
