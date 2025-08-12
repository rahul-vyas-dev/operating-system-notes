# Memory Management & Degree of Multiprogramming

## Introduction

In an operating system, **memory management** is the process of efficiently handling the computer’s memory so that multiple processes can run without interfering with each other.  
It is one of the most critical OS functions because it directly affects **CPU utilization**, **system speed**, and the **degree of multiprogramming**.

---

## Memory Management

### **Definition**

Memory management refers to **the process of controlling and coordinating computer memory** by allocating memory blocks to programs, ensuring that each process gets the memory it needs while preventing conflicts.

### **Key Functions**

1. **Allocation** – Assigning memory to processes.
2. **Deallocation** – Releasing memory after use.
3. **Tracking** – Keeping track of which parts of memory are used and by which process.
4. **Protection** – Preventing unauthorized access between processes.

---

### **Types of Memory Management**

| Type                          | Description                                                        |
| ----------------------------- | ------------------------------------------------------------------ |
| **Contiguous Allocation**     | Memory is assigned in a single continuous block.                   |
| **Non-Contiguous Allocation** | Memory can be allocated in separate blocks (Paging, Segmentation). |
| **Virtual Memory**            | Allows execution of processes not completely in main memory.       |
| **Swapping**                  | Temporarily moves processes in and out of main memory.             |

---

### **Diagram – Basic Memory Layout**

+-------------------+
| Operating System |
+-------------------+
| Process A |
+-------------------+
| Process B |
+-------------------+
| Free Memory |
+-------------------+

---

## Degree of Multiprogramming

### **Definition**

The **Degree of Multiprogramming** refers to the **number of processes that are present in the main memory at a given time**.

Higher multiprogramming → Better CPU utilization (to an extent).  
Too high → May lead to **thrashing** (too much time spent on swapping instead of execution).

---

### **Relation Between Memory Management & Multiprogramming**

- **Efficient memory management** → Allows more processes to be loaded → **Higher degree of multiprogramming**.
- Poor memory management → Less processes can fit in memory → Lower CPU utilization.

---

### **Example**

If a system has **4 GB RAM** and each process requires **1 GB**, then:
Degree of Multiprogramming = 4 processes

If better memory management is implemented (e.g., paging), more processes can be accommodated.

---

### **Graph – CPU Utilization vs Degree of Multiprogramming**

CPU Utilization
^
| ****\*****
| \*\* **
| ** **
| ** **
|\_**********\_\_\_\_********> Degree of Multiprogramming
