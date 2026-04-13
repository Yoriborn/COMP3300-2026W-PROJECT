# ----- Object Imports ----- #
from Utils.records import Records

# ----- Support Functions ----- #
def FIFO_Keys(job):
    return (job["arrival"], 
            job["pid"])

# ----- Scheduling Functions ----- #
# FIFO (First-in, First-Out):
def FIFO(jobs):
    time = 0
    gantt = []

    # Sort jobs by 'arrival' time first, 'pid' second.
    jobs.sort(key = FIFO_Keys)
    
    # Complete jobs until none left.
    for job in jobs:

        # Jump forward to next job if idle.
        if time < job["arrival"]:
            time = job["arrival"]

        # Run Calculate function from record.py in Utils folder.
        time = Records(job, time, gantt)

    return gantt
