
# Round Robin (RR)

**Definition:**  
Each process gets CPU for a fixed time quantum. After quantum expires, the process moves to the end of the queue if not finished.

---

**Example:**

| Process | Burst Time |
|---------|------------|
| P1      | 5          |
| P2      | 4          |
| P3      | 2          |
| Quantum | 2          |

---

**Gantt Chart:**

| Time | 0 | 2 | 4 | 6 | 8 | 10 | 11 |
|------|---|---|---|---|---|----|----|
| Proc | P1| P2| P3| P1| P2| P1 |    |

---

**Key Points:**
- Fair CPU allocation.
- Good for time-sharing systems.
- Quantum size impacts performance.
