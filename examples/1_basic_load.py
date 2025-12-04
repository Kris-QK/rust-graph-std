import gzip

# Path to the compressed graph data
DATA_FILE = "../data/dist/rust-std-1.89.0.nt.gz"

def main():
    print(f"--- Example 1: Basic Data Loading from {DATA_FILE} ---")
    
    try:
        # Read the gzip file in text mode ('rt')
        with gzip.open(DATA_FILE, 'rt', encoding='utf-8') as f:
            print("Reading first 10 triples:\n")
            for i, line in enumerate(f):
                if i >= 10: break
                print(f"[{i+1}] {line.strip()}")
                
    except FileNotFoundError:
        print("Error: Data file not found. Please ensure data/dist contains the .gz file.")

if __name__ == "__main__":
    main()
