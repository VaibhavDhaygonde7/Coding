import time
from functools import lru_cache

print("How many values do you want to cache")
cache = int(input())

@lru_cache(maxsize=cache)
def squrt(n):
    time.sleep(3)
    return n * n

if __name__ == "__main__":
    print("Enter number 1")
    n1 = int(input())
    print(squrt(n1))
    print("Enter number 2")
    n2 = int(input())
    print(squrt(n2))