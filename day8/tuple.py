tup =("tuple","is","awesome")
#length = tuple((len(word)for word in tup))
l=[]
for word in tup:
    l.append(len(word))
tupl =tuple(l)
print(tupl)