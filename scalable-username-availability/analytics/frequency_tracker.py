from collections import Counter
import math
class FrequencyTracker:
    """
    frequency tracker to analyze which usernames have more attempts
    """
 
    def __init__(self):
        self.counter = Counter()

    def track(self, username):
        """
        Tracks the count of the username
        Args:
            username: which username have to be track
        """
        self.counter[username] += 1
    
    def frequent_usernames(self, limit=5):
        """
        fetch top n(limit) most common usernames
        Args:
            limit: upto (limit) most common usernames
        Returns:
              list[tuple[str, int]]-> List of (username, attempt_count)
        """
        return self.counter.most_common(limit)
    
  

    def theoretical_false_positive_rate(self,m,n,k):
           return (1 - math.exp(-(k * n) / m) ) ** k