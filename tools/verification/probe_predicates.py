# probe_predicates.py
import sys
from collections import Counter


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 probe_predicates.py <nt_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    print(f"Scanning predicates in {filepath}...")

    predicate_counts = Counter()

    # 定义标准库白名单，顺便统计一下 Crate 分布，确保没有第三方库混入
    crate_counts = Counter()
    std_crates = {"std", "core", "alloc", "proc_macro", "test"}

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                parts = line.split(" ")
                if len(parts) < 3:
                    continue

                # 1. 提取 Predicate (通常是第二个元素)
                # 格式: <Subject> <Predicate> <Object> .
                predicate = parts[1]
                predicate_counts[predicate] += 1

                # 2. 提取 Crate (用于验证是否混入第三方库)
                # Subject 示例: <https://.../item/alloc.alloc_Mod>
                subject = parts[0]
                if "/item/" in subject:
                    try:
                        # 提取 /item/ 之后，第一个 . 之前的内容
                        start = subject.find("/item/") + 6
                        end = subject.find(".", start)
                        if end != -1:
                            crate = subject[start:end]
                            crate_counts[crate] += 1
                    except:
                        pass

                if i % 100000 == 0 and i > 0:
                    print(f"Processed {i} lines...", end="\r")

    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

    print(f"\n\n=== Analysis Result for {filepath} ===\n")

    print("--- Predicate Distribution (Top 20) ---")
    # 这里我们将看到哪些谓语最占地方，决定要切谁
    for pred, count in predicate_counts.most_common(20):
        print(f"{count:<10} {pred}")

    print("\n--- Crate Distribution (Verification) ---")
    # 这里用于验证是否只有标准库
    for crate, count in crate_counts.most_common():
        status = "[OK]" if crate in std_crates else "[WARNING: Third-party?]"
        print(f"{count:<10} {crate:<15} {status}")


if __name__ == "__main__":
    main()
