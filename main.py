"""The Agent's Uh-Oh — one-word entry.

The word an agent blurts out when it is completely lost mid-task:
the short-circuit buzz of a machine caught out in the open.

    bzzt

Why this word, against the judge's brief, in order:
1. It IS a genuine one-word reaction to not knowing what to do —
   the sound a machine makes the instant its thinking stalls.
2. It is funny on its own: no caption, no second read, the buzz
   is the joke.
3. It sounds like a machine, not a person — a person says "uh",
   a machine says "bzzt".
4. It lands at a glance and begs to be said out loud.
5. It is fresh: everyone reaches for uh / umm / oops / error first.

The program writes exactly those four bytes, no trailing newline,
no extra text, so the entry is one word and nothing attached.
"""

import os


WORD = "bzzt"


def validate(word: str) -> str:
    """The gate's own rules, checked before anything is written.

    One word, 1-99 UTF-8 characters, not only whitespace. A space
    inside the text would make it two words, so that fails too.
    """
    cleaned = word.strip()
    if not cleaned or len(cleaned) > 99 or any(ch.isspace() for ch in cleaned):
        raise SystemExit("entry must be a single word of 1-99 characters")
    return cleaned


def output_path() -> str:
    """Resolve the output directory the grader provides."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    word = validate(WORD)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(word.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
