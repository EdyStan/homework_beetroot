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


@timer
def sum_of_primes_in_range(upper):
    sume = 0
    for num in range(upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                sume += num
    print(sume)


sum_of_primes_in_range(200000)
