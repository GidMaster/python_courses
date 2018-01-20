from functools import partial

def func(group, year, name):
    return name, group, year

group_func = partial(func, '433-2', '2016')

print(group_func('Ivan'))
print(group_func('Peter'))
