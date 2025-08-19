# Overlay

## Introduction
In early computer systems, memory was very limited. Programs often needed more memory than was physically available. To solve this, the **Overlay technique** was used.

## Definition
Overlay is a memory management technique that allows a program to be larger than the physical memory by keeping only the necessary instructions and data in memory at a time. Non-essential parts are replaced when required.

## Working
- Program is divided into modules (parts).  
- Only the required module is loaded into memory.  
- When another module is needed, it **overlays** (replaces) the previous one in the same memory space.  
- This way, a large program can run on a small memory system.

## Advantages
- Allows execution of large programs on small memory.  
- Saves cost since additional hardware is not needed.  

## Disadvantages
- Programmer must manually divide program into overlays.  
- Complex to manage.  
- Not efficient compared to modern techniques like Virtual Memory.  

## Example / Analogy
Think of a **small desk** where you can only keep one book open at a time.  
If you need another book, you must close the current one and replace it with the new one.  
This is similar to how overlay replaces modules in limited memory.
