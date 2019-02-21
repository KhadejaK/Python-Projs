# 
# Khadeja Khalid
# CIS 41A Spring 2018
# Take-home assignment C
#

import re

#Part 1
line = input("Please input: ")

vowel = re.compile(r"^[a|e|i|o|u]")
result = vowel.search(line)

if result:
    print(line)
else:
    print("Does not begin with vowel")
    
#Part2
lines = input("Please input: ")
while (lines != "Q"):

    vowels = re.compile(r"^[a|e|i|o|u]")
    results = vowels.search(lines)

    if results:
        print(lines)
    else:
        print("Does not begin with vowel")
    lines = input("Please input: ")
    
'''
Unit C take home part

aEnd = re.compile(r"a$")
aSeq = re.compile(r"a{2,4}")
ab = re.compile(r"[ab]")
noab = re.compile(r"[^ab]")
abc = re.compile(r"abc")
noEmp = re.compile(r".")
period = re.compile(r"[.]")
wordChar = re.compile(r"\w")

line = input("Please input: ")
if aEnd.search(line):
    print("'a' at end")
if aSeq.search(line):
    print("'a' 2-4 times")
if ab.search(line):
    print("contains a or b")
if noab.search(line):
    print("contains something besides a or b")
if abc.search(line):
    print("contains 'abc'")
if noEmp.search(line):
    print("not empty")
if period.search(line):
    print("contains '.'")
if wordChar.search(line):
    print("contains word character")
'''