"""
RECORD CHECK  -  my version
===========================

Name  : naser
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# ==================================================================== INPUT

label=input("Please enter the hostname:   ")     
first=float(input("Please enter the GB used:  "))     
second=float(input("Please enter the Total GB: "))    
# ================================================================== PROCESS
difference=second-first

percent =first/second * 100


# =================================================================== OUTPUT
print("="*34)
print(f" RECORD CHECK  -  {label}")
print("="*34)

print(f"  Used is       : {first:>10.2f}")
print(f"  Total is      : {second:>10.2f}")
print(f"  Free is       : {difference:>10.2f}")
print(f"  Percent is    : {percent:>10.2f} %")

# report lines go here

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you