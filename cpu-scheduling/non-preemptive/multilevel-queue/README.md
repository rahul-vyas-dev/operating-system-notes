
# Multilevel Queue Scheduling

## Overview
- **Type:** Can be preemptive or non-preemptive  
- **Idea:** Ready queue divided into multiple queues based on process type.  
- **Implementation:** Each queue has its own scheduling algorithm.

---

## Example Structure

1. **Foreground Queue** – Round Robin
2. **Background Queue** – FCFS

Higher-priority queues always execute first.

---

## Advantages
- Organizes processes efficiently

## Disadvantages
- Starvation possible for lower queues

---

## Note
Since it's a queue system, Gantt chart depends on the chosen algorithms per queue.
