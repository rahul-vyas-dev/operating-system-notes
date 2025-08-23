# Shared Memory

## What is Shared Memory?
Shared Memory is a portion of memory **shared among multiple processes**.  
Processes can directly **read/write** to this memory area.

- **Fastest IPC method**
- Requires **synchronization tools** like semaphores to prevent conflicts.

## Example
Two processes updating a shared scoreboard in a game.

## Analogy
A **whiteboard in a classroom** where any student can write or read.
