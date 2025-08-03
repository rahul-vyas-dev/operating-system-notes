
# Shortest Job First – Preemptive (SRTF)

**Definition:**  
SRTF selects the process with the smallest remaining burst time for execution. It’s the preemptive form of SJF, meaning the running process can be interrupted if a shorter job arrives.

---

**Example:**

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1      | 0            | 6          |
| P2      | 1            | 8          |
| P3      | 2            | 7          |
| P4      | 3            | 3          |

---

**Gantt Chart:**

| Time | 0 | 3 | 6 | 13 | 21 |
|------|---|---|---|----|----|
| Proc | P1| P4| P1| P3 | P2 |

---

**Key Points:**
- Minimizes average waiting time.
- May cause starvation for longer processes.
