# ----- Record Function ----- #
def Records(job, time, gantt):
    # Calculates the Start & End times.
    start = time
    end = start + job["burst"]

    # Add PID, Start time & End time to the 'gantt' list.
    gantt.append({"pid": job["pid"], 
                  "start": start, 
                  "end": end})
    
    # Create and add a 'completion' time to the job.
    job["completion"] = end
    time = end

    return time