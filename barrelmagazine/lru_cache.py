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

    def __getitem__(self, key):
        with self._lock:
            return self._cache[key]

    def __setitem__(self, key, item):
        with self._lock:
            self._cache[key] = item

    def __delitem__(self, key):
        with self._lock:
            self._cache.pop(key)
