# Deadlock Prevention

Deadlock prevention works by **ensuring at least one of the necessary conditions cannot hold**.

## Methods:
1. **Eliminate Mutual Exclusion**
   - Make resources sharable if possible.
   - Example: Use spooling instead of locking a printer.

2. **Eliminate Hold and Wait**
   - Require processes to request all resources at once before starting.
   - Problem: Leads to low resource utilization.

3. **Eliminate No Preemption**
   - Allow resources to be forcibly taken away if needed.
   - Example: Preempt CPU time from a process.

4. **Eliminate Circular Wait**
   - Impose a strict ordering on resource requests.
   - Example: Always request resources in the order R1 → R2 → R3.
