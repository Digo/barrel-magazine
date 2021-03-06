"""
    A thread-safe LRU Cache implementation.
"""

import threading

import cachetools

class LRUCache:
    """
        A thread-safe LRU Cache implementation.
    """
    def __init__(self, maxsize=1000, ttl=0):
        # If TTL is set (e.g. the ttl value is greater than zero), use the TTLCache, otherwise
        # use the LRUCache.
        self._cache = cachetools.TTLCache(maxsize, ttl=ttl) if ttl > 0 else cachetools.LRUCache(maxsize)
        self._lock = threading.Lock()

    def pop(self, key):
        """
            Pops the value associated with the key from the cache.

            PARAMETERS:

            key - the key to pop.
        """
        with self._lock:
            return self._cache.pop(key)

    def __contains__(self, item):
        with self._lock:
            return item in self._cache

    def __getitem__(self, key):
        with self._lock:
            return self._cache[key]

    def __setitem__(self, key, item):
        with self._lock:
            self._cache[key] = item

    def __delitem__(self, key):
        with self._lock:
            self._cache.pop(key)
