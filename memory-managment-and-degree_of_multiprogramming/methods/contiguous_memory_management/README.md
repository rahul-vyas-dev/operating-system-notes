#  Contiguous Memory Allocation in Operating Systems

##  Introduction
In **Operating Systems**, memory management is a critical task that decides how processes are stored in RAM.  
One of the simplest memory allocation techniques is **Contiguous Memory Allocation**, where **each process is assigned a single continuous block of memory**.

This method ensures easy memory access but has limitations like **fragmentation**.

---

##  How It Works
- The **main memory** is divided into fixed-size or variable-size partitions.
- Each process is loaded into **one contiguous block** (all bytes stored together, without breaks).
- The OS keeps track of:
  - **Base Address** → starting location of the block.
  - **Limit Register** → size of the block.

---

##  Example

### Memory Layout
| Process P1 | Process P2 | Free Space | Process P3 |
| ---------- | ---------- | ---------- | ---------- |

Here:
- P1, P2, and P3 are stored in **adjacent memory cells**.
- No process is split into multiple locations.

---

##  Allocation Strategies
When choosing where to place a process in memory, the OS may use:

1. **First Fit** → Allocate the first available block large enough for the process.
2. **Best Fit** → Allocate the smallest available block that fits the process (minimizes wasted space).
3. **Worst Fit** → Allocate the largest available block (may help avoid fragmentation for large processes).

---

##  Advantages & Disadvantages

###  Advantages
- **Simple** to implement.
- **Fast** access due to sequential storage.
- Easy address translation using **base + offset**.

###  Disadvantages
- **External Fragmentation**: Free memory is scattered in small chunks.
- **Fixed-size partitioning** may waste memory (internal fragmentation).
- Not suitable for very large or dynamic processes.

---

##  Diagram

+---------------------------------------------------+
| P1 | P2 | Free Space | P3 | Free Space |
+---------------------------------------------------+
- All processes are in one continuous block.
- Free space may exist between processes (causing fragmentation).

---

##  Related Concepts
- **Non-contiguous Memory Allocation** → Processes split across multiple blocks (e.g., Paging, Segmentation).
- **Fragmentation** → Memory waste due to allocation patterns.

---

##  References
- [Operating System Concepts – Silberschatz et al.](https://www.os-book.com/)
- [GeeksforGeeks: Contiguous Memory Allocation](https://www.geeksforgeeks.org/contiguous-memory-allocation-in-operating-system/)

---
