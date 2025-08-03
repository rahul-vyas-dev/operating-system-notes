
# Multilevel Feedback Queue Scheduling

**Definition:**  
Uses multiple queues with different priorities and scheduling rules. Processes can move between queues based on execution history.

---

**Example Queues:**
- Queue 1: Round Robin (Quantum = 2)
- Queue 2: Round Robin (Quantum = 4)
- Queue 3: FCFS

---

**Example Execution:**

| Time | 0 | 2 | 4 | 8 | 12 |
|------|---|---|---|---|----|
| Proc | P1| P2| P1| P3 | P4 |

---

**Key Points:**
- Flexible and efficient.
- Reduces starvation by moving processes between queues.
