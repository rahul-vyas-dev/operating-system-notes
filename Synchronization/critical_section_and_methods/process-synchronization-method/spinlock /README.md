
---

### **`spinlock/README.md`**
```markdown
#  Spinlock
```

##  Introduction
A **Spinlock** is a synchronization mechanism where a thread repeatedly checks (spins) until a lock becomes available.

---

##  Definition
Unlike mutexes, spinlocks do not put the thread to sleep — they keep checking, making them suitable for short critical sections.

---

##  Methods
| Method           | Description |
|------------------|-------------|
| `lock()`         | Acquires the lock (busy-wait until available). |
| `unlock()`       | Releases the lock. |

---

##  Example (C)
```c
while (atomic_flag_test_and_set(&lock)) {
    // Busy wait
}
```

// Critical Section
atomic_flag_clear(&lock);

   Try Lock
      |
  Locked? --- Yes --> Spin (loop)
      |
     No
      v
  Enter Critical Section




