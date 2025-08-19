# Overlay in Operating System

## 🔹 What is Overlay?
Overlay is a memory management technique used in early computer systems where the size of a program was **larger than the available main memory (RAM)**.  
The program is divided into parts, and only the required part is loaded into memory at a given time.

---

## 🔹 How it works:
- The program is split into **modules**.
- Only the **active module** is kept in memory.
- Other modules are stored on disk and loaded when needed, replacing the existing ones.

---

## 🔹 Example:
Imagine a 16 KB RAM system:
- Program size = 24 KB
- The program is divided into 3 modules (8 KB each).
- At a time, only one module loads into memory.
- When the next part is required, it **overlays** the previous one.

---

## 🔹 Advantages:
- Allowed execution of large programs on small memory systems.
- Efficient use of limited RAM.

## 🔹 Disadvantages:
- Increased programmer’s burden (programmer had to manually divide code).
- Performance loss due to frequent loading/unloading.
- Not needed in modern systems because **virtual memory** replaced overlays.
