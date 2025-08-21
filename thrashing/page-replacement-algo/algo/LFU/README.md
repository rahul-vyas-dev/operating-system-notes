
---

### `.md`
```markdown
# LFU (Least Frequently Used) Page Replacement
```

## Concept  
- Replace the page with the **least number of references**.  
- Uses a counter for each page.  

---

## Example  
Pages: `7, 0, 1, 2, 0, 3, 0, 4`  
Frames: `3`  

- Count frequencies.  
- When replacement is needed, evict page with **lowest frequency**.  

---

## Python Code  
```python
from collections import defaultdict

def lfu(pages, frames):
    memory = []
    freq = defaultdict(int)
    page_faults = 0
    
    for page in pages:
        freq[page] += 1
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                # Find least frequently used
                lfu_page = min(memory, key=lambda x: freq[x])
                memory[memory.index(lfu_page)] = page
            page_faults += 1
        print(f"Page {page}: {memory}")
    print(f"Total Page Faults: {page_faults}")
```

pages = [7, 0, 1, 2, 0, 3, 0, 4]
lfu(pages, 3)
