name = "Harry"
#       -5-4-3-2-1 
#        H A R R Y
#        0 1 2 3 4
print(name[0])
print(name[-1])
print(name[-3]) # Name[-3+5] = Name[2]

#slicing 
print(name[1:5]) #end with one number before
print(name[2:-1])


one="Harry0123456789"
# print(one[0:10:n]) #Skips n-1 characters
print(one[0:10:1]) #skip 0 characters
print(one[0:10:2]) #skip 1 character
print(one[0:10:3]) #skip 2 characters

print(one[:4]) #equivalent to one[0:4] 
print(one[0:]) #equivalent to one[0:-1]