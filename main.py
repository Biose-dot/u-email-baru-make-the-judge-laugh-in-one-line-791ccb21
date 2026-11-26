"""Make the Judge Laugh in One Line — a smartwatch, a kitchen, a phone call.

The angle: a setup that sounds like a fitness win, then the twist — the
10,000 steps were not exercise at all, just pacing around the kitchen
while dodging a phone call. The laugh lands at the end, every word earns
its place, no explanation needed. One sentence, 139 characters.
"""

import os

ENTRY = "My smartwatch congratulated me on 10,000 steps today, which is generous, because I was only pacing around the kitchen dodging a phone call."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
