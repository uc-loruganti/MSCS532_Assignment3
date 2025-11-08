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

    # Universal hash function
    def _hash(self, key):
        # Universal hash function. h_ab(key) = ((a*key + b) mod p) mod table_size
        return ((self.a * key + self.b) % self.p) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        # Check if the key already exists and update
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    # Search for an entry in the hash table
    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    # Delete entry from the hash table
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

if __name__ == "__main__":
    print("Universal Hash Table Implementation")

    # Create a hash table of size 10
    hash_table = UniversalHashTable(size=10)

    # Hashing some example keys
    hash_table.insert(5, "apple")
    hash_table.insert(15, "banana")
    hash_table.insert(25, "cherry") # This might collide with 5 or 15 depending on hash function and size
    print("Search key 5:", hash_table.search(5))
    print("Search key 15:", hash_table.search(15))
    print("Search key 25:", hash_table.search(25))
    hash_table.delete(15)
    print("Search key 15 after deletion:", hash_table.search(15))