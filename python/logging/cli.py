from __future__ import annotations

import json
import logging
import sys
from dataclasses import asdict, dataclass

logging.basicConfig(
    level=logging.INFO,
)


@dataclass(slots=True)
class Success:
    """A successful response."""

    message: str


@dataclass(slots=True)
class Error:
    """An error response."""

    error: str


def write_stdout(value: Success) -> None:
    """Write a JSON response to stdout."""

    print(json.dumps(asdict(value)))


def write_stderr(value: Error) -> None:
    """Write a JSON error to stderr."""

    print(
        json.dumps(asdict(value)),
        file=sys.stderr,
    )


def main() -> int:
    """Run the application."""

    logging.info("Starting")

    write_stdout(
        Success(message="Everything worked"),
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
