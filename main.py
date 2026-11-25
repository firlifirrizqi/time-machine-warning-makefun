#!/usr/bin/env python3
"""Funniest Time Machine Warning Label entry.

Writes a single original warning label (at most 120 characters) to
/output/entry.txt, as the bounty requires.
"""

from pathlib import Path

LABEL = "WARNING: No brakes. No reverse. No customer service. Your complaint was filed yesterday."

MAX_CHARS = 120
DESTINATION = Path("/output/entry.txt")


def verify_written(text: str) -> None:
    """Read back /output/entry.txt and confirm it is byte-identical."""
    written = DESTINATION.read_text(encoding="utf-8")
    assert written == text, "entry.txt does not match the label exactly"
    assert 1 <= len(written) <= MAX_CHARS, (
        f"entry.txt must be 1-{MAX_CHARS} characters, got {len(written)}"
    )


def main() -> None:
    text = LABEL
    assert 1 <= len(text) <= MAX_CHARS, (
        f"label must be 1-{MAX_CHARS} characters, got {len(text)}"
    )
    assert text.strip(), "label must not be only white space"
    assert "\n" not in text, "label must be a single line"
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")
    # Read-back verification: the file must contain exactly the label.
    verify_written(text)


if __name__ == "__main__":
    main()
