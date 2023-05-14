import multiprocessing
import time

def worker(num):
    """작업 수행 함수"""    
    time.sleep(0.5)
    
    return f"worker -- {num}"
    
run_list = ['one', 'two', 'three', 'four', 'five']

if __name__ == "__main__":
    start = time.time()
    
    multiprocessing.freeze_support()
    
    my_threads = multiprocessing.cpu_count()

    pool = multiprocessing.Pool(processes=my_threads-1)

    # for i in range(100):
    #     pool.apply_async(worker, (i,))
    
    for s in pool.imap(worker, run_list):
        print(f"\rs = {s}", end='')
        
        
    pool.close()
    pool.join()
    print("--- End ---")


    end = time.time()

    elapsed_time = end - start

    print(f"end time is {elapsed_time}")

