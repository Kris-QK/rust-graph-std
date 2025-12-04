import gzip
import sys
from collections import Counter

# 你的最终产物路径
TARGET_FILE = "../data/dist/rust-std-1.89.0.nt.gz"


def main():
    print(f"--- Auditing Artifact: {TARGET_FILE} ---")

    predicate_counts = Counter()
    total_lines = 0

    try:
        # 直接读取 gzip 文件
        with gzip.open(TARGET_FILE, "rt", encoding="utf-8") as f:
            for line in f:
                total_lines += 1
                parts = line.split(" ")
                if len(parts) >= 2:
                    # 提取谓语 (Predicate)
                    predicate = parts[1]
                    predicate_counts[predicate] += 1

                if total_lines % 500000 == 0:
                    print(f"Audited {total_lines} lines...", end="\r")

    except FileNotFoundError:
        print("Error: File not found.")
        return

    print(f"\n\nTotal Lines: {total_lines}")
    print("=" * 60)
    print(f"{'Count':<10} | {'Predicate (Check this list carefully!)'}")
    print("-" * 60)

    # 打印所有谓语，按数量排序
    for pred, count in predicate_counts.most_common():
        print(f"{count:<10} | {pred}")
    print("=" * 60)


if __name__ == "__main__":
    main()
