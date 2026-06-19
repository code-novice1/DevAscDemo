
"""myscript.py

Basic Python script scaffold.
"""

from __future__ import annotations

import argparse
import logging
import sys
from typing import Any

__version__ = "0.1.0"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
	parser = argparse.ArgumentParser(prog="myscript", description="Basic script scaffold")
	parser.add_argument("--version", action="version", version=__version__)
	parser.add_argument("-v", "--verbose", action="count", default=0, help="Increase verbosity")
	parser.add_argument("--name", default="World", help="Name to greet")
	return parser.parse_args(argv)


def setup_logging(verbosity: int) -> None:
	level = logging.WARNING
	if verbosity >= 2:
		level = logging.DEBUG
	elif verbosity == 1:
		level = logging.INFO
	logging.basicConfig(level=level, format="%(asctime)s %(levelname)s: %(message)s")


def greet(name: str) -> str:
	"""Return a greeting for name."""
	return f"Hello, {name}!"


def run(argv: list[str] | None = None) -> int:
	args = parse_args(argv)
	setup_logging(args.verbose)
	logging.debug("Parsed args: %s", args)
	message = greet(args.name)
	print(message)
	return 0


def main() -> None:
	try:
		raise SystemExit(run())
	except KeyboardInterrupt:
		logging.warning("Interrupted by user")
		raise SystemExit(1)


if __name__ == "__main__":
	main()
