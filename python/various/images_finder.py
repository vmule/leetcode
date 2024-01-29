def find_image_paths(structure_input):
    """
    There are multiple images of the revamped Tesla Semi somewhere in a directory and we want to find them.

    Given a directory structure, find all the paths to image files (.jpg, .gif, .png) and return the paths.

    structure_input = "dir1\n\tdir11\n\tdir12\n\t\tfile.jpg\ndir2\n\tfile2.png\ndir3\n\tblah.txt\n\tdir31\n\t\tdir311\n\t\t\tblah.gif"

    ├── _ dir1\n <
    |   ├── _ \tdir11\n
    |   └── _ \tdir12\n <
    |       └── \t\tfile.jpg\n <
    |
    ├── _ dir2\n <
    |   └── \tfile2.png\n <
    |
    └── _ dir3 <
        ├── blah.txt
        └── _ dir31 <
            └── _ dir311 <
                └── blah.gif <

    output = ["dir1/dir12/file.jpg", "dir2/file2.png", "dir3/dir31/dir311/blah.gif"]
    """

    entries = structure_input.split("\n")
    result = []
    path_so_far = []
    for entry in entries:
        stripped_entry = entry.lstrip("\t")
        tabs = len(entry) - len(stripped_entry)

        # path_so_far = ["dir1", "dir12", "file.jpg"]
        # entry = "\tdir13"
        #
        # path_so_far = ["dir1"] Remove until len(path_so_far) = 1 because only one "\t" in "\tdir13"
        # path_so_Far = ["dir1", "dir13"]
        while path_so_far and tabs < len(path_so_far):
            path_so_far.pop()

        path_so_far.append(stripped_entry)
        if entry.endswith((".jpg", ".png", ".gif")):
            result_to_add = "/".join(path_so_far)
            result.append(result_to_add)

    return result


structure_input = "dir1\n\tdir11\n\tdir12\n\t\tfile.jpg\ndir2\n\tfile2.png\ndir3\n\tblah.txt\n\tdir31\n\t\tdir311\n\t\t\tblah.gif"

result = find_image_paths(structure_input)
print(result)
