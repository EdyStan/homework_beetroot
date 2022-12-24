# Find the largest palindrome made from the product of two 3-digit numbers
import multiprocessing as mp
import time


def find_highest_4_digit_palindrome():
    highest_num = 0
    for num_1 in range(1001, 10000):
        for num_2 in range(num_1, 10000):
            stud_num = str(num_1*num_2)
            if stud_num == stud_num[::-1]:
                highest_num = stud_num
    return int(highest_num)


if __name__ == "__main__":
    pool = mp.Pool()
    start_time = time.perf_counter()

    processes = []
    for _ in range(4):  # change the number
        p = mp.Process(target=find_highest_4_digit_palindrome)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time - start_time} seconds")
