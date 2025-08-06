# Critical Section, Race Conditions & Synchronization Methods

## 🔹 Critical Section
The **Critical Section** is the part of a program where shared resources (data, files, memory) are accessed.  
Only **one process/thread** should execute inside the critical section at any time to avoid data inconsistency.

---

## 🔹 Race Condition
A **Race Condition** occurs when:
1. Two or more processes/threads try to access shared data at the same time.
2. The program's output depends on the **execution order**.

### Example
```c
// Pseudocode
shared_counter = 0

Thread1: shared_counter = shared_counter + 1
Thread2: shared_counter = shared_counter + 1
