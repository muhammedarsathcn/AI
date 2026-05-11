class MockDb:
    """
    mock db for the final confirmation
    to prevent if the bloom filter gave false positive
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super(MockDb, cls).__new__(cls)

            # create set only one time
            cls._instance.users = set()

        return cls._instance

    def is_user_exists(self, username):
        """
        checks that username exists in the mock db

        Returns:
            bool:
                False -> username not exists in the db
                True -> username already exists in the db
        """

        return username in self.users

    def add(self, username):
        """
        Adds the new username into the db

        Args:
            username: username which need to add in the db
        """
        self.users.add(username)