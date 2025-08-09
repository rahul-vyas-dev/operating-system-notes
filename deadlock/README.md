# Deadlock in Operating Systems

## Overview
A **deadlock** is a state where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.

### Example
Two processes (P1 and P2) each hold one resource and wait for the other’s resource. Neither can proceed → Deadlock.

---

## Four Necessary Conditions
1. **Mutual Exclusion** – Only one process can use a resource at a time.
2. **Hold and Wait** – A process is holding at least one resource and waiting for others.
3. **No Preemption** – Resources cannot be forcibly taken away.
4. **Circular Wait** – A closed chain exists where each process waits for a resource held by the next.

---

## Handling Deadlocks
- **Prevention** – Design the system to avoid at least one necessary condition.
- **Avoidance** – Use algorithms like Banker’s Algorithm to ensure safe states.
- **Detection and Recovery** – Allow deadlock but detect it and recover.
