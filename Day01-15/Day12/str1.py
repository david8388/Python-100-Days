
print('My brother \'s name is \'007')
print(r'My brother \'s name is \'007')

str1 = 'hello123world'

print('he' in str1)
print('her' in str1)

print(str1.isalpha()) # just letter
print(str1.isalnum()) # letter and num
print(str1.isdecimal())

print(str1[0:5].isalpha())
print(str1[5:8].isdecimal())

list = ['床前明月光', '疑是地上霜', '舉頭望明月', '低頭思故鄉']

print('-'.join(list))
setence = 'You go your way I will go mine'
word_list = setence.split()
print(word_list)
email = '   abc@gmail.com    '
print(email)
print(email.strip())
print(email.lstrip())
print(email.rstrip())
