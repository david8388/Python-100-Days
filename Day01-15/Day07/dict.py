scores = {'David': 25, 'Chia': 40}
print(scores)

item = dict(one = 1, two = 2, three = 3)
item2 = dict(zip([1, 2, 3], '641'))
item3 = { num: num ** 2 for num in range(1, 10)}
print(item, item2, item3)

print(scores['David'])
print(scores['Chia'])

for key in scores:
    print(f'{key}: {scores[key]}')

## update element in dict

scores['David'] = 26
scores['Russ'] = 30
scores.update(james = 35, kobe = 40)
print(scores)

if 'Russ' in scores:
    print(scores['Russ'])

print(scores.get('james'))
print(scores.get('james', 60))

# delete item from dict
print(scores.popitem())
print(scores.popitem())
print(scores.pop('David', 100))
print(scores)

# clear dict

scores.clear()
print(scores)