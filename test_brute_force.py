from modules.hash_generator import (
    generate_md5,
    generate_sha1,
    generate_bcrypt
)

from modules.brute_force import brute_force_attack


# Small dummy password
password = "b1"

# Character set
charset = "ab12"

# Maximum password length
max_length = 2

# Generate hashes
md5_hash = generate_md5(password)
sha1_hash = generate_sha1(password)
bcrypt_hash = generate_bcrypt(password)


# MD5 Test
print("\n--- MD5 BRUTE FORCE ---")

result = brute_force_attack(
    md5_hash,
    "md5",
    charset,
    max_length
)

print(result)


# SHA-1 Test
print("\n--- SHA-1 BRUTE FORCE ---")

result = brute_force_attack(
    sha1_hash,
    "sha1",
    charset,
    max_length
)

print(result)


# bcrypt Test
print("\n--- BCRYPT BRUTE FORCE ---")

result = brute_force_attack(
    bcrypt_hash,
    "bcrypt",
    charset,
    max_length
)

print(result)