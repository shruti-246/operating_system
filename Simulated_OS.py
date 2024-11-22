import csv
from collections import deque

#process class
class Process:
    def __init__(self, pro_id, pro_time, res_need, acq_time):
        self.pro_id = pro_id
        self.pro_time = pro_time
        self.res_need = res_need
        self.acq_time = acq_time
        self.state = "ready"  # states: ready, waiting, blocked

#resource Control Block class
class ResControl:
    def __init__(self, res_name):
        self.res_name = res_name
        self.allocated = False
        self.wait_list = deque()  # Use deque for efficient queue operations
        self.res_time = 0

#reading processes from the file
def read_processes(file):
    processes = []
    with open(file, newline='') as file1:
        line = csv.DictReader(file1)
        for row in line:
            pro = Process(int(row['pro_id']),
                              int(row['pro_time']),
                              row['res_need'],
                              int(row['acq_time']))
            processes.append(pro)
    return processes

#resource acquisition
def res_acq(pro, resources, curr_time):
    for res in resources:
        if pro.curr_time >= pro.acq_time and pro.res_need == res.res_name:
            if res.allocated: #if the resource is not available then add the process to waiting list
                res.wait_list.append(pro)
                pro.state = "waiting"
            else: #if the resource is available then allocate it to the process
                res.allocated = True
                pro.state = "blocked"
                res.res_time = 10  #setting resource timer

#managing resource timers
def resource_times(resources):
    for res in resources:
        if res.allocated:
            res.res_time -= 1
            if res.res_time <= 0:
                res.allocated = False
                if res.wait_list: #allocating the resource to the next waiting process
                    next_pro = res.wait_list.popleft()
                    next_pro.state = "blocked"
                    res.allocated = True
                    res.res_time = 10

#process scheduling
def silumate_process(processes, resources):
    curr_time = 0
    while processes:
        print(f"Time: {curr_time}")
        for pro in processes[:]:
            if pro.pro_time > 0:
                pro.curr_time = curr_time
                res_acq(pro, resources, curr_time)
                if pro.state == "blocked":
                    print(f"Process {pro.pro_id} is blocked, needs {pro.res_need}.")
                else:
                    print(f"Process {pro.pro_id} is running.")
                    pro.pro_time -= 1
            if pro.pro_time == 0:
                processes.remove(pro)
        resource_times(resources)
        curr_time += 1

def main():
    resources = [ResControl('Resource0'), ResControl('Resource1')]
    processes = read_processes('pro.csv')
    silumate_process(processes, resources)

if __name__ == "__main__":
    main()
