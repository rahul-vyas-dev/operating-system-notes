# Monolithic Kernel

A **Monolithic Kernel** includes all OS services inside the kernel space.  
This means file system management, device drivers, memory management, and CPU scheduling run directly in kernel mode.

## Advantages
- High performance (no extra context switches)
- Direct communication between components

## Disadvantages
- Larger size → more complex
- A bug in one service can crash the whole OS

## Examples
- Linux Kernel
- UNIX Kernel
