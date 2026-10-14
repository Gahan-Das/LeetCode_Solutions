size = 0
cache = []
store = {}
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        global size
        global cache
        global store
        size = capacity
        cache[:] = []
        store.clear()
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        global store
        global cache
        # print(cache)
        if key in store:       
            cache.remove(key)
            cache.append(key)
            return store[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        global cache
        global store
        global size
        # print(cache)
        if key in store:
            cache.remove(key)
            cache.append(key) 
            store[key] = value
            return None
        if len(store) < size:
            store[key] = value
            cache.append(key)
            return None
        else:
            temp = cache.pop(0)
            try:
                store.pop(temp)
            except:
                pass
            store[key] = value
            cache.append(key)
            return None
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)