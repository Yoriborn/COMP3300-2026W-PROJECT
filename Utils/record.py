# ----- Record Function ----- #
def Record(job, time, gantt):
    # [STEP 1]: Calculates the Start & End times.
    start = time
    end = start + job["burst"]

    # [STEP 2]: Append PID, Start time & End time to the 'gantt' list.
    gantt.append({"pid": job["pid"], 
                  "start": start, 
                  "end": end})
    
    # [STEP 3]: Create and add a 'completion' time to the job.
    job["completion"] = end
    time = end

    return time