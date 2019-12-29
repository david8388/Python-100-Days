s1 = 'hello world!'
s2 = "hello world!"

s3 = '''
hello
world
'''

print(s1, s2, s3, end='')

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'

print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u4f60\u597d'

print(s1, s2)

s1 = r'\'hello, world! \''
s2 = r'\n\\hello, world!\\\n'

print(s1, s2, end='')