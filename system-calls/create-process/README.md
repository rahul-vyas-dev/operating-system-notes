# Process Control System Calls (Create Processe)

These system calls deal with **creating, managing, and terminating processes**.

## Examples
- `fork()` – Creates a new process.
- `exec()` – Executes a new program in the current process.
- `exit()` – Terminates the current process.
- `wait()` – Waits for a child process to finish.

## Example in C
```c
#include <stdio.h>
#include <unistd.h>

int main() {
    fork(); // Creates a child process
    printf("Hello from process!\n");
    return 0;
}
