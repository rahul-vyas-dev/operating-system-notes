# 📕 Virtual Memory

## 🔹 Introduction
Virtual memory allows execution of processes that are **larger than physical memory** by using disk as an extension of RAM.  
Implemented using **Paging + Demand Paging**.

---

## 🔹 Key Concepts
- **Demand Paging** → Only required pages are loaded into memory.
- **Page Fault** → Occurs when the needed page is not in memory.
- **Thrashing** → Excessive page faults reduce CPU efficiency.

---

## 🔹 Example
If RAM = 2 GB and program = 5 GB:
- Only active pages are kept in RAM.
- Inactive pages stored on disk.
- OS swaps pages in and out.

---

## ✅ Advantages
- Allows large programs to run.
- Efficient use of memory.
- Provides isolation between processes.

## ❌ Disadvantages
- Slower performance (due to disk access).
- Thrashing can degrade system efficiency.
