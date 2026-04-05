# ----- Object Imports ----- #
from Schedulers.first_in_first_out import FIFO
from Schedulers.shortest_job_first import SJF
from Schedulers.round_robin import RR
from Schedulers.priority import P

from Utils.metrics import Metrics

# ----- Module Imports ----- #
import json

# ----- Main Functions ----- #
def Main():

    # [STEP 1]: Open and 'r' Read 'input.json'.
    with open("input.json", "r") as f:
        input = json.load(f)

    policy = input["policy"]
    jobs = input["jobs"]

    # [STEP 2]: Select scheduling policy.
    if policy == "FIFO":
        gantt = FIFO(jobs)

    elif policy == "SJF":
        gantt = SJF(jobs)

    elif policy == "RR":
        gantt = RR(jobs, input["quantum"])

    elif policy == "PRIORITY":
        gantt = P(jobs)

    else:
        raise ValueError
    
    # [STEP 3]: Run Metrics function from metrics.py in Utils folder.
    metrics = Metrics(jobs)

    # [STEP 4]: Create the output.
    output = {
        "policy": policy,
        "gantt" : gantt,
        "metrics": metrics
    }

    # [STEP 5]: Open and 'w' Write to 'output.json'.
    with open("output.json", "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    Main()