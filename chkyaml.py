#! /usr/bin/python

import sys
import yaml

file_path = sys.argv[1]  # set filename in command line argument
# ---------------------------------------------------------------------


def f_check_yaml_file():
    try:
        yaml_data = yaml.safe_load(open(file_path, 'r'))
    except Exception as e:
        print >> sys.stderr, "Failed parse yaml file: %s" % e
        sys.exit(1)
# ---------------------------------------------------------------------


if __name__ == "__main__":
    f_check_yaml_file()
