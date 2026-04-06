# ----- Object Imports ----- #
from Utils.record import Record

# ----- Support Functions ----- #
def SJF_Keys(job):
    return (job["burst"],
            job["pid"])

# ----- Scheduling Functions ----- #
# SJF (Shortest Job First):
def SJF(jobs):
    time = 0
    gantt = []

    # [STEP 1]: Start a while loop until all jobs are finished.
    while jobs:
        available = []
        
        # [OPTION 1]: Find jobs that arrive before or at current 'time' & append them to the 'available' list.
        for job in jobs:
            if job["arrival"] <= time:
                available.append(job)

        # [OPTION 2]: If no jobs available, move 'time' forward to next 'arrival' time.
        if not available:
            fastforward = jobs[0]["arrival"]

            for job in jobs:
                if job["arrival"] < fastforward:
                    fastforward = job["arrival"]

            time = fastforward
            continue

        # [STEP 2]: Sort jobs by 'burst' time first, 'pid' second.
        available.sort(key = SJF_Keys)

        # [STEP 3]: Select job with shortest 'burst' time.
        job = available[0]

        # [STEP 4]: Run Calculate function from record.py in Utils folder.
        time = Record(job, time, gantt)

        # [STEP 5]: Remove the current job so it does not run again.
        jobs.remove(job)

    return gantt
        