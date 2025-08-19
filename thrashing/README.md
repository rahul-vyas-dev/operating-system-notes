# Thrashing in Operating System

## 🔹 What is Thrashing?
Thrashing is a situation in an operating system where the CPU spends most of its time **swapping pages in and out of memory** rather than executing instructions.  
It drastically reduces the system’s performance.

---

## 🔹 Why does Thrashing occur?
1. **High degree of multiprogramming** – Too many processes are competing for memory.
2. **Insufficient RAM** – The system is forced to use disk storage as memory.
3. **Poor Page Replacement Policy** – If frequently used pages are removed, page faults increase.

---

## 🔹 Example:
- Suppose a system has **2 GB RAM** but is running many processes requiring **4 GB of memory**.
- Due to shortage, OS keeps swapping pages from RAM to disk and vice versa.
- CPU executes fewer instructions and spends most of the time **paging** → performance drops.

---

## 🔹 Ways to Handle Thrashing
- **Reduce the degree of multiprogramming** (limit number of processes).
- **Use better page replacement algorithms** like LRU (Least Recently Used).
- **Increase physical memory (RAM)**.
- **Working Set Model** – OS only keeps the actively used pages of a process in memory.
