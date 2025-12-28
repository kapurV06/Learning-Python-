names= ['jeff','garry','jill','samantha']
print(' ,'.join(names))
for name in names:
 #   statement = 'hello there '+name
    statement = ' '.join(['Hello there',name])
    print(statement)

who = 'gary'
how_many = 12
print('{} bought {} apples'.format(who, how_many))
