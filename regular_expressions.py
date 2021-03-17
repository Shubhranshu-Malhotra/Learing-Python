import re

string = 'Hi! This is me learning python! This is self learning. But this is extra.'

a = re.search('This',string)
print(a)
print(a.span())
print(a.start(), a.end())
print(a.group()) # Don't really understand its usage. 

pattern = re.compile('This')
pattern2 = re.compile('Hi! This is me learning python! This is self learning.')
b = pattern.search(string)
print(b)
print(pattern.findall(string))
print(pattern.fullmatch(string)) # Matches only if the exact same string
print(pattern2.fullmatch(string)) # Matches only if the exact same string
print(pattern2.match(string)) # Matches the exact string in pattern to one passed and doen't care if the passed string is different afterwards
