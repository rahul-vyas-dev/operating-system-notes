#  Multi-Level Paging

##  Introduction
In large processes, the **page table becomes very big**.  
To manage this, the OS uses **multi-level paging** → breaks the page table into smaller tables.

---

## How It Works
- Virtual address split into parts:
  - **Outer page number** → points to *page directory*.
  - **Inner page number** → points to actual *page table*.
- Can extend to 2, 3, or more levels.

**Example (2-Level Paging):**Virtual Address = [Outer Page No | Inner Page No | Offset]
---

## Advantages
- Saves memory → unused page tables not created.
- Scales well for **large address spaces** (e.g., 64-bit systems).

##  Disadvantages
- Increases **memory access time** (multiple lookups).
- More complex implementation.
