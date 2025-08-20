```markdown
# Optimal Page Replacement  

## Concept  
- Replace the page that will not be used for the **longest time in the future**.  
- Gives minimum page faults.  
- Used as **theoretical benchmark**.  
```
---

## Example  
Pages: `7, 0, 1, 2, 0, 3, 0, 4`  
Frames: `3`  

1. Insert `7, 0, 1` → [7, 0, 1]  
2. Next `2`: Future use → `7` used farthest → Replace `7` → [2, 0, 1]  
3. Next `0`: Already present → No replacement  
4. Next `3`: Replace the one used farthest (`1`) → [2, 0, 3]  
5. Continue similarly…  

---

## Python Code  
```python
def optimal(pages, frames):
    memory = []
    page_faults = 0
    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                future = pages[i+1:]
                index = -1
                farthest = -1
                for mem_page in memory:
                    if mem_page in future:
                        next_use = future.index(mem_page)
                        if next_use > farthest:
                            farthest = next_use
                            index = mem_page
                    else:
                        index = mem_page
                        break
                memory[memory.index(index)] = pages[i]
            page_faults += 1
        print(f"Page {pages[i]}: {memory}")
    print(f"Total Page Faults: {page_faults}")

pages = [7, 0, 1, 2, 0, 3, 0, 4]
optimal(pages, 3)
