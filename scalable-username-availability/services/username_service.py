from bloom.bloom_filter import BloomFilter
from utils.normalizer import normalize
from utils.validation import validate_username
from mockDB.mock_db import MockDb
from analytics.frequency_tracker import FrequencyTracker
import math


class UsernameService:
    """
    Service layer for handling username operations
    like availability checking, registration,
    false positive tracking and analytics.
    """

    def __init__(self):

        self.bloom = BloomFilter()
        self.db = MockDb()
        self.track = FrequencyTracker()
        self.total_checks = 0
        self.false_positives = 0

    def check_availability(self, username):
        """
        Checks whether username is available
        Args:
            username(str): username entered by user
        Returns:
            bool:
                True  -> username available
                False -> username already exists
        """
        self.track.track(username)
        if not validate_username(username):
            return False
        username = normalize(username)
        bloom_result = self.bloom.check(username)
        if not bloom_result:
            return True
        
        self.total_checks += 1
        db_result = self.db.is_user_exists(username)
        if not db_result:
            self.false_positives += 1
            return True
        

        return False

    def registerUsername(self, username):
        """
        Registers new username into system
        Args:
            username(str): username to register
        Returns:
            bool:
                True  -> registration success
                False -> username already exists
        """
        username = normalize(username)
        if self.check_availability(username):
            self.db.add(username)
            self.bloom.add(username)
            return True
        return False

    def get_false_positive_percentage(self):
        """
        Calculates runtime false positive percentage
        Returns:
            float: false positive percentage
        """
        if self.total_checks == 0:
            return 0.0
        return (
            self.false_positives
            / self.total_checks
        ) * 100

    def theoretical_false_positive_rate(self):
        """
        Calculates theoretical false positive rate
        Formula:
            (1 - e^(-kn/m)) ^ k
        where:
            k -> number of hash functions
            n -> inserted usernames
            m -> bloom filter size
        Returns:
            float: theoretical false positive rate
        """

        m = self.bloom.size
        k = self.bloom.hash_count
        n = len(self.db.users)
        return (
            1 - math.exp(-(k * n) / m)
        ) ** k

    def print_stats(self):
        """
        Prints bloom filter statistics
        """
        runtime_rate = (
            self.get_false_positive_percentage()
        )
        theoretical_rate = (
            self.theoretical_false_positive_rate()
        ) * 100

        print("\nBloom Filter Statistics")
        print("-" * 35)
        print(
            f"Bloom Positive Checks: "
            f"{self.total_checks}"
        )
        print(
            f"False Positives: "
            f"{self.false_positives}"
        )
        print(
            f"Runtime False Positive Rate: "
            f"{runtime_rate:.10f}%"
        )

        print(
            f"Theoretical False Positive Rate: "
            f"{theoretical_rate:.10f}%"
        )

    def popular_usernames(self):
        """
        Retrieves frequently attempted usernames

        Returns:
            list[tuple[str, int]] | str
        """
        response = self.track.frequent_usernames()
        if len(response) == 0:
            return "No popular usernames"
        return response