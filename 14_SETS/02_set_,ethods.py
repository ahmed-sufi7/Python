s = {3, 23, 2 , 11}
 
s.add(32)
print(s)

s.add(342)
print(s)

s.remove(3)
print(s)

s.remove(32442)  # This will raise a KeyError because 32442 is not in the set
s.discard(32442)  # This will not raise an error and only remove if present