from bloom.bloom_filter import BloomFilter
from utils.normalizer import normalize
from utils.validation import validate_username
from mockDB.mock_db import MockDb
from analytics.frequency_tracker import FrequencyTracker

class UsernameService:
    def __init__(self):
        self.bloom = BloomFilter()
        self.db = MockDb()
        self.track = FrequencyTracker()

    """
       Checks the availability and also tracks how frequently usernames are attempted.
        Args:
            username (str): Username entered by the user
        Returns:
            bool:
                True  -> Username is available
                False -> Username already exists
    """
    def check_availability(self, username):
        self.track.track(username)
        if not self.bloom.check(username):
            return True
        return not self.db.is_user_exists(username)
    
    """
     Registers a new username into the system.
        Args:
            username (str): Username to register
        Returns:
            bool:
                True  -> Registration successful
                False -> Username already exists
    """
    def registerUsername(self, username):
       username = normalize(username)
       
       if self.check_availability(username):
           self.db.add(username)
           self.bloom.add(username)
           return True
       else:
           return False
    
    """
        Retrieves the most frequently attempted usernames.
        Returns:
            list[tuple[str, int]] | str:
                Returns list of (username, attempt_count)
                if available, otherwise returns message
                indicating no attempts recorded.
    """
    def popular_usernames(self):
        response = self.track.frequent_usernames()
        if len(response) == 0:
            return "No popular usernames"
        else:
            return response
        
       
