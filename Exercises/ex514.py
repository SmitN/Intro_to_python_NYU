cities = ['Boston', 'Chicago', 'New York', 'Boston', 'Chicago', 'Boston']
cdict={}

for city in cities:
    if city not in cdict:
        cdict[city] = 0
    cdict[city] = cdict[city] + 1 
print(cdict)

