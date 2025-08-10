# Mutex (Mutual Exclusion Object)

## Purpose
Ensures **only one** process/thread accesses a shared resource at a time.

---

## How It Works
1. Lock the mutex before entering the critical section.
2. Execute the critical section.
3. Unlock the mutex.

---

## Example (C)
```c
pthread_mutex_t lock;
pthread_mutex_lock(&lock);
// Critical Section
pthread_mutex_unlock(&lock);
