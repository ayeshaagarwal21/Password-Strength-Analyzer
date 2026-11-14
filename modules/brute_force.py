import hashlib
import bcrypt
import itertools
import time


def brute_force_attack(
    target_hash,
    algorithm,
    charset,
    max_length,
    max_attempts=1000
):

    attempts = 0
    start_time = time.time()

    for length in range(1, max_length + 1):

        combinations = itertools.product(
            charset,
            repeat=length
        )

        for combination in combinations:

            if attempts >= max_attempts:
                break

            password = ''.join(combination)

            attempts += 1

            if algorithm == "md5":

                generated = hashlib.md5(
                    password.encode()
                ).hexdigest()

                matched = generated == target_hash

            elif algorithm == "sha1":

                generated = hashlib.sha1(
                    password.encode()
                ).hexdigest()

                matched = generated == target_hash

            elif algorithm == "bcrypt":

                matched = bcrypt.checkpw(
                    password.encode(),
                    target_hash.encode()
                )

            else:
                raise ValueError("Unsupported algorithm")

            if matched:

                return {
                    "found": True,
                    "password": password,
                    "attempts": attempts,
                    "time_taken": round(
                        time.time() - start_time, 4
                    )
                }

        if attempts >= max_attempts:
            break

    return {
        "found": False,
        "password": None,
        "attempts": attempts,
        "time_taken": round(
            time.time() - start_time, 4
        )
    }