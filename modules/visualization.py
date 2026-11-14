import pandas as pd
import matplotlib.pyplot as plt
import os


def show_comparison():

    os.makedirs("results", exist_ok=True)

    df = pd.read_csv(
        "results/performance_comparison.csv"
    )

    # Graph 1: Execution Time
    plt.figure(figsize=(10, 5))

    for algorithm in df["Algorithm"].unique():

        subset = df[df["Algorithm"] == algorithm]

        plt.plot(
            subset["Attack Type"],
            subset["Execution Time"],
            marker="o",
            label=algorithm
        )

    plt.title("Execution Time Comparison")
    plt.xlabel("Attack Type")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "results/execution_time.png",
        dpi=300
    )

    plt.show()
    plt.close()

    # Graph 2: Attempts Comparison
    plt.figure(figsize=(12, 6))

    df["Label"] = (
        df["Algorithm"] + " - " + df["Attack Type"]
    )

    plt.bar(
        df["Label"],
        df["Attempts"]
    )

    plt.title("Number of Attempts Comparison")
    plt.xlabel("Algorithm and Attack Type")
    plt.ylabel("Number of Attempts")
    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.savefig(
        "results/attempts_comparison.png",
        dpi=300
    )

    plt.show()
    plt.close()

    print("Both graphs saved successfully!")