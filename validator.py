import sys

with open("sampl.py", "r") as f:
    code = f.read()

violations = []

if "password =" in code:
    violations.append("Hardcoded password found")

if "TODO" in code:
    violations.append("TODO comment found")

if violations:
    print("FAILED")
    for v in violations:
        print(v)
    sys.exit(1)

print("PASSED")