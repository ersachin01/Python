s = {1, 2, 3, 4, 5}

p = {2, "hello", 3.14, (1, 2, 3), frozenset({4, 5}) }       

e = set() # empty set
print(s)

s.add(6)
s.remove(3)
s.discard(10) # does not raise an error if the element is not present   
s.update({7, 8, 9}) 
s.union({10, 11, 12}) # returns a new set that is the union of s and the given set  
s.intersection({2, 4, 6, 8}) # returns a new set that is the intersection of s and the given set
s.difference({1, 2, 3}) # returns a new set that is the difference of s and the given set (elements that are in s but not in the given set)         
s.pop() # removes and returns an arbitrary element from the set (raises KeyError if the set is empty)
print(s)
print(p)        