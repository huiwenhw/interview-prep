class memoize(dict):
    def __init__(self, func):
        print('self ', self)
        self.func = func

    def __call__(self, *args):
        print 'called with ', args
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        print 'missing key ', key, ' result ', result, ' self[key] ', self[key], ' self.func(*key) ', self.func(*key)
        return result

@memoize
def foo(a, b):
    return a * b

print('calling foo(2, 4) ', foo(2, 4)) # 8
print(foo) # {(2, 4): 8}
print(foo('hi', 3)) # hihihi
print(foo) # {(2, 4): 8, ('hi', 3): 'hihihi'}
print(foo(2, 4)) # 8

def simple_decorator(decorator):
    '''This decorator can be used to turn simple functions
    into well-behaved decorators, so long as the decorators
    are fairly simple. If a decorator expects a function and
    returns a function (no descriptors), and if it doesn't
    modify function attributes or docstring, then it is
    eligible to use this. Simply apply @simple_decorator to
    your decorator and it will automatically preserve the
    docstring and function attributes of functions to which
    it is applied.'''
    def new_decorator(f):
        g = decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g
    # Now a few lines needed to make simple_decorator itself
    # be a well-behaved decorator.
    new_decorator.__name__ = decorator.__name__
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)
    return new_decorator

#
# Sample Use:
#
@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print 'calling {}'.format(func.__name__)
        return func(*args, **kwargs)
    return you_will_never_see_this_name

@my_simple_logging_decorator
def double(x):
    'Doubles a number.'
    return 2 * x

assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'
print double(155)
