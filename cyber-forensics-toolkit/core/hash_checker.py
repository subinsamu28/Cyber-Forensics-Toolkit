# core/hash_checker.py
import hashlib
import os

def calculate_hashes(path, hash_type="MD5"):
    hash_func = {
        "MD5": hashlib.md5,
        "SHA1": hashlib.sha1,
        "SHA256": hashlib.sha256
    }.get(hash_type.upper())

    if not os.path.exists(path):
        return ["Invalid file or path."]

    results = []

    def hash_file(fpath):
        h = hash_func()
        with open(fpath, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()

    if os.path.isfile(path):
        hash_val = hash_file(path)
        results.append(f"{os.path.basename(path)} - {hash_val}")
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for name in files:
                full_path = os.path.join(root, name)
                hash_val = hash_file(full_path)
                results.append(f"{name} - {hash_val}")
    else:
        results.append("Unsupported path.")

    return results
