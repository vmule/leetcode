# find duplicate files
import os
import shutil
import time
import unittest
from collections import defaultdict
from hashlib import md5 as hash
from multiprocessing import Pool


# read chunks for files larger than 100 MB
FILE_MAX_SIZE = 104857600
MAX_P_PROCESS = os.cpu_count()


def find_hashes(file):
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
    return (file_hash_digest, file)


def find_duplicate_files(path, multiprocess=True):

    files_size = defaultdict(list)
    hashes_dict = defaultdict(list)

    for root, dirs, files in os.walk(path):
        for file in files:
            file = os.path.join(root, file)
            size = os.stat(file).st_size
            files_size[size].append(file)

    duplicates_candidates = []
    for bucket in files_size.values():
        if len(bucket) < 2:
            continue
        else:
            for file in bucket:
                duplicates_candidates.append(file)

    if multiprocess is True:
        pool = Pool(MAX_P_PROCESS)
        results = pool.map(find_hashes, duplicates_candidates)
        for element in results:
            key, file = element
            hashes_dict[key].append(file)
    else:
        for file in duplicates_candidates:
            key, file = find_hashes(file)
            hashes_dict[key].append(file)

    results = []
    for value in hashes_dict.values():
        if len(value) > 1:
            results.append(value)

    return sorted(results)


def main():
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

    expected_result = [
        ["/tmp/a/file1", "/tmp/a/b/c/file2"],
        ["/tmp/a/file4", "/tmp/a/b/file3"],
    ]
    test = unittest.TestCase()

    start_time = time.time()
    duplicates = find_duplicate_files(path)
    print(
        "--- Multiprocess execution took  %s seconds ---" % (time.time() - start_time)
    )

    print(" ")

    for element in duplicates:
        print(element)

    print(" ")

    test.assertEqual(len(duplicates), len(expected_result))
    for i in range(len(duplicates)):
        test.assertCountEqual(duplicates[i], expected_result[i])
    print(" ")

    start_time = time.time()
    duplicates = find_duplicate_files(path, multiprocess=False)
    print(
        "--- Singleprocess execution took %s seconds ---" % (time.time() - start_time)
    )

    print(" ")

    for element in sorted(duplicates):
        print(element)

    print(" ")

    test.assertEqual(len(duplicates), len(expected_result))
    for i in range(len(duplicates)):
        test.assertCountEqual(duplicates[i], expected_result[i])

    print("All tests passed!!")

    shutil.rmtree("/tmp/a")


if __name__ == "__main__":
    main()
