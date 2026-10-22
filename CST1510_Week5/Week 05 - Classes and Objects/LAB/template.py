"""
RECORD CHECK  -  my version
===========================

Name  :naserallah terkawi
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# ====================================================================== CLASS
# 1. Define a class called Record.

class Record:
    def __init__(self, label, value, limit):
        """Store the label, value and limit on this record."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on value vs limit."""
        percent = self.value / self.limit * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.

r1 = Record("R-001", 87.0, 100.0)
r2 = Record("R-002", 120.0, 100.0)
r3 = Record("R-003", 95.0, 100.0)

records = [r1, r2, r3]

for r in records:
    print(r.label, r.status())


# ==================================================================== OUTPUT
# 3. Print a report for each record.

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Value  : {record.value}")
    print(f"  Limit  : {record.limit}")
    print(f"  Status : {record.status()}")

    print("=" * 34)
