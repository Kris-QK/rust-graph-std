import gzip
import sys

# 配置：数据路径
DATA_FILE = "../data/dist/rust-std-1.89.0.nt.gz"


def main():
    print(f"Loading Knowledge Graph from {DATA_FILE}...")

    # 简单的内存数据库 (Subject -> List of (Predicate, Object))
    # 注意：实际生产中请使用 Oxigraph 或 Neo4j，这里仅为演示数据格式
    triples = []

    try:
        with gzip.open(DATA_FILE, "rt", encoding="utf-8") as f:
            for line in f:
                # 简单的 N-Triples 解析
                parts = line.strip().split(" ", 2)
                if len(parts) == 3:
                    s, p, o = parts[0], parts[1], parts[2]
                    # 去掉结尾的 " ."
                    if o.endswith(" ."):
                        o = o[:-2]
                    triples.append((s, p, o))
    except FileNotFoundError:
        print("Error: Data file not found. Please run the slicer first.")
        return

    print(f"Loaded {len(triples)} triples into memory.")

    # === 演示任务：查找 String 及其实现的 Trait ===
    target_name = "String"
    print(f"\n🔍 Searching for struct '{target_name}'...")

    # 1. 找到 String 的 URI
    string_uri = None
    for s, p, o in triples:
        # <.../rdf-schema#label> "String"
        if "label" in p and f'"{target_name}"' in o:
            # 简单过滤，确保是 std 里的
            if "/item/alloc.string" in s or "/item/std.string" in s:
                string_uri = s
                break

    if not string_uri:
        print("Not found.")
        return

    print(f"✅ Found URI: {string_uri}")

    # 2. 查找它实现的 Trait (使用 prop:implements 或者是层级关系)
    # 注意：这里我们演示查找 "isDefinedOn" (方法属于它) 或者 "sourceLink"
    print(f"\n📂 Metadata for {target_name}:")
    for s, p, o in triples:
        if s == string_uri:
            # 简化显示谓语
            pred_name = p.split("/")[-1].replace(">", "")
            print(f"  - {pred_name}: {o}")

    print("\n💡 Demo Complete. Use this logic to feed your LLM RAG system.")


if __name__ == "__main__":
    main()
