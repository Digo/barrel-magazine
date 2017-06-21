"""
    Test for LRUCache without a TTL value.
"""

import time

import pytest

import barrelmagazine

_key = 'test_key'

@pytest.fixture
def cache():
    return barrelmagazine.LRUCache(ttl=6000)

def test_invalid_get_value_no_value(cache):
    with pytest.raises(KeyError):
        cache[_key]

def test_valid_get_value(cache):
    with pytest.raises(KeyError):
        cache[_key]

    cache[_key] = 1
    assert cache[_key] == 1

def test_valid_set_value(cache):
    with pytest.raises(KeyError):
        cache[_key]

    cache[_key] = 1
    assert cache[_key] == 1

def test_invalid_del_value(cache):
    with pytest.raises(KeyError):
        del cache[_key]

def test_valid_del_value(cache):
    cache[_key] = 1
    assert cache[_key] == 1

    del cache[_key]
    with pytest.raises(KeyError):
        cache[_key]

def test_invalid_pop_no_value(cache):
    with pytest.raises(KeyError):
        cache.pop(_key)

def test_valid_pop(cache):
    cache[_key] = 1
    assert cache[_key] == 1

    assert cache.pop(_key) == 1
    with pytest.raises(KeyError):
        cache[_key]

def test_valid_out_of_space():
    cache = barrelmagazine.LRUCache(maxsize=1, ttl=6000)

    cache['1'] = 1
    assert cache['1'] == 1

    cache['2'] = 2
    assert cache['2'] == 2
    with pytest.raises(KeyError):
        cache['1']

def test_valid_timeout():
    cache = barrelmagazine.LRUCache(ttl=5)

    cache[_key] = 1
    assert cache[_key] == 1

    # Wait for timeout
    time.sleep(7)
    with pytest.raises(KeyError):
        cache[_key]
