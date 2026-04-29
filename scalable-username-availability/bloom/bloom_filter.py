import mmh3 # type: ignore
from bitarray import bitarray # type: ignore

class BloomFilter:
    """
    Bloom filter implementation for first lookup on username availability
    username stored in bit_array 
    by undergoing multiple hash functions
    """
    def __init__(self, size=1000000, hash_count=5):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size);
        self.bit_array.setall(0)

    """
        Adds the new username in the bit_array
        Args:
            username(string) : new username which is going to add
    """
    def add(self, username):
       
        for i in range(self.hash_count):
            index = mmh3.hash(username,  i) % self.size
            self.bit_array[index] = 1
    
    """
        checks the  username which already exists in the bit_array
        Args:
            username(string) : new username which is going to add
        Returns:
            bool:
                False -> definitely not present in the bit_array
                True -> possibly present
    """
    def check(self, username):
        for i in range(self.hash_count):
            index = mmh3.hash(username, i) % self.size
            if self.bit_array[index] == 0:
                return False
        return True