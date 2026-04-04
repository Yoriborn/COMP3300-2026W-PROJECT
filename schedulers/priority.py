# ----- Object Imports ----- #
from utilitys.record import Help

# ----- Support Function ----- #
def P_Keys(job):
    return (job["priority"],
            job["pid"])

# ----- Scheduling Function ----- #
# P (Priority):
def P(jobs):
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
            fastfoward = jobs[0]["arrival"]

            for job in jobs:
                if job["arrival"] < fastfoward:
                    fastfoward = job["arrival"]

            time = fastfoward
            continue

        # [STEP 2]: Sort jobs by 'priority' number first, 'pid' second.
        available.sort(key = P_Keys)

        # [STEP 3]: Select the job with the lowest 'priority' number.
        job = available[0]

        # [STEP 4]: Run Help function from utilitys.
        time = Help(job, time, gantt)

        # [STEP 5]: Remove the current job so it does not run again.
        jobs.remove(job)

    return gantt