# Counting Semaphore

## Definition
A **Counting Semaphore** allows a resource to be accessed by multiple processes at the same time. The semaphore variable can hold values greater than 1, representing the number of available instances of the resource.

---

## Working
- **Initialization:** Set semaphore value to the number of available resources.
- **Wait(P):** Decreases the semaphore value when a process acquires the resource.
- **Signal(V):** Increases the semaphore value when a process releases the resource.

---

## Example
Suppose we have 3 printers in a network:
- Semaphore initialized to `3`
- If 2 processes are using printers, semaphore = `1`
- When all printers are in use, semaphore = `0` and other processes must wait.

---

## Methods
- **wait():**
  ```pseudo
  wait(S):
      while S <= 0:
          wait
      S = S - 1
  signal():
    S = S + 1
  
Initial: S = 3 (3 resources)

Process 1 -> Wait(P) -> S = 2
Process 2 -> Wait(P) -> S = 1
Process 3 -> Wait(P) -> S = 0
Process 4 -> Wait(P) -> Wait until S > 0

