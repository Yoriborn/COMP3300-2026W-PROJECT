# ----- Support Function ----- #
def RR_Keys(job):
    return (job["arrival"],
            job["pid"])

# ----- Scheduling Function ----- #
# RR (Round Robin):
def RR(jobs, quantum):
    time = 0
    gantt = []
    queue = []

    # [STEP 1]: Sort jobs by 'arrival' time first, 'pid' second.
    jobs.sort(key = RR_Keys)

    # [STEP 2]: Go through each job and track the remaining burst time.
    remaining = {}
    for job in jobs:
        remaining[job["pid"]] = job["burst"]

    # [STEP 4]: Start a while loop there are jobs are finished.
    i = 0
    while queue or i < len(jobs):

        # [4.1]: Find jobs that arrived before current 'time' & append them to the 'queue' list.
        while i < len(jobs) and jobs[i]["arrival"] <= time:
            queue.append(jobs[i])
            i += 1

        # [4.2]: If no jobs available, move 'time' forward to next 'arrival' time.
        if not queue:
            time = jobs[i]["arrival"]
            continue

        # [4.3]: Pop the next job from the 'queue' list.
        job = queue.pop(0)

        # [4.4]: Run the remaining 'quantum' time.
        if remaining[job["pid"]] <= quantum:
            run = remaining[job["pid"]]
        else:
            run = quantum

        # [4.5]: Calculates the Start & End times.
        start = time
        end = time + run
        
        # [4.6]: Append PID, Start time & End time to the 'gantt' list.
        gantt.append({"pid": job["pid"], 
                      "start": start, 
                      "end": end})
        
        # [4.7]: Update the Remaining & Current times.
        remaining[job["pid"]] -= run
        time = end

        # [4.8]: Start a while loop to arrive new jobs that arrived during the execution.
        while i < len(jobs) and jobs[i]["arrival"] <= time:
            queue.append(jobs[i])
            i += 1

        # [4.9]: If current job did not finish, append it back into the 'queue' list.
        if remaining[job["pid"]] > 0:
            queue.append(job)
        else:
            job["completion"] = time

    return gantt