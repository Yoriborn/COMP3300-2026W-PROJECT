# ----- Object Imports ----- #
from Utils.records import Records

# ----- Support Functions ----- #
def SJF_Keys(job):
    return (job["burst"],
            job["pid"])

# ----- Scheduling Functions ----- #
# SJF (Shortest Job First):
def SJF(jobs):
    time = 0
    gantt = []

    # Loop until all jobs are finished.
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

        # Sort jobs by 'burst' time first, 'pid' second.
        available.sort(key = SJF_Keys)

        # Select job with shortest 'burst' time.
        job = available[0]

        # Run Calculate function from record.py in Utils folder.
        time = Records(job, time, gantt)

        # Remove the current job so it does not run again.
        jobs.remove(job)

    return gantt
        