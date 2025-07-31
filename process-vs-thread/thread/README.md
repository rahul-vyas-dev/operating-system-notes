# Thread in Operating Systems

A **thread** is the smallest unit of execution within a process.  
Multiple threads can exist inside a single process and share:
- Code segment
- Data segment
- OS resources

## Key Points
- Threads share memory within a process.
- Lighter and faster to create than processes.
- Used for parallelism.

## Example
When Chrome loads multiple tabs, each tab may run as a thread in the same Chrome process.

## Advantages
- Faster context switching
- Efficient communication between threads

## Disadvantages
- No isolation (a crash in one thread can affect the process)
- Requires careful synchronization
