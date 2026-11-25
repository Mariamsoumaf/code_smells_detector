"""Chapter 3 (Functions): finds long functions and too many parameters."""

import ast

from smell import Smell

MAX_FUNCTION_LINES = 20
MAX_PARAMETERS = 3


def find_long_functions(tree):
    smells = []
    for function in _functions(tree):
        length = function.end_lineno - function.lineno + 1
        if length > MAX_FUNCTION_LINES:
            message = (f'"{function.name}" is {length} lines long '
                       f'(max {MAX_FUNCTION_LINES}): split it')
            smells.append(Smell("FUNCTIONS", function.lineno, message))
    return smells


def find_too_many_parameters(tree):
    smells = []
    for function in _functions(tree):
        count = len(get_parameter_names(function))
        if count > MAX_PARAMETERS:
            message = (f'"{function.name}" has {count} parameters '
                       f'(max {MAX_PARAMETERS})')
            smells.append(Smell("FUNCTIONS", function.lineno, message))
    return smells


def get_parameter_names(function):
    arguments = function.args
    all_parameters = arguments.posonlyargs + arguments.args + arguments.kwonlyargs
    return [parameter.arg for parameter in all_parameters
            if parameter.arg not in ("self", "cls")]


def _functions(tree):
    function_types = (ast.FunctionDef, ast.AsyncFunctionDef)
    return [node for node in ast.walk(tree) if isinstance(node, function_types)]
