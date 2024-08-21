def add(x, y):
    return x + y


print(add(1, 2))

# Anonymous functions: they aren't bound to an identifier "def"
# what's after ":" is what we return
add2 = lambda x, y: x + y
print(add2(1, 2))
print((lambda x, y: x + y)(1, 2))

"""
The point of this is that they're made to be passed into a higher-order function.
A higher-order is a function that can either take in another function as an input or return function as an output.
"""


def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        result.append(my_func(item))
    return result


nums = [3, 4, 5, 6, 7]

cubed = my_map(lambda x: x**3, nums)
cubed_map = map(lambda x: x**3, nums)

print(cubed)
print(list(cubed_map))
