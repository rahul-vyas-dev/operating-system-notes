# 📗 Segmentation in Operating Systems

## 🔹 Introduction
Segmentation divides memory into **variable-sized segments** based on logical divisions of a program (like code, data, stack).  
Each segment has a **base address** and **limit**.

---

## 🔹 How It Works
- Program is split into logical parts (functions, arrays, stack).
- Each segment is stored separately.
- OS maintains a **Segment Table**:
  - Base → starting address
  - Limit → length of segment

**Example Segment Table:**
Segment   Base   Limit Code      1000   400 Data      2000   600 Stack     3000   300

---

## ✅ Advantages
- Logical division (programmer-friendly).
- Supports dynamic growth of segments.
- No internal fragmentation.

## ❌ Disadvantages
- Causes **external fragmentation**.
- More complex memory management.
