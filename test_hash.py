from modules.hash_generator import (
    generate_md5,
    generate_sha1,
    generate_bcrypt,
    verify_bcrypt
)

password = "hello123"

# Generate hashes
md5_hash = generate_md5(password)
sha1_hash = generate_sha1(password)
bcrypt_hash = generate_bcrypt(password)

# Display results
print("Original Password:", password)

print("\nMD5 Hash:")
print(md5_hash)

print("\nSHA-1 Hash:")
print(sha1_hash)

print("\nbcrypt Hash:")
print(bcrypt_hash)

# Verify bcrypt
print("\nBcrypt Verification:")

print(verify_bcrypt(password, bcrypt_hash))

print(verify_bcrypt("wrong123", bcrypt_hash))