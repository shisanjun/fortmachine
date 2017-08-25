# -*- coding:utf-8 -*-
__author__ = 'shisanjun'

import yaml

def print_err(msg,quit=False):
    output = "\033[31;1mError: %s\033[0m" % msg
    if quit:
        exit(output)
    else:
        print(output)


def yaml_parser(ymal_filename):
    try:
        yaml_file=open(ymal_filename,"r")
        data=yaml.load(yaml_file)
        return data
    except Exception as e:
        print_err(e)
