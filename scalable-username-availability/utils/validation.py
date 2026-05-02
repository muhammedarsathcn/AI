import re
"""
to validate the username
the username should ony contains alphabetical characters and numbers
Args:
    username(str): username need to validate
Returns:
    bool:
        False -> username is not valid
        True -> username is valid
"""
def validate_username(username):
      return bool(re.fullmatch(r"[A-Za-z0-9]{3,30}", username))
