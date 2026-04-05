# ----- Object Imports ----- #
from Schedulers.first_in_first_out import FIFO
from Schedulers.shortest_job_first import SJF
from Schedulers.round_robin import RR
from Schedulers.priority import P

from Utils.metrics import Metrics

# ----- Module Imports ----- #
import json
import sys
import copy

# ----- Main Functions ----- #
def Main():
    data = json.load(sys.stdin)

    policy = data["policy"]
    jobs = data["jobs"]

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
        "gantt" : gantt,
        "metrics": metrics
    }

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    Main()