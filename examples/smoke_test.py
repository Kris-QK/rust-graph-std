import gzip
import sys


# 模拟一个极简的图数据库加载过程
def simple_smoke_test():
    gz_path = "../data/dist/rust-std-1.89.0.nt.gz"
    print(f"Loading {gz_path}...")

    target_subject = "std.string.String_Struct"  # 我们试着找 String
    found_count = 0

    try:
        with gzip.open(gz_path, "rt", encoding="utf-8") as f:
            for line in f:
                # 检查数据是否可读
                if "String_Struct" in line and "/item/" in line:
                    print(f"Sample Data: {line.strip()[:150]}...")  # 只打印前150字符
                    found_count += 1
                    if found_count >= 3:
                        break
    except Exception as e:
        print(f"FATAL ERROR: Data corrupted! {e}")
        return

    if found_count > 0:
        print("\n✅ SMOKE TEST PASSED: Data is readable and searchable.")
    else:
        print("\n❌ SMOKE TEST FAILED: Could not find 'String' in the data.")


if __name__ == "__main__":
    simple_smoke_test()
