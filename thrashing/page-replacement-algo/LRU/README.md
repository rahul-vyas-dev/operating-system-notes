```markdown
# LRU (Least Recently Used) Page Replacement
```

## Concept  
- Replace the page that has not been used for the **longest time in the past**.  
- Tracks recent usage history.  

---

## Example  
Pages: `7, 0, 1, 2, 0, 3, 0, 4`  
Frames: `3`  

1. Insert `7, 0, 1` → [7, 0, 1]  
2. Next `2`: Replace `7` (least recently used) → [2, 0, 1]  
3. Next `0`: Already present → [2, 0, 1]  
4. Next `3`: Replace `1` → [2, 0, 3]  
5. Continue similarly…  

---

## Python Code  
```python
def lru(pages, frames):
    memory = []
    page_faults = 0
    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                # Find least recently used
                recent = pages[:i]
                lru_page = None
                farthest = -1
                for mem_page in memory:
                    if mem_page in recent:
                        last_used = len(recent) - 1 - recent[::-1].index(mem_page)
                        if last_used > farthest:
                            farthest = last_used
                            lru_page = mem_page
                    else:
                        lru_page = mem_page
                        break
                memory[memory.index(lru_page)] = page
            page_faults += 1
        print(f"Page {page}: {memory}")
    print(f"Total Page Faults: {page_faults}")
```

pages = [7, 0, 1, 2, 0, 3, 0, 4]
lru(pages, 3)
