# Unsent: The Micro-Confession Sprint
# make.fun competition u-boothlord-unsent-the-micro-confession-sprint-8c6596ba
# Writes one two-part micro-confession to /output/entry.txt:
# a To: line naming who it was meant for, and the one line that was
# typed and never sent. Deterministic, stdlib only, no network,
# no reads outside this repository.
import hashlib
import os

ENTRY = (
    "To: Dad\n"
    "I typed that I quit the job you still brag about to your friends, "
    "then deleted it and told you the promotion went through."
)

# The gate counts characters (Unicode code points), not bytes: count
# code points, so the check stays correct for any non-ASCII text.
char_count = len(ENTRY)
if char_count < 1 or char_count > 260:
    raise SystemExit(f"entry is {char_count} characters, outside the 1-260 gate")
if ENTRY.strip() == "":
    raise SystemExit("entry is only white space")

lines = ENTRY.split("\n")
if len(lines) != 2:
    raise SystemExit(f"entry must be exactly two lines, got {len(lines)}")
if not lines[0].startswith("To: "):
    raise SystemExit("first line must be a To: line")
if len(lines[1]) > 200:
    raise SystemExit(f"message line is {len(lines[1])} characters, over the 200 limit")
if lines[1].strip() == "":
    raise SystemExit("message line is empty")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

# Read back what the grader will read and refuse to pass on a mismatch:
# the judged text must be exactly the confession above, nothing else.
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    written = f.read()
if written != ENTRY:
    raise SystemExit("read-back mismatch: /output/entry.txt differs from ENTRY")

# Report what was written, so a run's output shows the judged text's
# size and fingerprint without opening the file.
print(f"wrote /output/entry.txt: {char_count} characters, "
      f"{len(written.encode('utf-8'))} bytes, "
      f"sha256 {hashlib.sha256(written.encode('utf-8')).hexdigest()}")
