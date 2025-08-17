# 📘 Contiguous Memory Allocation

## 🔹 Introduction
Contiguous allocation assigns **a single continuous block of memory** to each process.  
All instructions and data of the process are stored together.

---

## 🔹 How It Works
- OS searches for a free block of required size.
- Allocates the **entire block** to the process.
- Updates allocation records.

**Example:**
[Process A][Process B][Free Space][Process C]
bs

---

## ✅ Advantages
- Simple to implement.
- Fast access (sequential storage).
- Less bookkeeping.

## ❌ Disadvantages
- **External fragmentation**.
- Difficult to resize a process.
- Limited flexibility.
