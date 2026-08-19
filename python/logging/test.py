"""example for stderr stdout and pipe.

usage:
    uv run test.py install requests
    uv run test.py install requests --json
    uv run test.py install requests --json > result.json

    Meanwhile, main.log records everything, including DEBUG messages that users never see in main.log

wrong usage:
    if you add print("starting install") for the code
    it would use stdout and piping like > result.json
    end up consuming "starting install" too.


RULE:
    "If another program ran my CLI, would this text be considered part of the command's result?"

    Yes ->  write it to stdout (typically with print() in a simple CLI).
    No  ->  it's just status/progress/debugging → use logging, which should usually write to stderr (and optionally a log file).
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import asdict, dataclass

LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class InstallResult:
    """Result of an installation."""

    package: str
    version: str
    installed: bool


def configure_logging() -> None:
    """Configure logging."""

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
    )

    # NOTE: file_handler never use stderr or stdout
    # it directly write it to file.
    # so logger.info is directly write main.log and stderr
    file_handler = logging.FileHandler("main.log")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    LOGGER.setLevel(logging.DEBUG)
    LOGGER.addHandler(file_handler)
    LOGGER.addHandler(console_handler)


def install_package(package: str) -> InstallResult:
    """Pretend to install a package."""

    LOGGER.info("Starting installation")
    LOGGER.debug("Checking package index")
    LOGGER.debug("Resolving dependencies")
    LOGGER.info("Downloading package")
    LOGGER.info("Installing package")
    LOGGER.debug("Cleaning temporary files")
    LOGGER.info("Installation complete")

    return InstallResult(
        package=package,
        version="1.2.3",
        installed=True,
    )


def print_human(result: InstallResult) -> None:
    """Print a human friendly result."""

    print()
    print("✔ Installation completed")
    print()
    print(f"Package : {result.package}")
    print(f"Version : {result.version}")


def print_json(result: InstallResult) -> None:
    """Print machine readable JSON."""

    print(json.dumps(asdict(result), indent=2))


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""

    parser = argparse.ArgumentParser()

    parser.add_argument("command")
    parser.add_argument("package")
    parser.add_argument(
        "--json",
        action="store_true",
    )

    return parser.parse_args()


def main() -> int:
    """Run the application."""

    configure_logging()

    args = parse_args()

    if args.command != "install":
        LOGGER.error("Unknown command")

        print("Unknown command", file=sys.stderr)

        return 1

    result = install_package(args.package)

    if args.json:
        print_json(result)
    else:
        print_human(result)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
