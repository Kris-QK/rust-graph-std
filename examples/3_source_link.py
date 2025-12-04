import gzip

DATA_FILE = "../data/dist/rust-std-1.89.0.nt.gz"

def main():
    print("--- Example 3: Extracting Source Code Links ---")
    
    try:
        with gzip.open(DATA_FILE, 'rt', encoding='utf-8') as f:
            count = 0
            for line in f:
                if "hasSourceLink" in line:
                    parts = line.split(' ')
                    # Output format: <Subject> ... "src/path/file.rs.html#line"
                    print(f"Item: {parts[0]}")
                    print(f"Link: {parts[2]}")
                    print("-" * 40)
                    count += 1
                    if count >= 5: break
                    
    except FileNotFoundError:
        print("Error: Data file not found.")

if __name__ == "__main__":
    main()
