import random

# Hash Table Implementation with Universal Hashing
class UniversalHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.a = random.randint(1, size - 1)
        self.b = random.randint(0, size - 1)
        self.p = self._next_prime(size)

    def _next_prime(self, n):
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        prime = n
        while not is_prime(prime):
            prime += 1
        return prime

    def _hash(self, key):
        # Universal hash function. hab(key) = ((a*key + b) mod p) mod table_size
        return ((self.a * key + self.b) % self.p) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

if __name__ == "__main__":
    print("Universal Hash Table Implementation")
    hash_table = UniversalHashTable(size=10)
    hash_table.insert(1, "one")
    hash_table.insert(2, "two")
    hash_table.insert(12, "twelve")  # Collision with key 2 if size is 10
    print("Search key 1:", hash_table.search(1))
    print("Search key 2:", hash_table.search(2))
    print("Search key 12:", hash_table.search(12))
    hash_table.delete(2)
    print("Search key 2 after deletion:", hash_table.search(2))