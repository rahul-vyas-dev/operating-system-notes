# CPU Scheduling Algorithms

CPU Scheduling decides **which process gets the CPU** and for how long.

There are **two main types** of CPU Scheduling:

---

## Non-Preemptive Scheduling
- Once a process starts executing, it **cannot be interrupted** until it finishes.
- Suitable for **batch systems**.
- **Advantages:** Simple, no context switch overhead.
- **Disadvantages:** Poor response time for short processes.

### Algorithms:
1. [First Come First Serve (FCFS)](non-preemptive/fcfs)
2. [Shortest Job First - Non-Preemptive](non-preemptive/sjf)
3. [Longest Job First - Non-Preemptive](non-preemptive/ljf)
4. [Priority Scheduling - Non-Preemptive](non-preemptive/priority)
5. [Multilevel Queue Scheduling](non-preemptive/multilevel-queue)
6. [Highest Response Ration First](non-preemptive/hrrf)

**Example Gantt Chart (FCFS)**  
Processes:  
- **P1**: Arrival=0, Burst=5  
- **P2**: Arrival=1, Burst=3  
- **P3**: Arrival=2, Burst=1  

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
