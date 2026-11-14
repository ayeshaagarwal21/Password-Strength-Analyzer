from modules.pattern_detector import detect_patterns

password = "password123"

result = detect_patterns(password)

print("Detected Patterns:")

for pattern in result:
    print("-", pattern)