# enhance this program to use multi-processing
import time
import multiprocessing


def calculate_sum(start, end, result_queue):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    result_queue.put(sum)


if __name__ == "__main__":
    start_time = time.time()

    num_processes = multiprocessing.cpu_count()
    num_processes = 10
    chunk_size = 10_000_000
    start = 1
    end = chunk_size
    result_queue = multiprocessing.Queue()

    processes = []

    for i in range(num_processes):
        p = multiprocessing.Process(
            target=calculate_sum, args=(start, end, result_queue)
        )
        processes.append(p)
        p.start()

        start += chunk_size
        end += chunk_size

    for process in processes:
        process.join()

    sum = 0
    while not result_queue.empty():
        sum += result_queue.get()

    end_time = time.time()

    print("Sum of numbers from 1 to 100,000,000: ", sum)
    print(
        "Time taken to calculate the sum using multiprocessing: ",
        end_time - start_time,
        "seconds",
    )
