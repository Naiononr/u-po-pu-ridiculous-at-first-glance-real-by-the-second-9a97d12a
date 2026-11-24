"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<= 200 chars) pitching a bizarre startup idea that
sounds absurd until you realise it would actually sell.

The pitch: renting professional mourners who weep on cue at strangers'
funerals. Bizarre on first read; on second read it is a real business -
professional mourning is an old, real profession, funerals are a
high-spend, status-driven market, and grieving families pay to look loved
in front of relatives who flew in.
"""

import os

SENTENCE = (
    "We rent professional mourners who weep on cue at strangers' funerals, "
    "because grieving families pay $200 an hour to look loved in front of "
    "relatives who flew in."
)


def validate(text):
    """Gate: 1-200 chars, single line, non-whitespace, valid UTF-8."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return True


def main():
    validate(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    out_path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    fd = os.open(out_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, SENTENCE.encode("utf-8"))
    finally:
        os.close(fd)
    os.chmod(out_path, 0o644)
    # Revision guard: read back the exact bytes written and re-validate
    # them, so a truncated or mangled write can never pass silently.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != SENTENCE.encode("utf-8"):
        raise RuntimeError("written bytes do not match the entry sentence")
    validate(written.decode("utf-8"))


if __name__ == "__main__":
    main()
