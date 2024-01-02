from modules.heap import Heap
from modules.processor import Processor


def process(proc_kol, time_kol, times):
    ans = list()

    heap = Heap()
    for i in range(min(proc_kol, len(times))):
        heap.insert(Processor(i, 0, times[i]))
        ans.append([i, 0])

    for i in range(proc_kol, time_kol):
        cur_proc = heap.extract_min()
        cur_time = cur_proc.start + cur_proc.time
        heap.insert(Processor(cur_proc.index, cur_time, times[i]))
        ans.append([cur_proc.index, cur_time])

    return ans
