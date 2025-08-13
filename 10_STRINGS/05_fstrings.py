# String formatting
template = "Dear {}, you are awesome. Take this {}$ bag"
a="John"
a1=10000
b="Jack"
b1=1000
c="Marie"
c1=300 

s1=template.format(a,a1)
print(s1)

print(f"{b}, you are awesome. Take this {b1}$ bag")