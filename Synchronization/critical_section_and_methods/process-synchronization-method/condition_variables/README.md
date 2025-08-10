
---

### **`condition_variables`**
```markdown
#  Condition Variables
```

##  Introduction
**Condition variables** allow threads to wait until a certain condition becomes true.

---

##  Definition
A condition variable is always used with a mutex to:
- Block a thread until a condition is signaled.
- Allow other threads to run while waiting.

---

##  Methods
| Method                  | Description |
|-------------------------|-------------|
| `wait(mutex)`           | Waits for the condition to be signaled. |
| `signal()`              | Wakes up one waiting thread. |
| `broadcast()`           | Wakes up all waiting threads. |

---

## Example (C)
```c
pthread_mutex_t lock;
pthread_cond_t cond;

pthread_mutex_lock(&lock);
while (!condition) {
    pthread_cond_wait(&cond, &lock);
}
pthread_mutex_unlock(&lock);
```

   [Thread]
      |
      v
 Wait for Signal <--+
      |             |
    Condition Met --+






