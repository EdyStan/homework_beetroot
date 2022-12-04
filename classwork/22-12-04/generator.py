def my_range(start, end, step=1):
    while True:
        if start >= end and step > 0 or start <= end and step < 0:
            break
        yield start
        start += step

