
# Priority Scheduling – Non-Preemptive

## Overview
- **Type:** Non-preemptive  
- **Idea:** Higher-priority processes run first.  
- **Implementation:** Select process with highest priority.

---

## Example

| Process | Priority | Burst Time |
|---------|----------|-----------|
| P1      | 2        | 6         |
| P2      | 1        | 8         |
| P3      | 3        | 7         |

**Order:** P3 → P1 → P2  *(Higher number = higher priority)*

---

## Gantt Chart

| P3 |------7------| P1 |-----6-----| P2 |--------8--------|
0 7 13 21

---

## Advantages
- Executes important jobs first

## Disadvantages
- Starvation possible for low-priority processes
