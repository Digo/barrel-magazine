####################
Barrel Magazine
####################

A thread-safe LRU cache for Python.

Usage
=====

The cache uses no timeout if the `ttl` value is less than 1.

.. code-block:: python

    import barrelmagazine

    # No time-to-live/timeout
    cache = barrelmagazine.LRUCache()

    cache['key'] = 'value'  # Add to cache.
    assert cache['key'] == 'value'  # Get from cache.
    del cache['key']   # Removed from the cache.

    try:
        cache['key']
    except KeyError:
        # Key not in the cache.
        pass

The value of `ttl` represents the timeout in seconds.

.. code-block:: python

    import time
    import barrelmagazine

    # 60 seconds timeout
    cache = barrelmagazine.LRUCache(ttl=60)

    cache['key'] = 'value'  # Add to cache.
    assert cache['key'] == 'value'  # Get from cache.
    time.sleep(65)

    try:
        cache['key']
    except KeyError:
        # Key not in the cache.
        pass
