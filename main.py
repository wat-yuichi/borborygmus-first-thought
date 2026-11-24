import os
from pathlib import Path

# The rumble of a hungry stomach: surprising, vivid, and it sounds like what it means.
WORD = "Borborygmus"
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
