# FIFO (First In, First Out) Page Replacement  

## Concept  
- Oldest page in memory is replaced first.  
- Implemented using a **queue**.  

---

## Example  
Pages: `7, 0, 1, 2, 0, 3, 0, 4`  
Frames: `3`  

Step-by-step:  
1. Insert `7, 0, 1` → [7, 0, 1]  
2. Next page `2` → Replace `7` → [2, 0, 1]  
3. Next page `0` → Already in memory → No replacement  
4. Next page `3` → Replace `0` → [2, 3, 1]  
5. Next page `0` → Replace `1` → [2, 3, 0]  
6. Next page `4` → Replace `2` → [4, 3, 0]  

---

## Python Code  
```python
def fifo(pages, frames):
    memory = []
    page_faults = 0
    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
        print(f"Page {page}: {memory}")
    print(f"Total Page Faults: {page_faults}")

pages = [7, 0, 1, 2, 0, 3, 0, 4]
fifo(pages, 3)
