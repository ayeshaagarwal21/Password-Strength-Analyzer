import math
import string

def calculate_entropy(password):

    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26

    if any(c.isupper() for c in password):
        pool_size += 26

    if any(c.isdigit() for c in password):
        pool_size += 10

    special_chars = set(string.punctuation)

    if any(c in special_chars for c in password):
        pool_size += len(special_chars)

    if not password or pool_size == 0:
        return 0

    entropy = len(password) * math.log2(pool_size)

    return round(entropy, 2)