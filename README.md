# Code Smells Detector (Software Construction)

A small Python tool that reads a `.py` file and finds **Clean Code smells**
from Chapters 1–4 of *Clean Code* (Robert C. Martin).

## 1. Problem
Developers spend most of their time **reading** code, not writing it.
- Xia et al. (IEEE TSE, 2018): developers spend about **58%** of their time on program comprehension.
- Stripe, *The Developer Coefficient* (2018): about **3.8 hours per week** go to fixing "bad code".

Hard-to-read code wastes time and money.

## 2. Research question
> Can a simple tool automatically find Clean Code violations (Chapters 2–4)
> in Python code?

## 3. Methodology
**Static analysis**: the tool reads the code without running it.
- `ast` (Python's built-in parser) → names, functions, parameters
- `tokenize` → comments

## 4. Techniques (what the tool checks)

| Chapter | Check | Rule |
|---|---|---|
| 2. Meaningful Names | Too short names | `x`, `d`, `f1` (loop counters `i`, `j`, `k` are allowed) |
| 2. Meaningful Names | Vague names | `data`, `temp`, `info`, `stuff` ... |
| 2. Meaningful Names | Number names | `data2`, `score1` |
| 3. Functions | Long functions | more than 20 lines |
| 3. Functions | Too many parameters | more than 3 |
| 4. Comments | Commented-out code | `# print(result)` |
| 4. Comments | Redundant comments | `x = x + 1  # add 1 to x` |

## 5. Why this methodology?
- **Fast:** checks a file in less than a second.
- **Safe:** it never runs the code it checks.
- **Built-in:** `ast` and `tokenize` come with Python, no extra libraries.
- **Clear rules:** each rule comes directly from the book, so it is easy to explain and test.

## 6. Clean Code inside the tool itself
- Meaningful names: `find_long_functions()`, `MAX_PARAMETERS`
- Small functions that do one thing
- Constants instead of magic numbers
- One file per chapter: no "position marker" comments needed (Chapter 4)
- The tool checks its own code → **0 smells**

## 7. How to run
```bash
python main.py examples/bad_example.py     # 17 smells
python main.py examples/clean_example.py   # 0 smells (same run)
python main.py name_checks.py              # the tool checks itself: 0 smells
```
Requires Python 3.8+. No extra packages.

## 8. Limitations
- Redundant-comment check works only for comments on the same line as code.
- Some rules (like name length) are simple and may give false alarms.

## Project structure
```
code_smells_detector/
├── main.py            ← reads the file, starts the analysis
├── analyzer.py        ← runs all the checks
├── name_checks.py     ← Chapter 2: Meaningful Names
├── function_checks.py ← Chapter 3: Functions
├── comment_checks.py  ← Chapter 4: Comments
├── smell.py           ← one problem found (category, line, message)
├── report.py          ← prints the result
└── examples/
    ├── bad_example.py
    └── clean_example.py
```

## Sources
- Robert C. Martin, *Clean Code*, Chapters 1–4
- Xia, X., Bao, L., Lo, D., et al. "Measuring Program Comprehension: A Large-Scale Field Study with Professionals." *IEEE TSE*, 2018.
- Stripe. *The Developer Coefficient*, 2018.
