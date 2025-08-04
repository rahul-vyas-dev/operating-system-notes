# First Come First Serve (FCFS) – Non-Preemptive

## Overview
- **Type:** Non-preemptive  
- **Idea:** Processes are executed in the order they arrive in the ready queue.  
- **Implementation:** FIFO Queue.

---

## Example

| Process | Arrival Time | Burst Time |
|---------|--------------|-----------|
| P1      | 0            | 5         |
| P2      | 1            | 3         |
| P3      | 2            | 2         |

---

## Gantt Chart

| P1 |-----5-----| P2 |---3---| P3 |-2-|
0 5 8 10

---

## Advantages
- Easy to implement
- Fair for processes arriving earlier

## Disadvantages
- Convoy effect: Long process delays all others
