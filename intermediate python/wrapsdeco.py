from functools import wraps

def add_wrapping(item):
    @wraps(item)
    def wrapped_item():
        return 'please go away and {}'.format(str(item()))
    return wrapped_item

@add_wrapping
def wish():
    return 'bye'
print(wish.__name__)