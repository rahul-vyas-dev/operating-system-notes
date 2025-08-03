
# Priority Scheduling – Preemptive

**Definition:**  
Processes are scheduled according to priority. Higher priority runs first. If a higher-priority process arrives, it preempts.

---

**Example:**

| Process | Burst Time | Priority (Lower = Higher) |
|---------|------------|---------------------------|
| P1      | 2          | 3                         |
| P2      | 1          | 1                         |
| P3      | 8          | 2                         |

---

**Gantt Chart:**

| Time | 0 | 1 | 3 | 11 |
|------|---|---|---|----|
| Proc | P2| P1| P3|    |

---

**Key Points:**
- Preemptive and non-preemptive versions exist.
- Aging can prevent low-priority starvation.
