
---

### **binary_semaphore.md**
```markdown
# Binary Semaphore
```

## Definition
A **Binary Semaphore** is a semaphore that can only have two values: `0` (resource unavailable) and `1` (resource available).  
It is often used for mutual exclusion (mutex).

---

## Working
- **Initialization:** Set semaphore to `1` (resource is free).
- **Wait(P):** Sets semaphore to `0` when a process acquires the resource.
- **Signal(V):** Sets semaphore to `1` when the resource is released.

---

## Example
If only one printer is available:
- Semaphore = `1` → Printer is free.
- When a process uses the printer, semaphore = `0` → No one else can use it until released.

---

## Methods
- **wait():**
  ```pseudo
  wait(S):
      while S == 0:
          wait
      S = 0
  signal():
    signal(S):
    S = 1
  
Initial: S = 1 (Resource free)

Process 1 -> Wait(P) -> S = 0 (Resource locked)
Process 2 -> Wait(P) -> Wait until S = 1
