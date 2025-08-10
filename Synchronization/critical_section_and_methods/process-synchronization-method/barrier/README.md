
---

### **`barrier/README.md`**
```markdown
#  Barrier
```

##  Introduction
A **Barrier** is a synchronization method that blocks all threads until all have reached the barrier point.

---

##  Definition
A barrier is useful when threads must all reach the same execution point before any can continue.

---

##  Methods
| Method              | Description |
|---------------------|-------------|
| `barrier_wait()`    | Waits until all threads reach the barrier. |

---

##  Example (C)
```c
pthread_barrier_t barrier;

pthread_barrier_init(&barrier, NULL, NUM_THREADS);
pthread_barrier_wait(&barrier);
```

 Thread 1 --->|
 Thread 2 --->|  Wait
 Thread 3 --->|
     All reached barrier
         |
     Continue execution



