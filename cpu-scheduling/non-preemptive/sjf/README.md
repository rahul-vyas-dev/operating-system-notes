# Shortest Job First (SJF) – Non-Preemptive

## Overview
- **Type:** Non-preemptive  
- **Idea:** Process with the smallest burst time executes first.  
- **Implementation:** Select shortest job from ready queue.

---

## Example

| Process | Burst Time |
|---------|-----------|
| P1      | 6         |
| P2      | 8         |
| P3      | 7         |
| P4      | 3         |

**Order:** P4 → P1 → P3 → P2

---

## Gantt Chart

| P4 |-3-| P1 |-----6-----| P3 |------7------| P2 |--------8--------|
0 3 9 16 24

---

## Advantages
- Minimizes average waiting time

## Disadvantages
- Starvation possible for long jobs

