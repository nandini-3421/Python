myset={12,78,34,78}
print(myset)

myset2={76,34,22}
print(myset2)
print(type(myset))

#union of two set using '|' operator
res=myset|myset2
print("the union of both the sets are",res)

#using union() method
res2=myset.union(myset2)
print("the union of both the sets is "res2)

#intersection of sets
res=myset & myset2
print(res)

res=myset.intersect(myset2)
print(res)

#set difference(-)
res=myset-myset2
print("the set difference is ",res)

