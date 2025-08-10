
---

### **`monitor`**

```markdown
#  Monitor
```
##  Introduction
A **Monitor** is a high-level synchronization construct that ensures **only one process** executes a monitor procedure at a time.

---

##  Definition
A monitor combines:
- **Mutex** (for mutual exclusion)
- **Condition variables** (for signaling and waiting)

---

## Methods
| Method          | Description |
|-----------------|-------------|
| `wait()`        | Process waits for a condition. |
| `signal()`      | Wakes up a process waiting for a condition. |

---

##  Example (Java)
```java
class BankAccount {
    private int balance = 0;

    public synchronized void deposit(int amount) {
        balance += amount;
        notify();
    }

    public synchronized void withdraw(int amount) throws InterruptedException {
        while (balance < amount) {
            wait();
        }
        balance -= amount;
    }
}






