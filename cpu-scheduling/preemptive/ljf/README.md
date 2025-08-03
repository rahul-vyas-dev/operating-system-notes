
# Longest Job First – Preemptive (LRTF)

**Definition:**  
LRTF selects the process with the largest remaining burst time. If a process arrives with a longer burst time than the current one, it preempts.

---

**Example:**

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1      | 0            | 5          |
| P2      | 1            | 10         |
| P3      | 2            | 8          |

---

**Gantt Chart:**

| Time | 0 | 1 | 11 | 19 | 24 |
|------|---|---|----|----|----|
| Proc | P1| P2| P3 | P1 |    |

---

**Key Points:**
- Maximizes turnaround time.
- Can cause starvation for shorter processes.
