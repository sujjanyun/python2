# FOR LOOPS

# for a single item in a bunch of items - for every needle in a haystack
# (for a single entry in a list of entries)

power_rangers = ["Jason", "Trini", "Billy", "Zack", "Kim"]

# FOR A SINGULAR ITEM FROM A LIST OF ITEMS
for ranger in power_rangers:
    print(ranger)

# similar WHILE loop version:
index = 0
ranger = ""

while index < len(power_rangers):
    ranger = power_rangers[index]
    print(ranger)
    index += 1

# we are implicitely creating a variable called ranger 
# and the value of the ranger 
# we don't need to pay attention to the index,
# because a for loop will pluck things out?

# for each entry in power_rangers, create a new variable, ranger
# and assign the value of the entry in the list

for ranger in power_rangers:
    print(ranger)
    if ranger == "Zack":



# A NEW HOPE
