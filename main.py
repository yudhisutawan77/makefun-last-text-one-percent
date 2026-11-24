#!/usr/bin/env python3
"""Last Text at One Percent.

Writes the dying phone's final text message to $ENTRY_OUT.
ENTRY_OUT may name the output file itself or a directory that will
hold entry.txt; both are supported.
"""

import os
import sys


def compose_farewell():
    """The phone's last text, built from its dying confession."""
    opening = "I'm at 1%. Before I go:"
    revenge = "I deleted your 6am alarm."
    signoff = "Sleep in. You're welcome."
    return " ".join([opening, revenge, signoff])


def resolve_destination():
    """Work out the output path from $ENTRY_OUT.

    Accepts a file path, an existing directory, or a path ending
    in a separator (treated as a directory holding entry.txt).
    """
    raw = os.environ.get("ENTRY_OUT", "").strip()
    if not raw:
        return os.path.join(os.getcwd(), "entry.txt")
    if os.path.isdir(raw) or raw.endswith(os.sep):
        return os.path.join(raw, "entry.txt")
    parent_dir = os.path.dirname(raw)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    return raw


def emit_final_text(destination, message):
    folder = os.path.dirname(destination)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as out_file:
        out_file.write(message)


def main():
    farewell = compose_farewell()
    if not (1 <= len(farewell) <= 200):
        print(f"entry is {len(farewell)} chars, must be 1-200", file=sys.stderr)
        return 1
    emit_final_text(resolve_destination(), farewell)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
