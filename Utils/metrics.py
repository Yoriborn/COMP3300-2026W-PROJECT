# ----- Metircs Function ----- #
def Metrics(jobs):
    turnaround_time = {}
    waiting_time = {}

    # [STEP 1]: Go through each job and compute their Turnaround time & Waiting time.
    for job in jobs:
        # TAT = completion_time - arrival_time 
        tat = job["completion"] - job["arrival"]

        # WT = turnaround_time - burst_time
        wt = tat - job["burst"]                     

        # Assign calculated TAT / WT to their PID.
        turnaround_time[job["pid"]] = tat
        waiting_time[job["pid"]] = wt

    # [STEP 2]: Calculate the average Turnaround time & Waiting time for all jobs.
    avg_turnaround = sum(turnaround_time.values()) / len(jobs)
    avg_waiting = sum(waiting_time.values()) / len(jobs)

    return {
        "turnaround" : turnaround_time,
        "waiting" : waiting_time,
        "avg_turnaround" : round(avg_turnaround, 2),
        "avg_waiting" : round(avg_waiting, 2)
    }
