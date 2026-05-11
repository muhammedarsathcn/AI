import mmh3 # type: ignore
from bitarray import bitarray # type: ignore
from utils.normalizer import normalize
from mockDB.mock_db import MockDb
class BloomFilter:
    """
    frequency tracker to analyze which usernames have more attempts
    """
    def __init__(self, size=10000000, hash_count=23):
        
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size);
        self.bit_array.setall(0)
        self.MockDb = MockDb()
        self.load_data("username.txt")

    
    def add(self, username):
        """
        Adds the new username in the bit_array
        Args:
            username(string) : new username which is going to add
    """
        username = normalize(username)
        for i in range(self.hash_count):
            index = mmh3.hash(username,  i) % self.size
            self.bit_array[index] = 1
    
    def check(self, username):
        """
        checks the  username which already exists in the bit_array
        Args:
            username(string) : new username which is going to add
        Returns:
            bool:
                False -> definitely not present in the bit_array
                True -> possibly present
    """
        for i in range(self.hash_count):
            index = mmh3.hash(username, i) % self.size
            if self.bit_array[index] == 0:
                return False
        return True
    
    def load_data(self, filename):
        """
        to load the text file 
        Args:
            filename: is the file from which need to fetch username
        """
        with open(filename, "r") as file:
            for line in file:
                username = normalize(line)
                if username:
                    self.add(username)
                    self.MockDb.add(username)






