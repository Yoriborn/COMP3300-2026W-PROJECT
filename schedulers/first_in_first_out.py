# ----- Object Imports ----- #
from utilitys.helper import Help

# ----- Support Functions ----- #
def FIFO_Keys(job):
    return (job["arrival"], 
            job["pid"])

# ----- Scheduling Functions ----- #
# FIFO (First-in, First-Out):
def FIFO(jobs):
    time = 0
    gantt = []

    # [STEP 1]: Sort jobs by 'arrival' time first, 'pid' second.
    jobs.sort(key = FIFO_Keys)
    
    # [STEP 2]: Go through each job.
    for job in jobs:

        # [STEP 3]: Jump forward to next job if idle.
        if time < job["arrival"]:
            time = job["arrival"]

        # [STEP 4]: Run Help function from utilitys.
        time = Help(job, time, gantt)

    return gantt
