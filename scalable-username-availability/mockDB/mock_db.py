class MockDb:
    """
    mock db for the final confirmation
    to prevent if the bloom filter gave false positive
    """
    def __init__(self):
        self.usernames = set()
    
    def is_user_exists(self, username):
        """
        checks that username is exists in the mock db
        Returns:
            bool:
                False -> username not exists in the db
                True -> username already exists in the db
        """
        return username in self.usernames
    
    def add(self, username):
        """
        Adds the new username into the db
        Args:
            username: username which need to add in the db
        """
        self.usernames.add(username)