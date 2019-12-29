str1 = 'hello, world!'

print(len(str1))
print(str1.capitalize())
print(str1.title())
print(str1.upper())
print(str1.find('or'))
print(str1.find('shit'))

# index is familiar with find, but not found will get error.
# print(str1.index('or'))
# print(str1.index(('shit')))

print(str1.startswith('He'))
print(str1.startswith('hel'))
print(str1.endswith('!'))
print(str1.center(50, '*'))
print(str1.rjust(50, ' '))

str2 = 'abc123456'

print(str2.isdigit())
print(str2.isalpha())
print(str2.isalnum())

str3 = ' xxx@gmail.com '
print(str3.strip())