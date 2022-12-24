from PIL import Image
import threading


def timer(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return to_execute

    return inner


def factorial(n):
    n = int(n)
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    # print(fact)


@timer
def repeat_factorial_func(n):
    for i in range(1, n+1):
        factorial(i)


@timer
def repeat_factorial_func_with_threads(n):
    for i in range(1, n+1):
        x = threading.Thread(factorial(i))
        x.start()
        x.join()


import requests


def make_a_request_to_python_org():
    r = requests.get('https://www.python.org/')
    # print(r.status_code)
    # x = r.status_code


@timer
def repeat_req_func(n):
    for _ in range(n):
        make_a_request_to_python_org()


@timer
def repeat_req_func_with_threads(n):
    for _ in range(n):
        x = threading.Thread(make_a_request_to_python_org())
        x.start()
        x.join()


if __name__ == '__main__':
    repeat_factorial_func(50)
    repeat_factorial_func_with_threads(50)
    repeat_req_func(50)
    repeat_req_func_with_threads(50)
