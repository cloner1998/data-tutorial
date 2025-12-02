from timeit import timeit


def my_any(x):
    result = False
    for y in x:
        if y:
            result = True
    return result

a = %timeit -o my_any([1, 2, 3, 4])

print(a)