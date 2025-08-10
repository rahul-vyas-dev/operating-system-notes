#  Semaphore

##  Introduction
A **Semaphore** is a synchronization tool used to control access to a shared resource by multiple processes in a concurrent system.

---

##  Definition
A semaphore uses a counter to keep track of how many units of a resource are available.  
- If the counter is **greater than 0**, a process can access the resource and decrement the counter.  
- If the counter is **0**, the process waits until another process releases the resource.

---

##  Types of Semaphore
1. **Binary Semaphore** → Value is `0` or `1`, similar to a mutex.
2. **Counting Semaphore** → Value can be any integer, allowing multiple accesses.

---

##  Methods
| Method       | Description |
|--------------|-------------|
| `wait()`     | Decreases semaphore count, waits if count is 0. |
| `signal()`   | Increases semaphore count, wakes up a waiting process. |

---

## Example (C)
```c
sem_t sem;
sem_init(&sem, 0, 1); // Initialize with value 1

sem_wait(&sem);       // Wait (P operation)
// Critical Section
sem_post(&sem);       // Signal (V operation)
```


     +-----------+
     |  Counter  |
     +-----------+
          |
    +-----------+
    |  > 0 ?    |
    +-----------+
       /    \
    Yes      No
   Access   Wait

















