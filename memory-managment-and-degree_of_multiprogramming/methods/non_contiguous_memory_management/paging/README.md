# Paging in Operating Systems

## Introduction
Paging is a **non-contiguous memory allocation technique** where:
- A process is divided into **fixed-size blocks** → called *Pages*.
- Main memory is divided into **same-size blocks** → called *Frames*.
- The OS uses a **Page Table** to map process pages to memory frames.

---

## How Paging Works
1. Process → divided into pages.
2. Memory → divided into frames.
3. Page Table → maps each page to its respective frame.

**Example:**
Logical Pages:  P0 | P1 | P2 | P3 Physical Frames: F2 | F5 | F1 | F7---

## Advantages
- Eliminates **external fragmentation**.
- Simple mapping using page tables.
- Supports **virtual memory**.

## Disadvantages
- **Internal fragmentation** (unused space in frames).
- Page tables consume extra memory.
