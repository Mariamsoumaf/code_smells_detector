"""One problem found in the code."""

from dataclasses import dataclass


@dataclass
class Smell:
    category: str
    line: int
    message: str
