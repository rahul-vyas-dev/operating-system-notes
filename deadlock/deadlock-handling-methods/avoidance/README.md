# Deadlock Avoidance

**Idea:**  
The system dynamically examines resource allocation to ensure it never enters an unsafe state.

---

## Banker's Algorithm
A well-known avoidance technique:
- Each process declares the maximum resources it may need.
- The system only grants requests if it results in a safe state.

**Safe State:** There exists at least one sequence of process execution such that every process can finish.

---

### Example

If granting a request leads to a state where one or more processes can’t complete, the system **waits** before allocating.

**Analogy:** Like a banker lending money only if they are sure all customers can repay eventually.

---

### Diagram
Safe State: Unsafe State:
P1 → P2 → P3 P1 → P2 (P3 starves)
