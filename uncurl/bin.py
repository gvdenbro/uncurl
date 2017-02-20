from __future__ import print_function

import sys
from collections import OrderedDict

import xerox
from api import parse

import yaml


def setup_yaml():
    """ http://stackoverflow.com/a/8661021 """
    represent_dict_order = lambda self, data: self.represent_mapping('tag:yaml.org,2002:map', data.items(), flow_style=False)
    yaml.add_representer(OrderedDict, represent_dict_order)


def main():
    setup_yaml()
    if sys.stdin.isatty():
        if len(sys.argv) > 1:
            # If an argument is passed
            result = parse(sys.argv[1])
        else:
            # Otherwise pull from clipboard
            result = parse(xerox.paste())
    else:
        result = parse(sys.stdin.read())
    print(result)
