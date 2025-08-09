# Deadlock Conditions in Operating Systems

For a deadlock to occur, these four conditions must **all** be present:

1. **Mutual Exclusion**
   - Only one process can access a resource at any given time.
   - Example: A printer can print only one document at a time.

2. **Hold and Wait**
   - A process is holding at least one resource and is waiting for additional resources.
   - Example: A process holds a file lock and waits for a printer.

3. **No Preemption**
   - A resource cannot be forcibly taken from a process; it must be released voluntarily.
   - Example: A thread using a CPU core is not forcibly stopped until it finishes.

4. **Circular Wait**
   - A closed chain of processes exists, where each process waits for a resource held by the next process in the chain.
   - Example: P1 → P2 → P3 → P1

**If any one of these conditions is eliminated, deadlock cannot occur.**
