#Check that a tuple type cannot be changed in python.

tuple1 = (1, 2, 3, 4, 5)

tuple1[0] = 10  
# This will raise a TypeError because tuples are immutable and do not support item assignment.