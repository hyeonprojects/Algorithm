# Hash Table
class HashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]

    def getKey(self, data):
        self.key = ord(data[0])
        return self.key

    def hashFunction(self, key):
        return key % self.size

    def getAddress(self, key):
        myKey = self.getKey(key)
        hash_address = self.hashFunction(myKey)
        return hash_address

    def save(self, key, value):
        hash_address = self.getAddress(key)
        self.hash_table[hash_address] = value

    def read(self, key):
        hash_address = self.getAddress(key)
        return self.hash_table[hash_address]

    def delete(self, key):
        hash_address = self.getAddress(key)

        if self.hash_table[hash_address] != 0:
            self.hash_table[hash_address] = 0
            return True
        else:
            return False