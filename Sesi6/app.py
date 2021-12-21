# def my_generator():
#   print("Inside my generator")
#   yield 'a'
#   yield 'b'
#   yield 'c'

# for char in my_generator():
#   print(char)

# function --
# def square(nums):
#     result = []

#     for num in nums:
#         result.append(num * num)

#     return result

# a
# def square(nums):
#     for num in nums:
#         yield num * num


# nums =[1,2,3,4,5].__iter__()
# # print(next(square(nums)))
# # print(square(nums).__next__())
# # print(square(nums).__next__())
# # print(square(nums).__next__())

# for char in square(nums):
#   print(char)

# list comperhension
# square_nums = [y*y for y in [1, 2, 3, 4, 5]]
# square_nums = [y*4 for y in range(7)]
# print(square_nums)

# list comperhension to generator
# square_nums = (y*y for y in [1, 2, 3, 4, 5])
# print(next(square_nums))
# print(next(square_nums))
# print(next(square_nums))
# print(next(square_nums))
# print(next(square_nums))

# def my_generator():
#   print("Inside my generator")
#   yield 'a'
#   yield 'b'
#   yield 'c'

# generator = my_generator()
# print(next(generator))
# print(next(generator))
# print(next(generator))

# def counter_generator(low, high):
#     while low <= high:
#        yield low
#        low += 1

# for i in counter_generator(5,10):
#   print(i, end=' ')

# def infinite_sequence():
#     num = 1
#     while True:
#         yield num
#         num += 1

# for i in infinite_sequence():
#   print(i, end=" ")

# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()

# parent()

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     else:
#         return second_child

# first = parent(1)
# print(first())

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)
# say_whee()

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_whee():
#     print("Whee!")

# say_whee()

# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1)
waste_some_time(999)