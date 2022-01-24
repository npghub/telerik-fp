import sys
from pylint import lint
# score = 1
THRESHOLD = 5
run = lint.Run(["test.py"], do_exit=False)
# print(run.linter.stats["global_note"])
score = run.linter.stats["global_note"]
if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    sys.exit(1)
sys.exit(0)
