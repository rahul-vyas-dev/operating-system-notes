# Ready State

In the **Ready** state, the process is loaded into memory and waiting for CPU time.

## Key Points
- All resources except CPU are allocated.
- Process waits in the **ready queue**.
- CPU scheduler decides which ready process to execute next.

## Example
Multiple programs open at once but only one is currently running on the CPU.

## Transition
- From **Ready** → **Running**: When the CPU is assigned to the process.
