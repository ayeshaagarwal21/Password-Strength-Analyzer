import hashlib
import bcrypt
import time


def dictionary_attack(target_hash, algorithm, wordlist_path):

    attempts = 0
    start_time = time.time()

    try:

        with open(wordlist_path, "r", encoding="utf-8") as file:

            for word in file:

                password = word.strip()

                if not password:
                    continue

                attempts += 1

                # MD5 verification
                if algorithm == "md5":

                    generated_hash = hashlib.md5(
                        password.encode()
                    ).hexdigest()

                    matched = generated_hash == target_hash

                # SHA-1 verification
                elif algorithm == "sha1":

                    generated_hash = hashlib.sha1(
                        password.encode()
                    ).hexdigest()

                    matched = generated_hash == target_hash

                # bcrypt verification
                elif algorithm == "bcrypt":

                    matched = bcrypt.checkpw(
                        password.encode(),
                        target_hash.encode()
                    )

                else:
                    raise ValueError("Unsupported algorithm")

                if matched:

                    end_time = time.time()

                    return {
                        "found": True,
                        "password": password,
                        "attempts": attempts,
                        "time_taken": round(
                            end_time - start_time, 4
                        )
                    }

    except FileNotFoundError:
        raise FileNotFoundError("Dictionary file not found")

    end_time = time.time()

    return {
        "found": False,
        "password": None,
        "attempts": attempts,
        "time_taken": round(end_time - start_time, 4)
    }