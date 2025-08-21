```markdown
# Clock (Second-Chance) Page Replacement  
```

### Concept  
- Circular buffer with a **"use bit"**.  
- Works like FIFO but gives each page a "second chance".  

---

### Algorithm Steps  
1. Keep pages in circular list.  
2. Each page has a reference bit (0 or 1).  
3. On replacement:  
   - If bit = 0 → replace page.  
   - If bit = 1 → set to 0 and move clock hand forward.  

---

### Pros & Cons  
✅ More efficient than FIFO  
❌ Slightly complex to implement  

---

(Python code can be added later)  
