"""Chapter 4 (Comments): finds commented-out code and redundant comments."""

import ast
import io
import re
import tokenize
from dataclasses import dataclass

from smell import Smell

FILLER_WORDS = {"a", "an", "the", "to", "of", "and", "by", "for", "in",
                "is", "it", "this", "add", "adds", "set", "sets", "get",
                "gets", "increment", "increments", "call", "calls",
                "return", "returns", "variable", "value", "function",
                "divide", "multiply", "subtract", "plus", "minus", "times"}
CODE_HINT = re.compile(r"[=()\[\]]|^(import|from|return|if|for|while|print)\b")


@dataclass
class Comment:
    text: str
    line: int
    code_before_it: str


def find_comment_smells(source):
    smells = []
    for comment in _read_comments(source):
        if _is_commented_out_code(comment.text):
            smells.append(Smell("COMMENTS", comment.line,
                                "commented-out code: delete it, Git remembers it"))
        elif comment.code_before_it and _repeats_the_code(comment):
            smells.append(Smell("COMMENTS", comment.line,
                                "comment only repeats what the code says"))
    return smells


def _read_comments(source):
    tokens = tokenize.generate_tokens(io.StringIO(source).readline)
    for token in tokens:
        if token.type == tokenize.COMMENT:
            line_number, column = token.start
            code_before_it = token.line[:column].strip()
            yield Comment(token.string, line_number, code_before_it)


def _is_commented_out_code(comment_text):
    text = comment_text.lstrip("#").strip()
    if not text or not CODE_HINT.search(text):
        return False
    try:
        ast.parse(text)
        return True
    except SyntaxError:
        return False


def _repeats_the_code(comment):
    comment_words = re.findall(r"\w+", comment.text.lower())
    code_words = set(re.findall(r"\w+", comment.code_before_it.lower()))
    meaningful_words = [word for word in comment_words if word not in FILLER_WORDS]
    return all(word in code_words for word in meaningful_words)
