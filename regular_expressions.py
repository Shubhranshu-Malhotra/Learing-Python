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

pattern3 = re.compile(r'([a-zA-Z]).([a])')
x = pattern3.search(string)
print(x)
print(x.group(1))
print(x.group(2))

pattern4 = re.compile(r'^Hi')
print(pattern4.search(string))

# Email checker
email_pattern = re.compile(r"^[a-zA-Z0-Z._]+@[a-zA-Z-]+\.[a-zA-Z]+")
email = 's@gmail.com'

print(email_pattern.search(email))