# CPU Scheduling Time Periods

In CPU Scheduling, several important **time parameters** are used to measure performance and efficiency.

This section covers:
1. [Arrival Time](arrival-time)
2. [Burst Time](burst-time)
3. [Completion Time](completion-time)
4. [Turnaround Time](turnaround-time)
5. [Waiting Time](waiting-time)

Click on each to see definitions, formulas, and examples.

Below is a visual representation of CPU scheduling time parameters.

```mermaid
gantt
    dateFormat  X
    title CPU Scheduling Time Chart
    section Process P1
    Arrival Time :a1, 0, 0
    Waiting      :a2, 0, 2
    Execution    :a3, 2, 6
    Completion   :a4, 6, 6

    section Process P2
    Arrival Time :b1, 1, 1
    Waiting      :b2, 6, 7
    Execution    :b3, 7, 10
    Completion   :b4, 10, 10   
