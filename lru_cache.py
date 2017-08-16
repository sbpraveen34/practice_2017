class LRUCache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache_list = []
        self.cache = {}

    def insert_into_cache(key, value):
        if key in self.cache:
            return False
        self.cache[key] = value
        self.cache_list.insert(0, key)
        if len(self.cache_list) > self.cache_size:
            last_key = self.cache_list.pop()
            del self.cache[key]


    def search_cache(key):
        if key in self.cache:
            self.cache_list.remove(key)
            self.cache_list.insert(0, key)
