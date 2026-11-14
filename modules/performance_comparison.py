import time
import pandas as pd

from modules.hash_generator import (
    generate_md5,
    generate_sha1,
    generate_bcrypt
)

from modules.dictionary_attack import dictionary_attack
from modules.brute_force import brute_force_attack


def run_comparison():

    password = "b1"

    charset = "ab12"
    max_length = 2

    wordlist = "dataset/comparison_passwords.txt"

    # Generate target hashes
    hashes = {
        "MD5": generate_md5(password),
        "SHA-1": generate_sha1(password),
        "bcrypt": generate_bcrypt(password)
    }

    algorithms = {
        "MD5": "md5",
        "SHA-1": "sha1",
        "bcrypt": "bcrypt"
    }

    results = []

    for name, algorithm in algorithms.items():

        target_hash = hashes[name]

        # Dictionary attack
        start = time.perf_counter()

        dictionary_result = dictionary_attack(
            target_hash,
            algorithm,
            wordlist
        )

        dictionary_time = time.perf_counter() - start

        results.append({
            "Algorithm": name,
            "Attack Type": "Dictionary",
            "Found": dictionary_result["found"],
            "Attempts": dictionary_result["attempts"],
            "Execution Time": round(dictionary_time, 6)
        })

        # Brute force attack
        start = time.perf_counter()

        brute_result = brute_force_attack(
            target_hash,
            algorithm,
            charset,
            max_length
        )

        brute_time = time.perf_counter() - start

        results.append({
            "Algorithm": name,
            "Attack Type": "Brute Force",
            "Found": brute_result["found"],
            "Attempts": brute_result["attempts"],
            "Execution Time": round(brute_time, 6)
        })

    # Convert results into DataFrame
    df = pd.DataFrame(results)

    print("\n===== PERFORMANCE COMPARISON =====\n")

    print(df.to_string(index=False))

    # Save results
    df.to_csv(
        "results/performance_comparison.csv",
        index=False
    )

    print("\nResults saved successfully!")

    return df