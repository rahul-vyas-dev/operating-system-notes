# Microkernel

A **Microkernel** runs only the essential services (like CPU scheduling, memory management, and IPC) in kernel mode.  
Other services (drivers, file systems) run in user space.

## Advantages
- Better stability (crash in one service doesn’t crash the OS)
- Easier to maintain and extend

## Disadvantages
- Slower performance due to extra user-kernel communication

## Examples
- QNX
- MINIX
- L4
