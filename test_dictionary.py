from modules.hash_generator import (
    generate_md5,
    generate_sha1,
    generate_bcrypt
)

from modules.dictionary_attack import dictionary_attack


# Dummy password
password = "hello123"

# Generate test hashes
md5_hash = generate_md5(password)
sha1_hash = generate_sha1(password)
bcrypt_hash = generate_bcrypt(password)

# Local dictionary path
wordlist = "dataset/passwords.txt"


# Test MD5
print("\n--- MD5 ATTACK ---")

result = dictionary_attack(
    md5_hash,
    "md5",
    wordlist
)

print(result)


# Test SHA-1
print("\n--- SHA-1 ATTACK ---")

result = dictionary_attack(
    sha1_hash,
    "sha1",
    wordlist
)

print(result)


# Test bcrypt
print("\n--- BCRYPT ATTACK ---")

result = dictionary_attack(
    bcrypt_hash,
    "bcrypt",
    wordlist
)

print(result)