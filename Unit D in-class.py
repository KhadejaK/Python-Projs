# 
# Khadeja Khalid
# CIS 41A Spring 2018
# In-class assignment D

#Part 1

for i in reversed(range(0, 11, 2)):
    print(i)
    
for i in range(10, -1, -2):
    print(i)
    
#Part 2
import re
quote = "I think that I shall never see a poem lovely as a tree. - Joyce Kilmer"

vowel = re.compile(r"\b\w*?[aeiouAEIOU]")

results = vowel.findall(quote)
    
c = ", ";

print(c.join(results))