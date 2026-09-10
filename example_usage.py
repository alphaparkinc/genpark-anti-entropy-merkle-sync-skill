from client import MerkleSyncTree

def main():
    print("=== Testing Anti-Entropy Merkle Sync ===")
    replica_east = MerkleSyncTree({"doc_1": "hash_a", "doc_2": "hash_b", "doc_3": "hash_c"})
    replica_west = MerkleSyncTree({"doc_1": "hash_a", "doc_2": "hash_modified", "doc_4": "hash_d"})
    
    diffs = replica_east.compare_and_diff(replica_west)
    print(f"Detected divergent keys between East & West: {diffs}")
    assert diffs == ["doc_2", "doc_3", "doc_4"]
    print("=== Anti-Entropy Verification Complete ===")

if __name__ == "__main__":
    main()
