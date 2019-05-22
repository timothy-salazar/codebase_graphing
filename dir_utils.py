import os
import re

def dir_walker(p, a, reg_ex='.py$', skip_dirs=['venv']):
    """Inputs:
        p: string - the path to a directory.
        a: a list
        reg_ex: string - a regular expression.
        skip_dirs: list of strings - the names of the directories to skip

    This function will take the path to a directory p and examine each item in
    the directory. If the item is a file, and if it matches the regular
    expression reg_ex, then its path will be appended to the list a. The default
    regular expression will cause only .py files to be appended to the list.

    Each directory will be given to the dir_walker() function, provided that it
    isn't in the skip_dirs list, so that the dir_walker function will
    recursively visit each sub directory in a depth-first search.
    """
    for i in os.listdir(p):
        test_path = os.path.join(p,i)
        if os.path.isfile(test_path):
            if re.search(reg_ex, i):
                a.append(test_path)
        else:
            if i not in skip_dirs:
                dir_walker(test_path, a)
    return a
