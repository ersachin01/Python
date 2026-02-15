#What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations?
print(len(s)) # Output: 2   

\
# Explanation: In Python, the integer 20 and the float 20.0 are considered equal when it comes to set membership, so they will not be added as separate elements. However, the string '20' is different and will be added to the set. Therefore, the set will contain two unique elements: 20 (or 20.0) and '20'.

