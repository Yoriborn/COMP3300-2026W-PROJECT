# ----- Object Imports ----- #
from schedulers.first_in_first_out import FIFO
from schedulers.shortest_job_first import SJF
from schedulers.round_robin import RR
from schedulers.priority import P

# ----- Module Imports ----- #
import json
import sys

# ----- Main Functions ----- #
def Metrics(jobs):
    turnaround = {}
    waiting = {}

    for job in jobs:
        TAT = job["completion"] - job["arrival"]    # TAT = Turnaround Time
        WT = TAT - job["burst"]                     #  WT = Waiting Time

        turnaround[job["pid"]] = TAT
        waiting[job["pid"]] = WT

    avg_TAT = sum(turnaround.values()) / len(jobs)
    avg_WT = sum(waiting.values()) / len(jobs)

    return {
        "turnaround" : turnaround,
        "waiting" : waiting,
        "avg_turnaround" : round(avg_TAT, 2),
        "avg_waiting" : round(avg_WT, 2)
    }

def Main():
    data = json.load(sys.stdin)

    policy = data["policy"]
    jobs = data["jobs"]

    import copy
    process = copy.deepcopy(jobs)

    if policy == "FIFO":
        gantt = FIFO(process)
    elif policy == "SJF":
        gantt = SJF(process)
    elif policy == "RR":
        gantt = RR(process, data["quantum"])
    elif policy == "PRIORITY":
        gantt = P(process)
    else:
        raise ValueError
    
    metrics = Metrics(process)

    output = {
        "policy": policy,
        "gantt" : gantt[:2],
        "metrics": metrics
    }

    print(json.dumps(output, indent=2, separators=(',', ': ')))

if __name__ == "__main__":
    Main()