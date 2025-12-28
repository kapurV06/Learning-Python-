def add_wrapping(item):
 def wrapped_item():
    return 'i want a {} this christmas'.format(str(item()))
 return wrapped_item 

@add_wrapping
def wish():
  return 'loaded one'

print(wish())
print(wish.__name__)