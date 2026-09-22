# import sys

# with open("sampl.py", "r") as f:
#     code = f.read()

# violations = []

# if "password =" in code:
#     violations.append("Hardcoded password found")

# if "TODO" in code:
#     violations.append("TODO comment found")

# if violations:
#     print("FAILED")
#     for v in violations:
#         print(v)
#     sys.exit(1)

# print("PASSED")
import sys

# Read rules
rules = []

with open("rules/rules.txt", "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        severity, pattern = line.split("|")

        rules.append({
            "severity": severity,
            "pattern": pattern
        })

# Read source code
with open("sampl.py", "r") as file:
    code_lines = file.readlines()

violations = []
critical_found = False

# Check rules
for line_number, code_line in enumerate(code_lines, start=1):

    for rule in rules:

        if rule["pattern"] in code_line:

            violations.append({
                "severity": rule["severity"],
                "pattern": rule["pattern"],
                "line": line_number,
                "code": code_line.strip()
            })

            if rule["severity"].lower() == "critical":
                critical_found = True


# Generate Report
print("\n" + "=" * 50)
print("CODE COMPLIANCE REPORT")
print("=" * 50)

if violations:

    print("\nVIOLATIONS FOUND\n")

    for violation in violations:

        print(f"Rule      : {violation['pattern']}")
        print(f"Severity  : {violation['severity']}")
        print(f"Line      : {violation['line']}")
        print(f"Code      : {violation['code']}")
        print("-" * 50)

else:

    print("\nNo violations found")
    print("\nSTATUS : PASS")

print("=" * 50)

# Pipeline Decision
if critical_found:
    print("\nSTATUS : FAILED")
    print("Critical violations found.")
    sys.exit(1)

elif violations:
    print("\nSTATUS : WARNING")
    print("Only warning violations found.")
    sys.exit(0)

else:
    print("\nSTATUS : PASSED")
    sys.exit(0)