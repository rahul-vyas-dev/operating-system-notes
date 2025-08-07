---
# Consumer-Producer Problem

##  Introduction
The **Consumer-Producer Problem** (also called the **Bounded Buffer Problem**) is a classic example of a multi-process synchronization issue. The problem describes two types of processes: producers and consumers, which share a common, fixed-size buffer.

- **Producer** adds items to the buffer.
- **Consumer** removes items from the buffer.

Proper synchronization is needed to ensure that:
- The producer doesn't add items into a full buffer.
- The consumer doesn't remove items from an empty buffer.

This problem is solved using semaphores or mutexes with condition variables.

---

## Synchronization Flow (Chart)

```text
                 +-------------------+
        +------->|    Producer       |
        |        +-------------------+
        |                 |
        |         [Wait if buffer full]
        |                 |
        |        +-------------------+
        |        | Add item to buffer|
        |        +-------------------+
        |                 |
        |                 v
+---------------+    +---------------+    +---------------+
|   Empty Slot  |<---| Shared Buffer |--->| Filled Slot   |
+---------------+    +---------------+    +---------------+
        ^                 |
        |         [Wait if buffer empty]
        |                 |
        |        +-------------------+
        |        |   Remove item     |
        +--------|   (Consumer)      <--------+
                 +-------------------+         |
```

---

## Solution Outline (Semaphore-Based)

```c
semaphore full = 0;
semaphore empty = n;
mutex buffer_mutex;

Producer() {
    while(true) {
        produce_item();
        wait(empty);
        wait(buffer_mutex);
        insert_item();
        signal(buffer_mutex);
        signal(full);
    }
}

Consumer() {
    while(true) {
        wait(full);
        wait(buffer_mutex);
        remove_item();
        signal(buffer_mutex);
        signal(empty);
        consume_item();
    }
}
```
