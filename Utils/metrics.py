# ----- Metircs Function ----- #
def Metrics(jobs):
    turnaround_time = {}
    waiting_time = {}

    # [STEP 1]: Go through each job and compute their Turnaround time & Waiting time.
    for job in jobs:
        # TAT = completion_time - arrival_time 
        turnaround = job["completion"] - job["arrival"]

        # WT = turnaround_time - burst_time
        waiting = turnaround - job["burst"]                     

        # Assign calculated TAT / WT to their PID.
        turnaround_time[job["pid"]] = turnaround
        waiting_time[job["pid"]] = waiting

    # [STEP 2]: Calculate the average Turnaround time & Waiting time for all jobs.
    avg_turnaround = sum(turnaround.values()) / len(jobs)
    avg_waiting = sum(waiting.values()) / len(jobs)

    # [STEP 3]: 
    return {
        "turnaround" : turnaround,
        "waiting" : waiting,
        "avg_turnaround" : round(avg_turnaround, 2),
        "avg_waiting" : round(avg_waiting, 2)
    }
