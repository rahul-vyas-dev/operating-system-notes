# Virtual Memory

## Introduction
Modern operating systems use **Virtual Memory** to handle large programs without worrying about the size of physical memory.

## Definition
Virtual Memory is a memory management technique where the operating system gives an **illusion of a large memory space** by combining physical memory (RAM) with disk storage.

## Working
- Programs are divided into fixed-size units called **pages**.  
- These pages are mapped between **virtual addresses** (used by program) and **physical addresses** (actual RAM).  
- If a required page is not in RAM, the OS loads it from disk (called **page fault handling**).  

## Advantages
- Allows execution of programs larger than physical RAM.  
- Provides process isolation (each process thinks it has its own memory).  
- Simplifies memory management for programmers.  

## Disadvantages
- Disk access is slower than RAM → may cause performance issues.  
- Page faults can reduce system speed if they happen frequently (thrashing).  

## Example / Analogy
Think of **virtual memory like a library card system**:  
- You don’t carry all the books at once.  
- You take only the needed ones to your desk (RAM).  
- If you need another, you swap it in from the library (disk).  
