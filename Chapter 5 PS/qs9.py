#Can you change the values inside a list which is contained in set S?  
s = {8, 7, 12, "Harry", [1,2]} 
 
 
  
#Ans: No, you cannot change the values inside a list that is contained in a set. 
# This is because sets in Python are unordered collections of unique elements, 
# and they do not allow mutable types like lists to be included as elements. 
# If you try to include a list in a set, it will raise a TypeError.