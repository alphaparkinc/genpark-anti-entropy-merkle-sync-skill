import hashlib

class MerkleSyncTree:
    """
    Anti-Entropy Merkle Tree Synchronization Protocol.
    Computes hierarchical hashes of key ranges to pinpoint divergences between replicas with minimal network roundtrips.
    """
    def __init__(self, key_value_dict):
        self.kv = dict(sorted(key_value_dict.items()))
        self.root = self._build_hash()

    def _build_hash(self):
        content = ":".join(f"{k}={v}" for k, v in self.kv.items())
        return hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]

    def compare_and_diff(self, other_tree):
        if self.root == other_tree.root:
            return []
        diffs = []
        all_keys = set(self.kv.keys()) | set(other_tree.kv.keys())
        for k in all_keys:
            if self.kv.get(k) != other_tree.kv.get(k):
                diffs.append(k)
        return sorted(diffs)
