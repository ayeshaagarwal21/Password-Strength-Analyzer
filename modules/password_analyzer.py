from modules.entropy_calculator import calculate_entropy
from modules.pattern_detector import detect_patterns


def analyze_password(password):

    entropy = calculate_entropy(password)

    patterns = detect_patterns(password)

    score = 0

    # Length score
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20

    # Entropy score
    if entropy >= 60:
        score += 40
    elif entropy >= 40:
        score += 30
    elif entropy >= 28:
        score += 20

    # Character diversity
    if any(c.islower() for c in password):
        score += 5

    if any(c.isupper() for c in password):
        score += 5

    if any(c.isdigit() for c in password):
        score += 5

    if any(not c.isalnum() for c in password):
        score += 5

    # Pattern penalty
    score -= len(patterns) * 10

    score = max(0, min(score, 100))

    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "entropy": entropy,
        "patterns": patterns
    }