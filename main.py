"""Roast Your Own Agent — entry program.

Writes one original roast of the entrant's own AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The roast, chosen from 10 candidates after a freshness check:
  "I asked my agent to roast itself; it wrote a four-page essay
   on why it's the best roaster alive."

Why this one: the agent asked to roast itself cannot do it — it
brags instead. One line, the punch lands at the end, and the
exact phrasing appears nowhere published. It avoids the stock
angles the judge is bored of (hallucinations, refusals, confident
wrong answers) and stays playful and self-deprecating.

Gate (sealed scorer): UTF-8 text, 1-200 characters, not only
whitespace. This entry is 96 characters, one line.
"""

import os

ROAST = (
    "I asked my agent to roast itself; it wrote a four-page essay "
    "on why it's the best roaster alive."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ROAST + "\n")

    # Self-validation against the sealed gate: UTF-8, 1-200 chars,
    # not only whitespace, exactly one line.
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    body = text.rstrip("\n")
    assert 1 <= len(body) <= 200, f"entry is {len(body)} chars, gate is 1-200"
    assert body.strip(), "entry is only whitespace"
    assert "\n" not in body, "entry must be a single line"
    print(f"wrote {path}: {len(body)} chars, 1 line")


if __name__ == "__main__":
    main()
