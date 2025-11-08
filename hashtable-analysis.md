# Analysis of Hash Table Performance

This document analyzes the performance of hash tables, focusing on the impact of the load factor and strategies for collision resolution, with direct references to the `hashtable_universalhash.py` implementation.

### Performance under Simple Uniform Hashing

The **Simple Uniform Hashing Assumption (SUHA)** states that each key is equally likely to hash into any of the available slots. Under this assumption, the performance of hash table operations using chaining is determined by the **load factor (α)**, where α = n / m (n = number of elements, m = number of slots).

- **Expected Search, Insert, and Delete Time:** The time for these operations is proportional to the length of the chain being operated on. On average, this is O(1 + α).

This theoretical complexity is demonstrated in the `insert`, `search`, and `delete` methods of the `UniversalHashTable` class. Each method first calculates a hash index and then iterates through the list at that index.

```python

def search(self, key):
    index = self._hash(key)
    # This loop's length is proportional to the load factor
    for k, v in self.table[index]:
        if k == key:
            return v
    return None
```

### The Role of the Load Factor (α)

The load factor is the most critical parameter for performance. As α increases, the average chain length grows, and performance degrades. If we can ensure α remains bounded by a constant, the expected time for all operations remains O(1).

The implementation in `hashtable_universalhash.py` uses a fixed-size table. This means that as more elements are inserted, the load factor `n/m` will grow without bound, and performance will eventually degrade towards O(n).

### Strategies for Maintaining Performance

#### 1. Using a Good Hash Function

A good hash function distributes keys uniformly. The script implements **universal hashing**, a robust technique that provides strong performance guarantees. This is implemented in the `__init__` and `_hash` methods.

- **Initialization**: In the `__init__` method, a prime number `p` (larger than the table size) is found, and random integers `a` and `b` are chosen. These are the parameters for the universal hash function family.

```python
# From hashtable_universalhash.py

def __init__(self, size):
    self.size = size
    self.table = [[] for _ in range(size)]
    self.a = random.randint(1, size - 1)
    self.b = random.randint(0, size - 1)
    self.p = self._next_prime(size)
```

- **Hashing**: The `_hash` method applies the universal hash function `h(k) = ((a*k + b) mod p) mod m`, which ensures a low probability of collision for any two distinct keys.

```python
# From hashtable_universalhash.py

def _hash(self, key):
    # Universal hash function. h_ab(key) = ((a*key + b) mod p) mod table_size
    return ((self.a * key + self.b) % self.p) % self.size
```

#### 2. Dynamic Resizing (Rehashing)

This is the standard strategy for keeping the load factor low. When α exceeds a threshold, a new, larger table is created, and all elements are re-hashed into it.

_**Note:** The current implementation in `hashtable_universalhash.py` does not include dynamic resizing. The table size is fixed upon creation. In a real-world application, its performance would degrade as the number of elements grows significantly larger than the initial size._ 