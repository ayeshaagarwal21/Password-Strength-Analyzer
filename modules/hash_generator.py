import hashlib
import bcrypt


# MD5 Hash Generator
def generate_md5(password):

    password_bytes = password.encode('utf-8')

    hash_object = hashlib.md5(password_bytes)

    return hash_object.hexdigest()


# SHA-1 Hash Generator
def generate_sha1(password):

    password_bytes = password.encode('utf-8')

    hash_object = hashlib.sha1(password_bytes)

    return hash_object.hexdigest()


# bcrypt Hash Generator
def generate_bcrypt(password):

    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt(rounds=12)

    hashed_password = bcrypt.hashpw(
        password_bytes,
        salt
    )

    return hashed_password.decode('utf-8')


# Verify bcrypt password
def verify_bcrypt(password, stored_hash):

    return bcrypt.checkpw(
        password.encode('utf-8'),
        stored_hash.encode('utf-8')
    )