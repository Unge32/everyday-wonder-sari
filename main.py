#!/usr/bin/env python3
"""SARI -- one lift ride that turns an ordinary building strange.

The program writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

At 136 characters the line sits comfortably inside the 1-200
gate, a single sentence with one full stop at its end. Sari
is the named character here, the woman riding the lift home
after an ordinary day, expecting nothing from the ride at all.

The lift is the most forgettable room in any building: a
small metal box people enter to wait, staring at floor
numbers, avoiding each other's eyes. Sari knows that ritual
by heart, which is why the stranger's humming stops her.
The tune is not a famous song or a jingle from a shop; it
is the lullaby her dead grandmother used to sing, a melody
she has not heard from another living person in years.

For exactly one floor the coincidence rewrites the whole
building in her head: the corridors, the neighbours she
never speaks to, the doors she passes every day suddenly
feel like rooms in a family home rather than a block of
strangers stacked on top of each other. Then the doors open
and the spell ends, but the wonder stays with her -- a small everyday
moment made strange and new by a song arriving from nowhere,
told in one sentence, grounded in a lift, a stranger, and
a grandmother's voice Sari thought she would never hear again.
"""

import os

LINE = "Sari watched the lift doors open on a stranger humming her dead grandmother's song, and for one floor the whole building felt like home."


def main():
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 gate"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"
    assert LINE.strip() == LINE, "line must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (path, len(LINE)))


if __name__ == "__main__":
    main()
