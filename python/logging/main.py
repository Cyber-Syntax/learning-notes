"""learning stdout,stderr,stdin..."""

from __future__ import annotations

import sys

print("hello stdout")

print("oops stderr", file=sys.stderr)

# uv run python main.py > output.txt
#
# terminal output:
# oops stderr
#
# output.txt:
# hello stdout


# uv run main.py 2> errors.txt
#
# terminal output:
# hello stdout
#
# errors.txt:
# oops stderr
