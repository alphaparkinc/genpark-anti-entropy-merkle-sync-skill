from client import MerkleSyncTree
import json

def handle_request(req):
    action = req.get("action")
    if action == "diff":
        kv1 = req.get("kv1", {})
        kv2 = req.get("kv2", {})
        t1 = MerkleSyncTree(kv1)
        t2 = MerkleSyncTree(kv2)
        return {"status": "ok", "diffs": t1.compare_and_diff(t2)}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "diff", "kv1": {"a": "1"}, "kv2": {"a": "2"}})))
