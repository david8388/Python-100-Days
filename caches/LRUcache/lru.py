from collections import deque


class LRUCache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.queue = deque()
        self.dict = dict()

    def is_queue_full(self):
        return len(self.queue) == self.cache_size

    def get(self, key):
        if key not in self.dict:
            return -1
        else:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.dict[key]

    def set(self, key, value):
        if key not in self.dict:
            if self.is_queue_full():
                eliminateEl = self.queue.pop()
                self.dict.pop(eliminateEl)
                self.queue.appendleft(key)
                self.dict[key] = value
            else:
                self.queue.appendleft(key)
                self.dict[key] = value


cache = LRUCache(3)

cache.set('1', 'Hello')
cache.set('2', 'world')
cache.set('3', 'Hola')
cache.set('1', 'Cisco')
cache.get('2')
cache.set('4', 'Cisco')
cache.set('5', 'IKEA')
cache.get('2')
cache.get('5')
print(cache, cache.queue)



