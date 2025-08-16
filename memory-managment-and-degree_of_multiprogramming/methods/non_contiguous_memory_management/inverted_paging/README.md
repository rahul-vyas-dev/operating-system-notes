# 📙 Inverted Page Table (IPT)

## 🔹 Introduction
Traditional paging → each process has its own page table.  
This is **memory-heavy** when many processes run.  

👉 Solution → use **Inverted Page Table (IPT)**:
- One global page table for the system.
- Each entry corresponds to a **frame** in physical memory.

---

## 🔹 How It Works
Each IPT entry contains:
- Process ID
- Virtual Page Number
- Control bits

**Example:**
Frame 0 → (PID 1, Page 0) Frame 1 → (PID 2, Page 3) Frame 2 → (PID 1, Page 1)

---

## ✅ Advantages
- Saves memory (only one table).
- Works well with large virtual address spaces.

## ❌ Disadvantages
- Slower lookup (may need hashing or associative memory).
- More complex design.
