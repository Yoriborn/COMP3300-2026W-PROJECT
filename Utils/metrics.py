# ----- Metircs Function ----- #
def Metrics(jobs):
    turnaround_time = {}
    waiting_time = {}

    # Go through each job and compute their Turnaround time & Waiting time.
    for job in jobs:
        tat = job["completion"] - job["arrival"]
        wt = tat - job["burst"]                     

        # Assign calculated TAT / WT to their PID.
        turnaround_time[job["pid"]] = tat
        waiting_time[job["pid"]] = wt

    # Calculate the average Turnaround time & Waiting time for all jobs.
    avg_turnaround = sum(turnaround_time.values()) / len(jobs)
    avg_waiting = sum(waiting_time.values()) / len(jobs)

    return {
        "turnaround" : turnaround_time,
        "waiting" : waiting_time,
        "avg_turnaround" : round(avg_turnaround, 2),
        "avg_waiting" : round(avg_waiting, 2)
    }
