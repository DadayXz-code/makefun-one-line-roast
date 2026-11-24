"""One-Line Roast: The Gadget You Use Every Day.

Writes exactly one original roast line about the phone -- the gadget
used every day -- to /output/entry.txt. Deterministic: the same line,
byte for byte, on every run. No randomness, no time, no network.
"""

import os

# The roast: my phone, its storage, and a landlord who locks every room.
LINE = (
    "My phone has 128 GB of storage and still begs me to delete photos, "
    "like a landlord who rents me a mansion and locks every room."
)


def main() -> None:
    # The gate allows 1 to 200 characters; stay comfortably inside it.
    assert 1 <= len(LINE) <= 200, "roast line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
