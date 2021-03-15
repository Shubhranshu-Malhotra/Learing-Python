# Get the duplicate characters list from thegiven  list

some_list = ['a', 'b', 'c', 'b', 'd', 'a']

duplicates = list({x for x in some_list if some_list.count(x)>1 })

print(duplicates)