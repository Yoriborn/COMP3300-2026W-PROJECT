# COMP3300-2026W-PROJECT
Operating System Fundamentals...

Project Option 1: 
    CPU Scheduling Simulator

Explanation:
    By taking advantage of pythons object-oriented design, the project was broken down into several objects to maintain readability, 
    cleanliness, and modularity which was the "Design Decision" goal.

    The Schedulers folder holds all the scheduling policy algorithms (FIFO, SJF, Priority, and RR) while Utils folders holds code that was 
    reused (record.py) and the calculation code for the scheduling metrics (Waiting Time, Turnaround Time, and their averages).
    The main code (app.py) was left outside so it could easily communicate with both input.json and output.json
    This can be easily be seen as each object has an "Object Import" section so you know what and where said code is coming from.

    Each scheduling policy uses a "Support Function" to assist the introduction of a "Tie-Breaking policy" within its algorithm. This introduces 
    lexicographic ordering across the scheduling policies, primarily giving arrival times / burst times priority with PID reserved as a Tie-Breaker 
    when two jobs have equal primary values.
    - In FIFO, a Sort command is used in tandem with a Support Key that orders job by ARRIVAL_TIME First & PID Second so earlier jobs are
      selected first, with the smaller PID being a Tie-Breaker.
    - In SJF, a Sort command is used in tandem with a Support Key that orders job by BURST_TIME First & PID Second so shorter jobs are
      selected first, with the smaller PID being a Tie-Breaker.
    - In Priority, a Sort command is used in tandem with a Support Key that orders job by PRIORITY First, PID Second, so higher priority
      jobs are selected first, with the smaller PID being a Tie-Breaker.
    - In RR, a Sort command is used in tandem with a Support key that orders job by ARRIVAL_TIME First, PID Second, so earlier jobs are
      inserted into the queue first, with the smaller PID being a Tie-Breaker (Note, the FIFO-Queue takes over after sort).

    As per the Rubric, AI tools were accessible to be used to assist development.
    AI was used to help me with the RR algorithm. While I did understand the premise of Round Robin, I did not understand how to implement it into
    a coding (specifically python) format. After been giving a brief explanation (understanding a queue), I was then able to implement the 
    Round Robin algorithm into my code with a better understanding.

How-to-Run:
    python3 app.py < input.json > output.json

