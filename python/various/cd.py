"""
Implent cd like function that returns the correct path to cd into.
"""

SYMLINKS = {"/home/z": "/home/vito", "/home/y": "/home/z", "/home/x": "/home/y"}


def find_sym(symlinks, path):
    while path in symlinks:
        path = symlinks[path]
    return path


def cd(pwd, path):

    if path[0] == "/":
        split_pwd = []
    else:
        split_pwd = pwd.split("/")
    split_path = path.split("/")

    for folder in split_path:
        if folder == ".":
            continue
        elif folder == "..":
            split_pwd.pop()
        else:
            split_pwd.append(folder)

    abs_path = "/".join(split_pwd)

    while len(split_pwd) > 1:
        sub_path = "/".join(split_pwd)
        real_sub_path = find_sym(SYMLINKS, sub_path)
        if real_sub_path == sub_path:
            split_pwd.pop()
        else:
            abs_path = abs_path.replace(sub_path, real_sub_path)
            break
    return abs_path


assert cd("/home/vito", "../../etc/var/log") == "/etc/var/log"
assert cd("/etc", "var/log") == "/etc/var/log"
assert cd("/home/vito", "/") == "/"
assert cd("/home/vito", "..") == "/home"
assert cd("/home/vito", "../../home/franco") == "/home/franco"
assert cd("/home/vito", "/home/x") == "/home/vito"
assert cd("/home/vito", "/home/x/banana/cane") == "/home/vito/banana/cane"

print("All tests passed!!")
