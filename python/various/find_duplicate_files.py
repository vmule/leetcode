# find duplicate files
import os
import shutil
from collections import defaultdict
from hashlib import blake2b as hash


def find_duplicate_files(path):

    # read chunks for files larger than 100 MB
    FILE_MAX_SIZE = 104857600

    files_hash = defaultdict(list)
    files_size = defaultdict(list)

    for root, dirs, files in os.walk(path):
        for file in files:
            file = os.path.join(root, file)
            size = os.stat(file).st_size
            files_size[size].append(file)

    for bucket in files_size.values():
        if len(bucket) < 2:
            continue

        for file in bucket:
            with open(file, "rb") as f:
                if os.stat(file).st_size >= FILE_MAX_SIZE:
                    file_hash = hash()
                    chunk = f.read(8192)
                    while chunk:
                        file_hash.update(chunk)
                        chunk = f.read(8192)
                else:
                    file_hash = hash(f.read())
            file_hash_digest = file_hash.hexdigest()
            files_hash[file_hash_digest].append(file)

    results = []
    for value in files_hash.values():
        if len(value) > 1:
            results.append(value)

    return results


if not os.path.isdir("/tmp/a"):
    os.mkdir("/tmp/a")
if not os.path.isdir("/tmp/a/b"):
    os.mkdir("/tmp/a/b")
if not os.path.isdir("/tmp/a/b/c"):
    os.mkdir("/tmp/a/b/c")

# unique files
with open("/tmp/a/file11", "w") as f:
    f.write("Text 00000000000")
with open("/tmp/a/file12", "w") as f:
    f.write("Text 000000000000")
with open("/tmp/a/file13", "w") as f:
    f.write("Text 0000000000000")
with open("/tmp/a/file14", "w") as f:
    f.write("Text 00000000000000")
with open("/tmp/a/file15", "w") as f:
    f.write("Text 000000000000000")
with open("/tmp/a/file16", "w") as f:
    f.write("Text 0000000000000000")

# duplicates
with open("/tmp/a/file1", "w") as f:
    f.write("Text one")
with open("/tmp/a/b/c/file2", "w") as f:
    f.write("Text one")
with open("/tmp/a/b/file3", "w") as f:
    f.write("Text three")
with open("/tmp/a/file4", "w") as f:
    f.write("Text three")


path = "/tmp/a"
duplicates = sorted(find_duplicate_files(path))
for element in duplicates:
    print(element)

assert duplicates == [
    ["/tmp/a/file1", "/tmp/a/b/c/file2"],
    ["/tmp/a/file4", "/tmp/a/b/file3"],
]

print("All tests passed!!")

shutil.rmtree(path)
