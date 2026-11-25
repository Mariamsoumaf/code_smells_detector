"""Runs every check on a piece of source code."""

import ast

from comment_checks import find_comment_smells
from function_checks import find_long_functions, find_too_many_parameters
from name_checks import find_bad_names


def analyze_source(source):
    tree = ast.parse(source)
    smells = (find_bad_names(tree)
              + find_long_functions(tree)
              + find_too_many_parameters(tree)
              + find_comment_smells(source))
    return sorted(smells, key=lambda smell: smell.line)
