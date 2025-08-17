

#  Segmented Paging

## 🔹 Introduction
Segmented Paging is a **hybrid memory management scheme** that combines:
- **Segmentation** → Divides program into logical segments (Code, Data, Stack, etc.).
- **Paging** → Each segment is further divided into fixed-size pages.

 This solves the **external fragmentation problem** of segmentation while keeping the **logical structure**.

---

## 🔹 How It Works
1. A process is divided into **segments** (Code, Data, Stack).
2. Each segment is divided into **pages** of fixed size.
3. The OS maintains a **Segment Table**:
   - Each entry points to a **Page Table** for that segment.
4. The Page Table maps logical pages → physical frames.

---

## 🔹 Address Translation
A logical address is represented as:

< Segment Number , Page Number , Offset >

**Steps:**
1. Use **Segment Number** → find the base address of the Page Table for that segment.
2. Use **Page Number** → find the frame number.
3. Add **Offset** → get the exact physical address.

---

## 🔹 Example
Suppose:
- Segment 0 → Code  
- Segment 1 → Data  

Virtual Address = `<1, 3, 50>`  
- Segment = **1** (Data Segment)  
- Page = **3** → mapped to Frame 6  
- Offset = **50**  

👉 Final Physical Address = Frame 6 + 50  

---

## ✅ Advantages
- Removes **external fragmentation** (because of paging).
- Retains **logical division** (segmentation).
- Efficient memory utilization.

## ❌ Disadvantages
- More **complex translation** (two tables involved).
- Requires more memory for storing both **Segment Tables** and **Page Tables**.


---
