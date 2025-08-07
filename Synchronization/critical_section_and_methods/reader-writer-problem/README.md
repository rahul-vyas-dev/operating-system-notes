
---

# Readers-Writers Problem

## Introduction
The **Readers-Writers Problem** deals with synchronizing access to a shared resource (e.g., a file or database) such that:

- Multiple **readers** can read the data **simultaneously**.
- Only **one writer** can write at a time.
- If a writer is writing, **no other reader or writer** can access the resource.

The key challenge is to avoid **starvation** and ensure **fairness**.

---

## Access Flow (Chart)

```text
                  +-------------------+
        +-------->|     Reader       |
        |         +-------------------+
        |         [Can proceed if no writer]
        |                 |
        |        +-------------------+
        |        | Read Shared Data  |
        |        +-------------------+
        |
+---------------+                     +---------------+
| Shared Data   |<------------------->|    Writer     |
+---------------+                     +---------------+
        ^                                [Wait if readers or writers]
        |                                +-------------------+
        +--------------------------------| Write to Data     |
                                         +-------------------+
```

---

## Solution Outline (Semaphore-Based)

```c
int readcount = 0;
semaphore mutex = 1;
semaphore wrt = 1;

Reader() {
    wait(mutex);
    readcount++;
    if (readcount == 1)
        wait(wrt); // first reader locks writer
    signal(mutex);

    read_data();

    wait(mutex);
    readcount--;
    if (readcount == 0)
        signal(wrt); // last reader unlocks writer
    signal(mutex);
}

Writer() {
    wait(wrt);
    write_data();
    signal(wrt);
}
```

---

## Variants

1. **First Readers-Writers Problem** (Readers priority, writers may starve)
2. **Second Readers-Writers Problem** (Writers priority, readers may starve)
3. **Third Readers-Writers Problem** (Fairness, no starvation)

---

# Summary
| Problem             | Readers-Writers                        | Producer-Consumer                     |
|---------------------|----------------------------------------|---------------------------------------|
| Resource Type       | Shared memory (read/write)             | Bounded buffer                        |
| Process Types       | Readers & Writers                      | Producers & Consumers                 |
| Goal                | Allow multiple readers or 1 writer     | Synchronize buffer access             |
| Tools Used          | Semaphores, Mutex                      | Semaphores, Mutex                     |
| Key Challenges      | Starvation, Fairness                   | Buffer underflow/overflow             |

---

>  These are classic problems that help build an understanding of synchronization, inter-process communication, and the use of semaphores/mutexes.
