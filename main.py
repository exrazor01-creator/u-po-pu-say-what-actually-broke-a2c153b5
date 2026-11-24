"""Write one line of brutal-truth error copy: a dead session.

The line names the real failure in plain words - the login expired,
the server lost the session - and tells the user exactly what to do
next: sign in again. The joke is the server's goldfish memory, an
image a reader repeats out loud to a colleague, and the sting is
that signing in again will not fix the forgetting.

Gate guard: the entry must be UTF-8 text of 1 to 200 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt for bounty
u-po-pu-say-what-actually-broke-a2c153b5. Refuse to write anything
that fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "Your login expired because the server has the memory of a "
    "goldfish. Sign in again. It will forget you just as fast."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 and ch not in ("\n", "\r") for ch in text):
        raise SystemExit("entry must not contain control characters")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing space")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
