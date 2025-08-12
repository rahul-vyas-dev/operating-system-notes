# Deadlock Prevention

**Idea:**  
Prevent deadlock by structurally negating at least one of the four necessary conditions for deadlock.

---

## Strategies

1. **Eliminate Mutual Exclusion**  
   - Make resources sharable where possible.  
   Example: Multiple processes reading the same file.

2. **Eliminate Hold and Wait**  
   - Require processes to request all required resources at once.  
   Drawback: Can cause low resource utilization.

3. **Eliminate No Preemption**  
   - Allow preemption of resources if the requested one is not available.  
   Example: CPU scheduling where a higher-priority process takes over.

4. **Eliminate Circular Wait**  
   - Impose a total ordering of resources and require processes to request in increasing order.

---

### Example Diagram
┌────────────┐ ┌────────────┐
│ Process P1 │────▶ │ Resource R1│
└────────────┘ └─────▲──────┘
│
┌─────┴──────┐
│ Resource R2│
└────────────┘

## By ordering resource requests, circular waits are avoided.


