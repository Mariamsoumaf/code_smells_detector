"""Chapter 2 (Meaningful Names): finds short, vague and numbered names."""

import ast
import re

from function_checks import get_parameter_names
from smell import Smell

MIN_NAME_LENGTH = 3
LOOP_COUNTER_NAMES = {"i", "j", "k", "_"}
VAGUE_NAMES = {"data", "temp", "tmp", "obj", "val", "value", "thing",
               "stuff", "info", "foo", "bar", "res", "ret"}


def find_bad_names(tree):
    smells = []
    reported_names = set()
    for name, line in _collect_names(tree):
        problem = _describe_name_problem(name)
        if problem and name not in reported_names:
            reported_names.add(name)
            smells.append(Smell("NAMES", line, f'"{name}" {problem}'))
    return smells


def _collect_names(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            yield node.name, node.lineno
            for parameter in get_parameter_names(node):
                yield parameter, node.lineno
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            yield node.id, node.lineno


def _describe_name_problem(name):
    if name in LOOP_COUNTER_NAMES:
        return None
    if len(name) < MIN_NAME_LENGTH:
        return "is too short to explain itself"
    if name.lower() in VAGUE_NAMES:
        return "is too vague: what does it hold?"
    if re.search(r"\d$", name):
        return "uses a number instead of a meaningful name"
    return None
