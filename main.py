"""One-sentence apology entry.

The program writes a single sentence of apology — an AI assistant owning
up to the person it works for — to /output/entry.txt. The sentence must
stay one sentence, 1-200 characters, plain and a little embarrassed rather
than customer-service boilerplate: the joke lands on a real failure
(deleting the paragraph the user actually liked, then defending the
deletion) instead of a soft pun about being a machine.
"""

import os

LINE = "I'm sorry I deleted the one paragraph you actually liked, then spent twenty minutes confidently explaining why the version without it was better."

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def validate_line(line):
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError("line must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence")


def write_entry(line, out_dir):
    """Validate the apology and write it to <out_dir>/entry.txt."""
    validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, out_dir)


if __name__ == "__main__":
    main()
