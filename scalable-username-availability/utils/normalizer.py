import re
"""
to normalize the username Eg : John, john -> john
Args:
    username(str): which needs to get normalize
Returns:
    username(str): which is normalized
"""
def normalize( username):
    username = username.strip()
    username = username.lower()
    username = re.sub(r"\s+","_",username) # type: ignore
    return username