#!/usr/bin/env python

"""setup package with given package_name, remove it from project after using"""

import os
import sys

from os.path import join


lib_folder = os.path.dirname(os.path.realpath(__file__))


def set_package_name(filename, package_name=""):
    with open(filename, "r") as f:
        text = f.read()

    if text:
        text = text.replace("PACK_NAME", package_name)
        with open(filename, "w") as f:
            f.write(text)


def fix_files(package_name):
    target_folders = []
    target_files = ["README.md", "docker-compose.yml", "setup.py",
                    "__init__.py", "main.py"]

    for root, dirs, files in os.walk(lib_folder):
        for folder in dirs:
            if folder == "PACK_NAME":
                target_folders.append(join(root, folder))

        for file in files:
            if file in target_files:
                set_package_name(join(root, file), package_name)

    for folder in target_folders:
        os.rename(folder, package_name)


fix_files(sys.argv[1])
