import re
# A password must be:
# 1) Atleast 8 characters long.
# 2) Can have any alphabet in any case.
# 3) can include digits
# 4) must end with a digit
# 5) Should not include space
password_pattern = re.compile(r'[a-zA-Z0-9$%#@\S]{7,}\d')
password = 'noinenoine9'
print(password_pattern.fullmatch(password))
