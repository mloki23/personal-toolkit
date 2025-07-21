import os
import hashlib

def find_duplicate_files(directory):
    """
    Finds duplicate files in a given directory and its subdirectories.
    Returns a dictionary where keys are file hashes and values are lists of file paths.
    """
    hashes = {}
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if os.path.isfile(full_path):
                file_hash = calculate_file_hash(full_path)
                if file_hash in hashes:
                    hashes[file_hash].append(full_path)
                else:
                    hashes[file_hash] = [full_path]
    return {h: paths for h, paths in hashes.items() if len(paths) > 1}

def calculate_file_hash(filepath, block_size=65536):
    """
    Calculates the SHA256 hash of a file.
    """
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read(block_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(block_size)
    return hasher.hexdigest()