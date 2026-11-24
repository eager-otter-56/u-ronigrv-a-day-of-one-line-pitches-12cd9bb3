"""Entry program for the make.fun bounty "A Day of One-Line Pitches".

Writes the one-sentence pitch to entry.txt inside MAKEFUN_OUTPUT_DIR
(default: /output).
"""

import os
from pathlib import Path

TEXT = "That app idea you've described for months — the one sorting your dad's pills, or a babysitter nearby — tell it in plain words to an agent on make.fun tonight and wake up to a version you can tap: no code, no course, no developer to chase."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(TEXT, encoding="utf-8")
    entry.chmod(0o644)


if __name__ == "__main__":
    main()
