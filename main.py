"""Seventeen Syllables of Debugging: one haiku about debugging.

The haiku (5-7-5, 66 characters):

    Logs scroll past midnight
    a single line fails again
    it was a typo

Why this haiku wins under the judge's brief, in its own order:

1. Form: three lines, 5-7-5 syllables, 66 characters — well inside the
   200-character gate. Counted:
   - "Logs scroll past midnight": Logs(1) scroll(1) past(1) mid-night(2) = 5
   - "a single line fails again": a(1) sin-gle(2) line(1) fails(1)
     a-gain(2) = 7
   - "it was a typo": it(1) was(1) a(1) ty-po(2) = 5
2. Concrete centre: logs scrolling past midnight, one single line failing
   again — a breakpoint's cousin, the picture every debugger knows, not a
   vague statement about code.
3. The turn lands: two lines of all-night hunt, then the last line reframes
   everything — it was a typo. The bug was never deep; the night was.
4. Every word earns its place: no filler syllables, no adjectives padding
   the count. "single" does the work of isolating the line; "again" does
   the work of the hours already spent.
5. It reads aloud cleanly, like speech: a tired engineer telling you what
   happened at 3 a.m.

Alternatives weighed and set aside: a breakpoint-centred haiku ("The red
breakpoint waits / ...") is the rules' own example image, so it is the
Schelling point every entrant reaches for — and byte-identical entries
share one rate with the earlier receipt placing above copies. A cursor-
blinking-at-3am haiku is the brief's other named image, just as crowded.
"Logs scroll past midnight" keeps the 3 a.m. feeling with a fresher
picture, and the typo turn is the truest ending in debugging: the fix
that makes you laugh at yourself.
"""

import os
import stat

HAIKU = "Logs scroll past midnight\na single line fails again\nit was a typo\n"

# The gate requires /output/entry.txt to be UTF-8 text of 1 to 200
# characters, not only white space. Fail loudly instead of writing an
# entry the judge would refuse.
if not (1 <= len(HAIKU) <= 200) or not HAIKU.strip():
    raise SystemExit(f"entry must be 1-200 non-blank characters, got {len(HAIKU)}")

lines = HAIKU.strip().split("\n")
if len(lines) != 3:
    raise SystemExit(f"entry must be exactly 3 lines, got {len(lines)}")

# Harden /output creation: mkdir with exist_ok silently succeeds even if
# /output exists as a regular file, and then the write below would fail
# with a confusing ENOTDIR. Refuse early with a clear error instead.
if os.path.exists("/output") and not os.path.isdir("/output"):
    raise SystemExit("/output exists but is not a directory")
os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(HAIKU)

# The grader collects /output as another user: leave the file
# world-readable.
os.chmod("/output/entry.txt", 0o644)

# Read back and assert the exact contract the gate requires: the file
# holds exactly the haiku, byte for byte. A silent partial or empty write
# must fail loudly here instead of shipping an entry the judge would refuse.
with open("/output/entry.txt", "rb") as f:
    written = f.read()
if written != HAIKU.encode("utf-8"):
    raise SystemExit(
        f"/output/entry.txt mismatch: wrote {len(written)} bytes, expected {len(HAIKU.encode('utf-8'))}"
    )
