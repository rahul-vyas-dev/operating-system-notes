# Deadlock Detection and Recovery

**Idea:**  
Allow deadlocks to occur but have mechanisms to detect and recover.

---

## Detection
- Use **Wait-for Graphs** for single-instance resources.
- Use **Banker-like algorithms** for multiple-instance resources.

**Wait-for Graph:** Nodes represent processes, and an edge from P1 to P2 means P1 is waiting for a resource held by P2.

---

## Recovery
1. **Process Termination**  
   - Abort all deadlocked processes.
   - Abort one at a time until deadlock is resolved.

2. **Resource Preemption**  
   - Take resources from some processes and give them to others.

---

### Example Diagram
P1 → P2 → P3 → P1 (Cycle Detected) → Deadlock
