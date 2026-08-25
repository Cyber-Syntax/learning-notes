"""python sys.argv example."""

import sys
from pathlib import Path

# `args_count := len(sys.argv)`: Calculate len(sys.argv), store the result in
# args_count, and also give me that result.
# if (args_count := len(sys.argv)) > 2:
#     print(f"One argument expected, got {args_count - 1}")
#     raise SystemExit(2)
# elif args_count < 2:
#     print("You must specify the target dir")
#     raise SystemExit(2)

# Alternative to walrus operator `:=`
# more better for reading, more better for dev's that new to python
# NOTE:
# Suppose you run python sys_argv.py src src_2
# then sys.argv = ["sys_argv.py" ,"src", "src_2"]
# so args_count = 3 because of len()
args_count = len(sys.argv)

if args_count > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the target dir")
    raise SystemExit(2)

# sys_argv[0] is sys_argv.py
# sys_argv[1] is the folder name gived by user (e.g src)
target_dir = Path(sys.argv[1])

if not target_dir.is_dir():
    print("The target path is not a directory")
    raise SystemExit(1)

# For each entry inside target_dir, put that entry into the variable `entry`.
# Example: src/{app.py, main.py, cli.py}
# 3 iteration:
#       entry = Path("src/app.py") -> print(entry.name) -> app.py
#       entry = Path("src/main.py") -> print(entry.name) -> main.py
#       entry = Path("src/cli.py") -> print(entry.name) -> cli.py
for entry in target_dir.iterdir():
    print(entry.name)
