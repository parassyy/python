# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 19:52:22 2025

@author: paras
"""

fobj = open("marks.txt", "r")
while True:
    stud = fobj.readline()
    if stud == "":
        break

    stud = stud.strip()  # remove leading/trailing whitespace
    if stud == "":
        continue  # skip empty lines

    parts = stud.split()
    if len(parts) != 5:
        print(f"Skipping invalid line: {stud}")
        continue  # skip malformed lines

    rno, name, sub1, sub2, sub3 = parts
    total = int(sub1) + int(sub2) + int(sub3)
    avg = total / 3
    res = "PASS" if int(sub1) >= 40 and int(sub2) >= 40 and int(sub3) >= 40 else "FAIL"

    print(f'{rno}\t{name}\t{sub1}\t{sub2}\t{sub3}\t{total}\t{avg:.2f}\t{res}')

fobj.close()
