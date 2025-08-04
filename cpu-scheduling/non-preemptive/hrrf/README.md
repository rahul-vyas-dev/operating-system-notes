# Highest Response Ratio Next (HRRN)

## Overview
- **Type:** Non-preemptive  
- **Idea:** Process with highest response ratio executes first.  
- **Formula:**  
\[
RR = \frac{\text{Waiting Time} + \text{Burst Time}}{\text{Burst Time}}
\]

---

## Example

| Process | Burst Time | Waiting Time | Response Ratio |
|---------|-----------|--------------|----------------|
| P1      | 5         | 4            | 1.8            |
| P2      | 3         | 5            | 2.67           |
| P3      | 8         | 3            | 1.375          |

**Order:** P2 → P1 → P3

---

## Gantt Chart

| P2 |---3---| P1 |-----5-----| P3 |--------8--------|
0 3 8 16

---

## Advantages
- Reduces starvation
- Balances waiting time and burst time

## Disadvantages
- Requires frequent recalculation
