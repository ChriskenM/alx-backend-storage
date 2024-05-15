#!/usr/bin/env python3

import redis
import requests
from typing import Callable
from functools import wraps

# Initialize Redis client
r = redis.Redis()

def count_access(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(url: str) -> str:
        # Increment the count for the URL
        count_key = f"count:{url}"
        r.incr(count_key)
        return method(url)
    return wrapper

def cache_result(expiration: int = 10) -> Callable:
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(url: str) -> str:
            # Check if the result is already cached
            cache_key = f"cache:{url}"
            cached_result = r.get(cache_key)
            if cached_result:
                return cached_result.decode('utf-8')

            # Call the original function and cache the result
            result = method(url)
            r.setex(cache_key, expiration, result)
            return result
        return wrapper
    return decorator

@count_access
@cache_result(expiration=10)
def get_page(url: str) -> str:
    """Fetch the HTML content of a URL and return it as a string."""
    response = requests.get(url)
    return response.text

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://www.example.com"
    print(get_page(url))
    print(get_page(url))  # This should be faster if called within 10 seconds

