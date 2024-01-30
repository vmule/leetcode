# find duplicate files
from collections import defaultdict
from hashlib import blake2b as hash


def find_duplicate_files(files):

    files_hash = defaultdict(list)
    for file in files:
        with open(file, "rb") as f:
            file_hash = hash()
            chunk = f.read(8192)
            while chunk:
                file_hash.update(chunk)
                chunk = f.read(8192)
        file_hash_digest = file_hash.hexdigest()
        files_hash[file_hash_digest].append(file)

    print(list(files_hash.values()))
    return list(files_hash.values())


with open("/tmp/file1", "w") as f:
    f.write("Text one")
with open("/tmp/file2", "w") as f:
    f.write("Text one")
with open("/tmp/file3", "w") as f:
    f.write("Text three")
with open("/tmp/file4", "w") as f:
    f.write("Text three")


files = ["/tmp/file1", "/tmp/file2", "/tmp/file3", "/tmp/file4"]

assert find_duplicate_files(files) == [
    ["/tmp/file1", "/tmp/file2"],
    ["/tmp/file3", "/tmp/file4"],
]

print("All tests passed!!")
