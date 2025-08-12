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
1. [Shortest Job First - Preemptive (SRTF)](preemptive/sjf)
2. [Longest Job First - Preemptive (SRTF)](preemptive/ljf)
3. [Priority Scheduling - Preemptive](preemptive/priority)
4. [Round Robin (RR)](preemptive/round-robin)
5. [Multilevel Feedback Queue Scheduling](preemptive/multilevel-feedback-queue)

---

📊 **Example Gantt Chart (Round Robin)**  
Example processes:  
- **P1**: Burst=5  
- **P2**: Burst=3  
- **P3**: Burst=6  
- **Quantum**: 2  

```mermaid
gantt
    dateFormat  X
    title Preemptive (Round Robin) Gantt Chart Example
    section Processes
    P1 :a1, 0, 2
    P2 :a2, 2, 4
    P3 :a3, 4, 6
    P1 :a4, 6, 8
    P3 :a5, 8, 10
    P3 :a6, 10, 12
