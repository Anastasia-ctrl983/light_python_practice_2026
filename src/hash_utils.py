import hashlib

def calculate_hash(file_path, chunk_size=8192):
    # Считает хэш файла (MD5) -----
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except (OSError, PermissionError):
        return None
