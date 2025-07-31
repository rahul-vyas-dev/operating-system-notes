# Process in Operating Systems

A **process** is a program in execution.  
It is an independent unit that has its own:
- Memory space
- CPU registers
- Program counter
- Stack and heap

## Key Points
- Each process has a separate memory address space.
- Processes do not share memory by default.
- Managed by the OS scheduler.

## Process Lifecycle
1. New → Created
2. Ready → Waiting for CPU
3. Running → Executing
4. Waiting → Waiting for I/O
5. Terminated → Finished execution

## Example
When you open Chrome and VS Code separately, each runs as a process.

## Advantages
- Isolation between tasks
- Stability (one process crash doesn’t affect others)

## Disadvantages
- More resource usage
- Slower context switching compared to threads
