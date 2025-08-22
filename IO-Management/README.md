# 📘 I/O Management in Operating System

## 🔹 Introduction
**I/O Management** in an Operating System deals with handling **input/output devices** (like keyboard, mouse, disk, printer, network cards) and coordinating their operations with the CPU and memory.  

Since I/O devices are slower than CPU and memory, efficient management is required to reduce CPU idle time and improve system performance.

---

## 🔹 Objectives of I/O Management
- ✅ Provide **abstraction** – hide hardware complexity.  
- ✅ Ensure **efficient CPU utilization** (CPU should not always wait for I/O).  
- ✅ Provide **fair access** to multiple processes.  
- ✅ Handle **errors and failures** in devices gracefully.  

---

##  Types of I/O Devices
- **Character Devices** → Keyboard, mouse, printer (stream of characters).  
- **Block Devices** → Hard disk, SSD (fixed-size blocks of data).  
- **Network Devices** → Network Interface Cards (NICs).  

---

##  I/O Techniques

### 1. **Programmed I/O**
- CPU continuously checks (polls) device until I/O completes.  
-  CPU time is wasted.  
- Example: Polling keyboard input.  

---

### 2. **Interrupt-Driven I/O**
- Device sends an **interrupt signal** to CPU when ready.  
-  CPU can do other tasks in the meantime.  
- Example: Keyboard generates interrupt when a key is pressed.  

---

### 3. **Direct Memory Access (DMA)**
- Special **DMA controller** transfers data directly between memory and I/O device.  
-  CPU is free for other work.  
- Example: Disk transferring data directly into RAM.  

---

##  I/O Buffering
Used to **match speed differences** between fast CPU/memory and slower I/O devices.  

- **Single Buffering** → One buffer between process and device.  
- **Double Buffering** → Two buffers, while one is filled the other is emptied.  
- **Circular Buffering** → Multiple buffers in a circular queue.  

---

##  I/O Spooling
**SPOOL = Simultaneous Peripheral Operation On-Line**  

- Uses **disk as a buffer** to hold output for slow devices (e.g., printer).  
- Example: Multiple print jobs stored in a spool, printer processes them one by one.  

---

##  I/O Scheduling
- Decides the **order of I/O operations** when multiple requests exist.  
- Improves throughput and reduces waiting.  
- Example: Disk Scheduling (FCFS, SSTF, SCAN, C-SCAN).  

---

##  Diagram: I/O System in OS
+----------------------+
| User Processes |
+----------------------+
|
v
+----------------------+
| I/O System Calls |
+----------------------+
|
v
+----------------------+
| Device Drivers |
+----------------------+
|
v
+----------------------+
| I/O Controllers |
+----------------------+
|
v
+----------------------+
| I/O Devices |
+----------------------+


---

##  Summary
- OS provides an interface to I/O devices.  
- Techniques: **Programmed I/O, Interrupts, DMA**.  
- Optimizations: **Buffering, Spooling, Scheduling**.  
- Goal: **Better CPU utilization + Fair I/O access**.  

---
