
# Longest Job First (LJF) – Non-Preemptive

## Overview
- **Type:** Non-preemptive  
- **Idea:** Process with the largest burst time executes first.  
- **Implementation:** Select longest job from ready queue.

---

## Example

| Process | Burst Time |
|---------|-----------|
| P1      | 5         |
| P2      | 8         |
| P3      | 2         |
| P4      | 10        |

**Order:** P4 → P2 → P1 → P3

---

## Gantt Chart

| P4 |----------10----------| P2 |--------8--------| P1 |-----5-----| P3 |-2-|
0 10 18 23 25

---

## Advantages
- Good for heavy CPU-bound jobs

## Disadvantages
- Starvation for short jobs
