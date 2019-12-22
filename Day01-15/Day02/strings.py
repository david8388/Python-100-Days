str1 = 'hello world'

print('字串長度:', len(str1))
print('首字大寫', str1.title())
print('字串變大寫', str1.upper())

print('字串是否為大寫', str1.isupper())
print('字串是否以hello開頭', str1.startswith('hello'))
print('字串是否以hello結尾', str1.endswith('hello'))

print('字串是否以驚嘆號(!)開頭', str1.startswith('!'))
print('字串是否以驚嘆號(!)結尾', str1.endswith('!'))

# 弦承 to UTF8 \u5f26\u627f
str2 = '- David'
str3 = str1.title() + ' ' + str2.lower()
print(str3)