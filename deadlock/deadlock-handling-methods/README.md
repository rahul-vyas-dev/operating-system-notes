# Deadlock Handling Methods

Deadlock is a situation in which a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by another process.

This directory contains four common approaches to handle deadlocks in Operating Systems, each explained in a **separate folder**.

---

## Methods

1. **[Deadlock Prevention](./prevention/README.md)**  
   - Proactively design the system so deadlocks can never occur.

2. **[Deadlock Avoidance](./avoidance/README.md)**  
   - Make decisions at runtime to ensure the system never enters an unsafe state.

3. **[Deadlock Detection and Recovery](./detection-and-recovery/README.md)**  
   - Allow deadlocks to occur but detect them and take action to recover.

4. **[Deadlock Ignorance](./ignorance/README.md)**  
   - Simply ignore deadlocks and assume they are rare.

---

## Deadlock Conditions
For a deadlock to occur, **all** of these must hold simultaneously:
1. **Mutual Exclusion** – A resource is assigned to only one process at a time.
2. **Hold and Wait** – Processes holding resources can request additional resources.
3. **No Preemption** – Resources cannot be forcibly taken away.
4. **Circular Wait** – A closed chain of processes exists, each holding at least one resource needed by the next process.

Deadlock handling methods work by preventing, avoiding, detecting, or ignoring these conditions.
