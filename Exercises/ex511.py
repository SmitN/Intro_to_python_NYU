FILENAME='revenue.txt'
dict={}

fh = open(FILENAME)
for items in fh:
    items = items.split(",")
    name = items[0]
    dec = float(items[-1])
    dict[name] = dec
print(dict)

