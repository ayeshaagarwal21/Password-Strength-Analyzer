import re

def detect_patterns(password):

    patterns = []

    # Repeated characters
    if re.search(r'(.)\1{2,}', password):
        patterns.append("Repeated characters")

    # Sequential numeric patterns
    if re.search(
        r'0123|1234|2345|3456|4567|5678|6789',
        password
    ):
        patterns.append("Sequential numbers")

    # Common password words
    common_words = [
        "password",
        "admin",
        "welcome",
        "qwerty",
        "letmein"
    ]

    if any(word in password.lower() for word in common_words):
        patterns.append("Common password word")

    # Keyboard sequences
    keyboard_patterns = [
        "qwerty",
        "asdf",
        "zxcv"
    ]

    if any(p in password.lower() for p in keyboard_patterns):
        patterns.append("Keyboard sequence")

    return patterns