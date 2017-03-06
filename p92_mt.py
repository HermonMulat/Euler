import sys
import multiprocessing as mp
def process(n):
    digits = list(str(n))
    return sum((int(i)**2 for i in digits))
def ref_table(n):
    table = {1:1, 89:89}
    for i in range(1,n+1):
        num = i
        while(num not in table):
            num = process(num)
        table[i] = table[num]
    return table

def main(s,e,n,pid,return_vals):
    if (s==0):
        s = 1
    look_up = ref_table(81*n)
    counter = 0
    for i in range(s,e):
        if look_up[process(i)] == 89:
            counter += 1
    return_vals[i] = counter

if __name__ == '__main__':
    import time
    start_time = time.time()

    n = int(sys.argv[1])
    process_count = int(sys.argv[2])

    manager = mp.Manager()
    return_vals = manager.dict()

    gap = (10**n/process_count)

    processes = []
    print "About to strat creating processes"
    for i in range(process_count):
        s = i*gap
        e =(i+1)*gap
        countProcess = mp.Process(target=main,args=(s,e,n,i,return_vals))
        processes.append(countProcess)
        countProcess.start()
    print "Created all processes.\nNow waiting for processes to finish"
    for i in processes:
        i.join()

    print "\nFinal Answer:", sum(return_vals.values())
    print "Total time:",time.time()-start_time,"seconds"
